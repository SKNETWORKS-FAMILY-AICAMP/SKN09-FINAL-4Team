from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from user.models import User
from .models import Chat, Message, Content, MessageImage
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from dogs.models import DogProfile, DogBreed
from django.http import HttpResponseNotAllowed
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from user.utils import get_logged_in_user
from collections import defaultdict
from datetime import date, timedelta
import uuid
import requests
from chat.utils import get_image_response
from urllib.parse import quote
from django.urls import reverse

def chat_entry(request):
    if request.session.get('guest'):
        return redirect('chat:main')

    elif request.session.get('user_id'):
        dog_id = request.session.get('current_dog_id')
        if dog_id:
            return redirect('chat:chat_member', dog_id=dog_id)
        else:
            return redirect('dogs:dog_info_join')

    else:
        return redirect('user:home')
    
def group_chats_by_date(chat_list):
    today = date.today()
    yesterday = today - timedelta(days=1)
    grouped = defaultdict(list)

    for chat in chat_list:
        created = chat.created_at.date()
        if created == today:
            label = "오늘"
        elif created == yesterday:
            label = "어제"
        else:
            label = created.strftime("%Y.%m.%d")
        grouped[label].append(chat)

    return dict(grouped)

def chat_member_view(request, dog_id):
    user = get_logged_in_user(request)
    if not user:
        return redirect('user:home')

    dog = get_object_or_404(DogProfile, id=dog_id, user=user)

    dog_list = DogProfile.objects.filter(user=user).order_by('created_at')

    chat_list = Chat.objects.filter(dog=dog).order_by('-created_at')
    grouped_chat_list = group_chats_by_date(chat_list)
    current_chat = Chat.objects.filter(dog=dog).order_by('-created_at').first()
    messages = Message.objects.filter(chat=current_chat).order_by('created_at') if current_chat else []

    request.session['current_dog_id'] = dog.id

    return render(request, 'chat/chat.html', {
        'grouped_chat_list': grouped_chat_list,
        'chat_list': chat_list,
        'current_chat': current_chat,
        'chat_messages': messages,
        'is_guest': False,
        'user_email': user.email,
        'dog': dog,
        'dog_list': dog_list,
    })


@csrf_exempt
@require_http_methods(["GET", "POST"])
def guest_profile_register(request):
    if request.method == 'GET':
        request.session.flush()
        request.session['guest'] = True

        guest_email = f"guest_{uuid.uuid4().hex[:10]}@example.com"
        guest_user = User.objects.create(email=guest_email, password='guest_pw')
        request.session['guest_user_id'] = str(guest_user.id)
        request.session['user_email'] = guest_email

        return redirect('chat:main')

    elif request.method == 'POST':
        guest_name = request.POST.get("guest_name", "").strip()
        guest_breed = request.POST.get("guest_breed", "").strip()

        if not guest_name or not guest_breed:
            return redirect('chat:main')

        request.session["guest_dog_name"] = guest_name
        request.session["guest_dog_breed"] = guest_breed

        guest_user_id = request.session.get("guest_user_id")
        user = User.objects.get(id=guest_user_id)

        chat = Chat.objects.create(user=user, dog=None, chat_title="비회원 상담 시작")
        welcome_message = f"{guest_name}의 상담을 시작해볼까요? 😊"
        Message.objects.create(chat=chat, sender="bot", message=welcome_message)
        request.session["current_chat_id"] = str(chat.id)

        return redirect('chat:chat_talk_detail', chat_id=chat.id)

    return HttpResponseNotAllowed(['GET', 'POST'])


