#!/usr/bin/env bash
set -e

# 1) DB 준비 대기 (wait-for-it, nc 등)
until nc -z $DB_HOST $DB_PORT; do
  echo "Waiting for database..."
  sleep 2
done

# 1.5) 데이터베이스 자동 생성
mysql -h "$DB_HOST" -P "$DB_PORT" \
  -u "$DB_USER" -p"$DB_PASSWORD" \
  -e "CREATE DATABASE IF NOT EXISTS \`$DB_NAME\` \
  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"


# 2) 마이그레이션
python manage.py migrate --noinput

# 3) 정적 파일 수집
python manage.py collectstatic --noinput

# --- Nginx 시작
nginx

# 4) 애플리케이션 실행
exec "$@"