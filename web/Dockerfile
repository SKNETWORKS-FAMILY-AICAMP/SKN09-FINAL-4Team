FROM python:3.12-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# 1) 시스템 의존성 설치 (chromium + 한글 폰트 + google-chrome 링크 생성)
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    libssl-dev \
    netcat \
    default-mysql-client \
    nginx \
    curl \
    unzip \
    gnupg \
    fonts-nanum \
    fonts-noto-color-emoji \                           
    fonts-liberation \
    libappindicator3-1 \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libdbus-1-3 \
    libgdk-pixbuf2.0-0 \
    libnspr4 \
    libnss3 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    xdg-utils \
    chromium \
 && ln -s /usr/bin/chromium /usr/bin/google-chrome \
 && rm -rf /var/lib/apt/lists/*

# 2) requirements.txt 설치 (webdriver-manager 포함되어야 함)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 3) 애플리케이션 코드 복사
COPY . .

# 4) collectstatic으로 STATIC_ROOT에 모으기
RUN python manage.py collectstatic --noinput

# 5) Nginx 설정 복사
COPY nginx/default.conf /etc/nginx/conf.d/default.conf
RUN rm -f /etc/nginx/sites-enabled/default

# 6) 엔트리포인트 스크립트 복사 및 권한 설정
COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

# 7) 컨테이너 시작 시 실행될 명령 지정
ENTRYPOINT ["entrypoint.sh"]
CMD ["gunicorn", "petmind.wsgi:application", "--config", "gunicorn.conf.py"]