@require_http_methods(["GET", "POST"])
def chat_member_talk_detail(request, dog_id, chat_id):
    user_id = request.session.get("user_id")
    if not user_id:
        return JsonResponse({'error': '로그인 필요'}, status=401)  # 로그인 안 된 경우 JSON 응답으로 처리

    try:
        user = User.objects.get(id=uuid.UUID(user_id))
    except (User.DoesNotExist, ValueError):
        return JsonResponse({'error': '사용자를 찾을 수 없습니다.'}, status=404)  # 사용자 없음

    dog = get_object_or_404(DogProfile, id=dog_id, user=user)
    chat = get_object_or_404(Chat, id=chat_id, dog=dog)

    if request.method == "POST":
        message = request.POST.get("message", "").strip()
        image_files = request.FILES.getlist("images")

        if message:
            user_message = Message.objects.create(chat=chat, sender='user', message=message)
        elif image_files:
            user_message = Message.objects.create(chat=chat, sender='user', message="[이미지 전송]")
        else:
            return JsonResponse({'error': '메시지나 이미지를 입력해주세요.'}, status=400)  # 메시지나 이미지 없을 경우

        for img in image_files[:3]:
            try:
                MessageImage.objects.create(message=user_message, image=img)
            except Exception:
                pass

        if image_files:
            answer = get_image_response(image_files, message)
        elif message:
            user_info = get_dog_info(dog)
            answer = call_runpod_api(message, user_info)
        else:
            answer = "질문이나 이미지를 입력해주세요."

        Message.objects.create(chat=chat, sender='bot', message=answer)

        # 리디렉션 대신 JSON 응답 반환
        return JsonResponse({'response': answer, 'chat_id': chat.id})  # JSON 응답으로 변경

    messages = Message.objects.filter(chat=chat).prefetch_related("images").order_by('created_at')
    chat_list = Chat.objects.filter(dog=dog).order_by('-created_at')
    grouped_chat_list = group_chats_by_date(chat_list)

    dog_list = DogProfile.objects.filter(user=user).order_by('created_at')

    return render(request, "chat/chat_talk.html", {
        "messages": messages,
        "current_chat": chat,
        "chat_list": chat_list,
        "grouped_chat_list": grouped_chat_list,
        "user_email": user.email,
        "is_guest": False,
        "now_time": timezone.localtime().strftime("%I:%M %p").lower(),
        "dog": dog,
        "dog_list": dog_list,
    })


def chat_main(request):
    is_guest = request.session.get("guest", False)
    user_id = request.session.get("user_id")
    guest_user_id = request.session.get("guest_user_id")
    user_email = request.session.get("user_email")
    current_dog_id = request.session.get("current_dog_id")
    current_chat_id = request.session.get("current_chat_id")

    guest_name = request.session.get("guest_dog_name")
    guest_breed = request.session.get("guest_dog_breed")

    dog_breeds = DogBreed.objects.all().order_by("name")

    if is_guest and (not guest_name or not guest_breed):
        return render(request, "chat/chat.html", {
            "show_guest_info_form": True,
            "is_guest": True,
            "dog_breeds": dog_breeds,
        })

    chat_list, current_chat, messages = [], None, []

    if user_id and not is_guest:
        try:
            user = User.objects.get(id=user_id)
            chat_list = Chat.objects.filter(dog__user=user).order_by('-created_at')

            if current_dog_id:
                current_chat = Chat.objects.filter(dog__id=current_dog_id).first()
            else:
                current_chat = chat_list.first()
                if current_chat and current_chat.dog:
                    request.session["current_dog_id"] = current_chat.dog.id

        except User.DoesNotExist:
            return redirect('user:home')

    elif is_guest and guest_user_id:
        try:
            user = User.objects.get(id=guest_user_id)
            chat_list = Chat.objects.filter(dog=None, user=user).order_by('-created_at')

            if current_chat_id:
                current_chat = Chat.objects.filter(id=current_chat_id, user=user).first()

            if not current_chat:
                current_chat = chat_list.first()

            if not current_chat:
                current_chat = Chat.objects.create(user=user, dog=None, chat_title="비회원 상담 시작")
                Message.objects.create(chat=current_chat, sender="bot", message=f"{guest_name}의 상담을 시작해볼까요? 😊")
                chat_list = Chat.objects.filter(dog=None, user=user).order_by('-created_at')

            request.session["current_chat_id"] = str(current_chat.id)

        except User.DoesNotExist:
            return redirect('user:home')

    else:
        return redirect('user:home')

    if current_chat:
        messages = Message.objects.filter(chat=current_chat).order_by('created_at')

    return render(request, 'chat/chat.html', {
        'chat_list': chat_list,
        'current_chat': current_chat,
        'chat_messages': messages,
        'is_guest': is_guest,
        'user_email': user_email,
        'guest_dog_name': guest_name,
        'guest_dog_breed': guest_breed,
        'dog_breeds': dog_breeds,
        'show_guest_info_form': False,
        'show_login_notice': is_guest 
    })

