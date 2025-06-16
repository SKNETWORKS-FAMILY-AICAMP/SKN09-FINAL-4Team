import os
import tempfile
import img2pdf
import time
import base64
import mimetypes
import requests

from urllib.parse import unquote
from django.template.loader import render_to_string
from django.conf import settings
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def generate_pdf_from_context(context, pdf_filename="report.pdf"):
    try:
        html_str = render_to_string("chat/report_template.html", context)
        html_str = html_str.replace(
            "/static/css/", f"file://{os.path.join(settings.BASE_DIR, 'static/css/')}"
        )
        html_str = html_str.replace(
            "/static/images/", f"file://{os.path.join(settings.BASE_DIR, 'static/images/')}"
        )

        with tempfile.NamedTemporaryFile(suffix='.html', delete=False, mode='w', encoding='utf-8') as tmp_html:
            tmp_html.write(html_str)
            html_path = tmp_html.name
        print(f"📄 HTML 파일 저장 완료: {html_path}")

        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp_img:
            image_path = tmp_img.name

        pdf_fd, pdf_path = tempfile.mkstemp(suffix='.pdf')
        os.close(pdf_fd)

        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=794,1123")


        service = Service(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get("file://" + html_path)
        print(f"🌐 PDF 렌더링 시작: file://{html_path}")
        time.sleep(2)
        driver.save_screenshot(image_path)
        driver.quit()

        if os.path.exists(image_path):
            print(f"📸 스크린샷 저장 완료 - 크기: {os.path.getsize(image_path)} bytes")

        with open(pdf_path, "wb") as f:
            f.write(img2pdf.convert(image_path))
        print(f"✅ PDF 생성 완료: {pdf_path}")

        os.remove(html_path)
        os.remove(image_path)

        return pdf_path

    except Exception as e:
        print(f"❌ PDF 생성 중 예외 발생: {str(e)}")
        raise


def get_base64_image(image_path):
    decoded_path = unquote(image_path)

    if decoded_path.startswith("http"):
        try:
            print(f"🌐 S3 이미지 요청 시작: {decoded_path}")
            response = requests.get(decoded_path, timeout=5)

            if response.status_code == 200:
                mime_type = response.headers.get("Content-Type", "image/jpeg")
                base64_str = base64.b64encode(response.content).decode("utf-8")
                print("✅ S3 이미지 인코딩 성공")
                return base64_str, mime_type
            else:
                print(f"❌ S3 이미지 요청 실패 - 응답 코드: {response.status_code}")
                return None, None

        except Exception as e:
            print(f"❌ S3 이미지 요청 예외 발생: {str(e)}")
            return None, None

    full_path = os.path.join(settings.MEDIA_ROOT, decoded_path)

    if not os.path.exists(full_path):
        print(f"❌ [오류] 로컬 이미지 파일 존재하지 않음: {full_path}")
        return None, None

    try:
        with open(full_path, "rb") as img_file:
            encoded = base64.b64encode(img_file.read()).decode("utf-8")
            mime_type, _ = mimetypes.guess_type(full_path)
            print("✅ 로컬 이미지 인코딩 성공")
            return encoded, mime_type or "image/jpeg"

    except Exception as e:
        print(f"❌ 로컬 이미지 인코딩 실패: {str(e)}")
        return None, None
