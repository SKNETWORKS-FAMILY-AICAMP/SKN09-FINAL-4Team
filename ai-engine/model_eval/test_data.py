# test_data.py
# 반려견 프로필 및 질문 목록 정의

# 반려견 프로필 데이터
DOG_PROFILES = [
    {
        "dog_name": "코코",
        "dog_breed": "말티즈",
        "dog_age": 3,
        "dog_gender": "여아",
        "dog_neutered": "중성화 완료",
        "dog_disease": "없음",
        "dog_disease_detail": "",
        "dog_period": "② 1년 이상~3년 미만",
        "dog_housing": "아파트"
    },
    {
        "dog_name": "보리",
        "dog_breed": "푸들",
        "dog_age": 2,
        "dog_gender": "남아",
        "dog_neutered": "중성화 미완료",
        "dog_disease": "없음",
        "dog_disease_detail": "",
        "dog_period": "① 1년 미만",
        "dog_housing": "아파트"
    },
    {
        "dog_name": "초코",
        "dog_breed": "시바견",
        "dog_age": 5,
        "dog_gender": "여아",
        "dog_neutered": "중성화 완료",
        "dog_disease": "있음",
        "dog_disease_detail": "알레르기 피부염 (2023)",
        "dog_period": "③ 3년 이상~10년 미만",
        "dog_housing": "단독주택"
    },
    {
        "dog_name": "몽이",
        "dog_breed": "비숑",
        "dog_age": 1,
        "dog_gender": "남아",
        "dog_neutered": "중성화 완료",
        "dog_disease": "없음",
        "dog_disease_detail": "",
        "dog_period": "① 1년 미만",
        "dog_housing": "아파트"
    },
    {
        "dog_name": "루루",
        "dog_breed": "포메라니안",
        "dog_age": 4,
        "dog_gender": "여아",
        "dog_neutered": "중성화 미완료",
        "dog_disease": "있음",
        "dog_disease_detail": "슬개골 탈구 수술 (2021)",
        "dog_period": "③ 3년 이상~10년 미만",
        "dog_housing": "빌라/다세대"
    },
    {
        "dog_name": "탄이",
        "dog_breed": "웰시코기",
        "dog_age": 6,
        "dog_gender": "남아",
        "dog_neutered": "중성화 완료",
        "dog_disease": "없음",
        "dog_disease_detail": "",
        "dog_period": "③ 3년 이상~10년 미만",
        "dog_housing": "단독주택"
    },
    {
        "dog_name": "하니",
        "dog_breed": "골든리트리버",
        "dog_age": 3,
        "dog_gender": "여아",
        "dog_neutered": "중성화 완료",
        "dog_disease": "없음",
        "dog_disease_detail": "",
        "dog_period": "② 1년 이상~3년 미만",
        "dog_housing": "단독주택"
    },
    {
        "dog_name": "댕댕이",
        "dog_breed": "시츄",
        "dog_age": 2,
        "dog_gender": "남아",
        "dog_neutered": "중성화 완료",
        "dog_disease": "있음",
        "dog_disease_detail": "기관지염 치료 (2024)",
        "dog_period": "② 1년 이상~3년 미만",
        "dog_housing": "아파트"
    },
    {
        "dog_name": "별이",
        "dog_breed": "진돗개",
        "dog_age": 7,
        "dog_gender": "여아",
        "dog_neutered": "중성화 완료",
        "dog_disease": "없음",
        "dog_disease_detail": "",
        "dog_period": "③ 3년 이상~10년 미만",
        "dog_housing": "단독주택"
    },
    {
        "dog_name": "쫑이",
        "dog_breed": "닥스훈트",
        "dog_age": 10,
        "dog_gender": "남아",
        "dog_neutered": "중성화 완료",
        "dog_disease": "없음",
        "dog_disease_detail": "",
        "dog_period": "③ 3년 이상~10년 미만",
        "dog_housing": "빌라/다세대"
    }
]