def chat_switch_dog(request, dog_id):
    user_id = request.session.get("user_id")
    if not user_id:
        return redirect("user:home")

    dog = get_object_or_404(DogProfile, id=dog_id, user_id=user_id)

    return redirect('chat:chat_member', dog_id=dog.id)
    
def get_dog_info(dog, chat=None, user_id=None):
    if chat is not None:
        chat_history, prev_q, prev_a = get_chat_history(chat)
    else:
        chat_history, prev_q, prev_a = [], None, None

    def safe(v, default="모름"):
        if v is None:
            return default
        if isinstance(default, str) and isinstance(v, int):
            return str(v)
        return v

    info = {
        "name": safe(dog.name, ""),
        "breed": safe(getattr(dog, "breed_name", None)),
        "age": safe(dog.age),
        "gender": safe(dog.gender),
        "neutered": safe(dog.neutered),
        "disease": safe("있음" if dog.disease_history else "없음"),
        "disease_desc": safe(dog.disease_history, ""),
        "period": safe(dog.living_period),
        "housing": safe(dog.housing_type),
        "chat_history": chat_history,
        "prev_q": prev_q,
        "prev_a": prev_a,
        "prev_cate": None,
        "is_first_question": len(chat_history) == 0,
        "user_id": user_id if user_id else (str(dog.user.id) if hasattr(dog, "user") else "unknown")
    }
    return info

def get_minimal_guest_info(session, chat=None, user_id=None):
    name = session.get("guest_dog_name", "비회원견")
    breed = session.get("guest_dog_breed", "견종 정보 없음")
    if chat is not None:
        chat_history, prev_q, prev_a = get_chat_history(chat)
    else:
        chat_history, prev_q, prev_a = [], None, None

    info = {
        "name": name,
        "breed": breed,
        "age": "모름",
        "gender": "모름",
        "neutered": "모름",
        "disease": "모름",
        "disease_desc": "",
        "period": "모름",
        "housing": "모름",
        "chat_history": chat_history,
        "prev_q": prev_q,
        "prev_a": prev_a,
        "prev_cate": None,
        "is_first_question": len(chat_history) == 0,
        "user_id": user_id if user_id else session.get("guest_user_id", "guest")
    }
    return info

def get_chat_history(chat):
    past_msgs = Message.objects.filter(chat=chat).order_by("created_at")
    chat_history = [
        {"role": "user" if m.sender == "user" else "assistant", "content": m.message}
        for m in past_msgs
    ]
    prev_q, prev_a = None, None
    for i in range(len(chat_history) - 2, -1, -2):
        if chat_history[i]["role"] == "user" and chat_history[i + 1]["role"] == "assistant":
            prev_q = chat_history[i]["content"]
            prev_a = chat_history[i + 1]["content"]
            break
    return chat_history, prev_q, prev_a

def call_runpod_api(message, dog_info):
    try:
        api_url = "http://213.173.105.9:32652/chat"
        payload = {
            "message": message,
            "dog_info": dog_info
        }
        res = requests.post(api_url, json=payload, timeout=120)
        res.raise_for_status()
        data = res.json()
        return data.get("response", "⚠️ 응답이 없습니다.")
    except Exception as e:
        return f"❗ 오류 발생: {str(e)}"