# 질문 목록
QUESTIONS = [ 
    '산책 나가면 갑자기 한 방향으로만 끌고 가려 해요. 이유가 뭘까요?', 
    '요즘 자꾸 자기 엉덩이 주변을 핥아요. 혹시 항문샘 문제일까요?',
    '낯선 사람을 보면 너무 짖고 흥분해요. 어떻게 해야 하나요?', 
    '혼자 두면 짖고 물건을 망가뜨려요. 분리불안일까요?',
    '밖에서 다른 강아지들만 보면 공격적으로 굴어요. 왜 그런 걸까요?',
    '산책 도중 자꾸 땅을 파요. 무슨 의미일까요?', 
    '요즘 문만 열면 밖으로 도망가려고 해요. 왜 그럴까요? 스트레스 때문일까요?', 
    '평소엔 얌전한데, 갑자기 소파 밑에 숨어서 안 나오려고 해요.', 
    '요즘 자꾸 귀를 긁고 머리를 흔들어요. 귀에 문제가 있는 걸까요?',
    '코가 평소보다 말라 있고, 따뜻해요. 열이 있는 건가요?', 
    '요즘 발바닥을 자꾸 핥아요. 발에 이상 있는 걸까요?',
    '왼쪽 눈만 자꾸 깜빡여요. 결막염 같은 걸까요?', 
    '배변을 자주 해요. 하루에 5번은 넘는 것 같은데 정상일까요?', 
    '갑자기 피부에 붉은 반점이 생겼어요. 알레르기일까요?',
    '몸을 자꾸 긁고 털이 빠져요. 피부병일 가능성도 있나요?', 
    '밥을 잘 안 먹고 사료를 입에 넣었다 뱉어요. 입 안에 문제 있는 걸까요?', 
    '밤마다 짖고 깨서 잠을 잘 못 자요. 불면증 같은 게 있는 건가요?', 
    '식사 후 구토를 자주 해요. 위장이 약한 걸까요?', 
    '물을 거의 안 마셔요. 탈수 걱정해도 될까요?',
    '밥을 잘 안 먹어요. 입맛이 없는 걸까요? 편식일까요?',
    '잠자는 시간이 너무 많아졌어요. 왜 그럴까요?', 
    '앉아, 기다려 같은 기본 훈련을 잘 안들어요.', 
    '하네스를 차려고 하면 도망가요. 외출이 싫은 걸까요?', 
    '차를 타면 자꾸 구토해요. 어떻게 훈련하면 좋을까요?', 
    '목줄만 보면 도망가요. 산책을 싫어하는 걸까요?', 
    '산책 중에 자꾸 바닥에 있는 걸 주워 먹어요. 위험하지 않을까요?', 
    '계단 오르내릴 때 다리를 절어요. 관절 문제일 수 있나요?', 
    '다른 강아지와 놀다가 갑자기 낑낑거려요. 왜 그런건가요?', 
    '발을 만지려고 하면 극도로 싫어하고 물려고 해요. 왜 그런가요?', 
    '가족 중 특정한 사람만 따라다니고, 다른 사람은 피해요. 이유가 뭘까요?', 
    ]