@require_POST
@csrf_exempt
def chat_send(request):
    is_guest = request.session.get('guest', False)
    user_id = request.session.get("guest_user_id") if is_guest else request.session.get("user_id")
    
    if not user_id:
        # 로그인 안 됐을 경우: 로그인 페이지로 이동 or 에러 페이지
        return redirect('user:login')

    user = get_object_or_404(User, id=user_id)
    message = request.POST.get("message", "").strip()
    image_files = request.FILES.getlist("images")

    if not message and not image_files:
        # 메시지나 이미지가 없으면 다시 채팅 입력 폼으로 리다이렉트
        return redirect(request.META.get('HTTP_REFERER', '/'))

    # ---- 비회원일 때 ----
    if is_guest:
        chat_id = request.session.get("current_chat_id")
        chat = Chat.objects.filter(id=chat_id, user=user).first()

        if not chat:
            chat = Chat.objects.create(user=user, dog=None, chat_title=message[:20] if message else "비회원 상담")
            request.session["current_chat_id"] = str(chat.id)

        user_message = Message.objects.create(
            chat=chat,
            sender="user",
            message=message if message else "[이미지 전송]"
        )

        for img in image_files[:3]:
            try:
                MessageImage.objects.create(message=user_message, image=img)
            except Exception:
                pass

        # 답변 생성은 여기서 하지 않음 (대화 상세에서 비동기로 처리)
        # 대화방 상세 페이지로 리다이렉트, just_sent=1 파라미터 부여
        return redirect('chat:chat_talk_detail', chat_id=chat.id)

    # ---- 회원/반려견일 때 ----
    current_dog_id = request.session.get("current_dog_id")
    dog = DogProfile.objects.filter(id=current_dog_id, user=user).first()

    if not dog:
        # 반려견 선택 안 됐을 때
        return redirect('dogs:dog_info_join')

    chat = Chat.objects.create(
        dog=dog,
        user=user,
        chat_title=message[:20] if message else "상담 시작"
    )

    user_message = Message.objects.create(
        chat=chat,
        sender="user",
        message=message if message else "[이미지 전송]"
    )

    for img in image_files[:3]:
        try:
            MessageImage.objects.create(message=user_message, image=img)
        except Exception:
            pass

    # 답변 생성은 여기서 하지 않음 (대화 상세에서 비동기로 처리)
    url = reverse('chat:chat_member_talk_detail', args=[dog.id, chat.id])
    return redirect(f"{url}?just_sent=1&last_msg={quote(message)}")



@require_POST
@csrf_exempt
def chat_member_delete(request, chat_id):
    try:
        chat = Chat.objects.get(id=chat_id)
        user_id = request.session.get('user_id')

        if not user_id or str(chat.dog.user.id) != str(user_id):
            return JsonResponse({'status': 'unauthorized'}, status=403)

        chat.delete()
        return JsonResponse({'status': 'ok'})
    except Chat.DoesNotExist:
        return JsonResponse({'status': 'not_found'}, status=404)
    

@require_POST
@csrf_exempt
def chat_member_update_title(request, chat_id):
    import json
    try:
        chat = Chat.objects.get(id=chat_id)
        user_id = request.session.get('user_id')

        if not user_id or str(chat.dog.user.id) != str(user_id):
            return JsonResponse({'status': 'unauthorized'}, status=403)

        data = json.loads(request.body)
        new_title = data.get('title', '').strip()
        if new_title:
            chat.chat_title = new_title
            chat.save()
            return JsonResponse({'status': 'ok'})
        return JsonResponse({'status': 'empty_title'}, status=400)
    except Chat.DoesNotExist:
        return JsonResponse({'status': 'not_found'}, status=404)
    

@require_http_methods(["GET", "POST"])
def chat_talk_view(request, chat_id):
    is_guest = request.session.get('guest', False)
    user_email = request.session.get("user_email")
    current_dog_id = request.session.get("current_dog_id")
    user_id = request.session.get("guest_user_id") if is_guest else request.session.get("user_id")

    try:
        chat = Chat.objects.get(id=chat_id)
    except Chat.DoesNotExist:
        return JsonResponse({'error': '채팅을 찾을 수 없습니다.'}, status=404) 

    if not is_guest:
        if not user_id or not chat.user or str(chat.user.id) != str(user_id):
            return JsonResponse({'error': '권한이 없습니다.'}, status=403)  

    if request.method == "POST":
        message_text = request.POST.get("message", "").strip()
        image_files = request.FILES.getlist("images")

        if not message_text and not image_files:
            return JsonResponse({'error': '메시지나 이미지가 필요합니다.'}, status=400)  

        user_message = Message.objects.create(
            chat=chat,
            sender='user',
            message=message_text if message_text else "[이미지 전송]"
        )

        for img in image_files[:3]:
            try:
                MessageImage.objects.create(message=user_message, image=img)
            except Exception:
                pass

        if image_files:
            answer = get_image_response(image_files, user_message)
        else:
            if is_guest:
                user_info = get_minimal_guest_info(request.session)
            else:
                user = get_object_or_404(User, id=user_id)
                chat_history, prev_q, prev_a = get_chat_history(chat)
                user_info = get_dog_info(chat.dog)
                user_info.update({
                    "chat_history": chat_history,
                    "prev_q": prev_q,
                    "prev_a": prev_a,
                    "prev_cate": None,
                    "is_first_question": len(chat_history) == 0,
                    "user_id": str(user.id)
                })

            answer = call_runpod_api(message_text, user_info)

        Message.objects.create(chat=chat, sender='bot', message=answer)

        # 리디렉션 대신 JSON 응답을 반환
        return JsonResponse({'response': answer, 'chat_id': chat.id})  # JSON 응답으로 변경

    messages = Message.objects.filter(chat=chat).prefetch_related("images").order_by('created_at')
    chat_list = Chat.objects.filter(user__id=user_id).order_by('-created_at') if not is_guest else []
    now_time = timezone.localtime().strftime("%I:%M %p").lower()

    dog = chat.dog if not is_guest else None
    dog_list = DogProfile.objects.filter(user__id=user_id).order_by('created_at') if dog else []

    return render(request, "chat/chat_talk.html", {
        "messages": messages,
        "current_chat": chat,
        "chat_list": chat_list,
        "user_email": user_email,
        "is_guest": is_guest,
        "now_time": now_time,
        "dog": dog,
        "dog_list": dog_list
    })




def recommend_content(request, chat_id):
    if not request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({"error": "Invalid request"}, status=400)

    if request.session.get("guest", False):
        return JsonResponse({
            "error": "비회원은 추천 콘텐츠를 이용할 수 없습니다.",
            "cards_html": "",
            "has_recommendation": False
        }, status=403)

    chat = Chat.objects.get(id=chat_id)
    history = Message.objects.filter(chat=chat).order_by("created_at")
    chat_history = [
        {"role": "user" if m.sender == "user" else "assistant", "content": m.message}
        for m in history
    ]

    contents = Content.objects.all().values("title", "body", "reference_url", "image_url")
    df = pd.DataFrame.from_records(contents)

    if df.empty:
        return JsonResponse({
            "cards_html": "",
            "has_recommendation": False
        })

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(df["body"])
    chat_text = "\n".join([m["content"] for m in chat_history if m["role"] in ["user", "assistant"]])

    if not chat_text.strip():
        return JsonResponse({
            "cards_html": "",
            "has_recommendation": False
        })

    user_vector = vectorizer.transform([chat_text])
    cosine_scores = cosine_similarity(user_vector, tfidf_matrix).flatten()
    top_indices = cosine_scores.argsort()[-3:][::-1]
    top_contents = df.iloc[top_indices]

    html = '''
    <div style="padding: 10px 16px;">
    <p style="font-weight:600; margin: 0 0 12px 0; font-size:15px;">
    🐾 반려견의 마음을 이해하는 데 도움 되는 이야기들이에요:
    </p>
    <div style="display:flex; flex-direction:column; gap:12px;">
    '''
    for item in top_contents.to_dict(orient="records"):
        html += f'''
        <a href="{item['reference_url']}" target="_blank" style="text-decoration:none; color:inherit;">
        <div style="border:1px solid #eee; border-radius:10px; padding:12px 16px; background:#fff; box-shadow:0 1px 3px rgba(0,0,0,0.05);">
            <p style="font-size:14px; font-weight:600; margin:0 0 4px;">{item['title']}</p>
            <p style="font-size:13px; color:#555; margin:0; line-height:1.4;">{item['body'][:80]}...</p>
        </div>
        </a>
        '''
    html += '</div></div>'

    Message.objects.create(
        chat=chat,
        sender="bot",
        message=html,
        created_at=timezone.now()
    )

    return JsonResponse({
        "cards_html": html,
        "has_recommendation": True
    })