# 상황 질문
SCENARIO= [
  {
    "persona": "30대 직장인. 반려견 키우는 건 처음이라 모든 게 낯설고 조심스러움. 인터넷도 많이 찾아보지만 더 확실한 조언을 듣고 싶어함. 말투는 다소 조심스럽고 공손한 편.",
    "dog_profile": {
      "dog_name": "초코",
      "dog_breed": "푸들",
      "dog_age": 2,
      "dog_gender": "남아",
      "dog_neutered": "미중성화",
      "dog_disease": "없음",
      "dog_disease_detail": "",
      "dog_period": "① 6개월 이상~1년 미만",
      "dog_housing": "아파트"
    },
    "problem": "산책할 때 한 방향으로만 끌고 가려고 하는 문제를 겪고 있음."
  },
  {
    "persona": "50대 주부. 반려견 경험은 오래되었고 관찰력이 좋은 편. 건강 이상에는 민감하게 반응함. 말투는 차분하고 담백하며, 경험을 근거로 질문함.",
    "dog_profile": {
      "dog_name": "바니",
      "dog_breed": "말티즈",
      "dog_age": 3,
      "dog_gender": "여아",
      "dog_neutered": "중성화 완료",
      "dog_disease": "없음",
      "dog_disease_detail": "",
      "dog_period": "② 1년 이상~3년 미만",
      "dog_housing": "아파트"
    },
    "problem": "강아지가 엉덩이 주변을 자주 핥는 행동 문제를 겪고 있음."
  },
  {
    "persona": "20대 대학생. 평소 성격은 급하고 직접적인 스타일. 짖는 행동이 민폐가 될까 봐 스트레스를 받음. 말투는 솔직하고 직설적이며, 해결책 중심의 질문을 많이 함.",
    "dog_profile": {
      "dog_name": "별이",
      "dog_breed": "진돗개",
      "dog_age": 7,
      "dog_gender": "여아",
      "dog_neutered": "중성화 완료",
      "dog_disease": "없음",
      "dog_disease_detail": "",
      "dog_period": "③ 3년 이상~10년 미만",
      "dog_housing": "단독주택"
    },
    "problem": "강아지가 낯선 사람을 볼 때 너무 짖고 흥분하는 문제를 겪고 있음."
  },
  {
    "persona": "40대 프리랜서. 반려견과의 교감에 관심이 많고, 훈련보다는 심리적 안정에 초점을 맞춤. 말투는 부드럽고 이해심 많음.",
    "dog_profile": {
      "dog_name": "코코",
      "dog_breed": "비글",
      "dog_age": 4,
      "dog_gender": "남아",
      "dog_neutered": "미중성화",
      "dog_disease": "알레르기",
      "dog_disease_detail": "식품 알레르기",
      "dog_period": "② 1년 이상~3년 미만",
      "dog_housing": "빌라"
    },
    "problem": "분리 불안으로 혼자 있을 때 짖거나 파괴 행동을 보임."
  },
  {
    "persona": "30대 주부. 집에서 주로 돌보고, 반려견과 산책을 자주 함. 반려견 교육에 관심이 많고 적극적으로 문제를 해결하려 함.",
    "dog_profile": {
      "dog_name": "몽이",
      "dog_breed": "시추",
      "dog_age": 5,
      "dog_gender": "남아",
      "dog_neutered": "중성화 완료",
      "dog_disease": "없음",
      "dog_disease_detail": "",
      "dog_period": "③ 3년 이상~10년 미만",
      "dog_housing": "아파트"
    },
    "problem": "낯선 사람이나 다른 강아지에게 공격적인 태도를 보임."
  },
  {
    "persona": "40대 직장인. 반려견과 함께 운동하는 것을 좋아하며, 체력 관리를 중요시함. 문제 행동 발생 시 즉각적이고 명확한 훈련법을 원함.",
    "dog_profile": {
      "dog_name": "루키",
      "dog_breed": "골든 리트리버",
      "dog_age": 2,
      "dog_gender": "남아",
      "dog_neutered": "중성화 완료",
      "dog_disease": "없음",
      "dog_disease_detail": "",
      "dog_period": "① 6개월 이상~1년 미만",
      "dog_housing": "단독주택"
    },
    "problem": "산책 중 지나가는 자전거나 오토바이에 지나치게 반응함."
  },
  {
    "persona": "50대 은퇴자. 반려견과 오랜 시간을 보내며 경험이 많음. 천천히 문제를 풀어나가길 원하며 조언을 신중히 듣는 스타일.",
    "dog_profile": {
      "dog_name": "해피",
      "dog_breed": "요크셔 테리어",
      "dog_age": 6,
      "dog_gender": "여아",
      "dog_neutered": "중성화 완료",
      "dog_disease": "없음",
      "dog_disease_detail": "",
      "dog_period": "③ 3년 이상~10년 미만",
      "dog_housing": "아파트"
    },
    "problem": "낯선 환경에 적응하지 못하고 불안해함."
  },
  {
    "persona": "30대 싱글. 반려견과의 교감을 중요시하며, 자연주의적 접근을 선호함. 말투는 부드럽고 긍정적임.",
    "dog_profile": {
      "dog_name": "초롱",
      "dog_breed": "푸들",
      "dog_age": 3,
      "dog_gender": "여아",
      "dog_neutered": "중성화 완료",
      "dog_disease": "없음",
      "dog_disease_detail": "",
      "dog_period": "② 1년 이상~3년 미만",
      "dog_housing": "빌라"
    },
    "problem": "집 안에서 배변을 가리지 못함."
  },
  {
    "persona": "20대 대학생. 바쁜 일정 속에서도 반려견과 시간을 보내려 노력함. 솔직하고 직설적인 질문을 선호함.",
    "dog_profile": {
      "dog_name": "구름",
      "dog_breed": "믹스견",
      "dog_age": 1,
      "dog_gender": "남아",
      "dog_neutered": "미중성화",
      "dog_disease": "없음",
      "dog_disease_detail": "",
      "dog_period": "① 6개월 이상~1년 미만",
      "dog_housing": "아파트"
    },
    "problem": "낯선 장소에서 지나치게 긴장하고 두려워함."
  },
  {
    "persona": "40대 주부. 반려견과의 의사소통에 관심이 많으며, 문제 행동을 개선하기 위해 꾸준히 노력함.",
    "dog_profile": {
      "dog_name": "달콩",
      "dog_breed": "포메라니안",
      "dog_age": 4,
      "dog_gender": "여아",
      "dog_neutered": "중성화 완료",
      "dog_disease": "없음",
      "dog_disease_detail": "",
      "dog_period": "② 1년 이상~3년 미만",
      "dog_housing": "아파트"
    },
    "problem": "혼자 있을 때 울거나 짖는 분리 불안 증상을 보임."
  }
]

#############
# 전처리 코드\
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


df0 = pd.DataFrame(QUESTIONS, columns=['question'])
df0.index.name = 'Index'


def remove_similar_entries(df, content_col='question', threshold=0.90, preview=True):
    """
    TF-IDF 기반 유사 항목 제거 함수
    - title과 content를 합쳐 유사도 계산
    - 유사도가 threshold 이상인 항목은 제거
    - 중복 후보 미리보기도 가능
    """
    df = df.reset_index(drop=True).copy()
    
    # TF-IDF 벡터화
    vectorizer = TfidfVectorizer().fit_transform(df[content_col])
    similarity_matrix = cosine_similarity(vectorizer)

    to_drop = set()
    duplicate_pairs = []

    for i in range(similarity_matrix.shape[0]):
        for j in range(i + 1, similarity_matrix.shape[0]):
            sim = similarity_matrix[i, j]
            if sim > threshold:
                to_drop.add(j)
                duplicate_pairs.append((i, j, sim))

    if preview:
        print("🟡 유사도가 높은 항목 쌍:")
        for i, j, sim in duplicate_pairs:
            print(f"\n🔹 [{i}] 질문: {df.loc[i]}")
            print(f"🔹 [{j}] 질문: {df.loc[j]}")
            print(f"   ↪ 유사도: {sim:.4f}")

    # 중복 제거
    df_cleaned = df.drop(list(to_drop)).reset_index(drop=True)

    return df_cleaned

# 전처리 실행
# df1 = remove_similar_entries(df0)