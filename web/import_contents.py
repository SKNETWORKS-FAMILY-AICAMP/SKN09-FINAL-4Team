import csv
import os
import sys
import django

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "petmind.settings")
django.setup()

from chat.models import Content

csv_path = os.path.join(BASE_DIR, 'data',  "merged_rag_data.csv")

with open(csv_path, newline='', encoding="utf-8-sig") as csvfile: 
    reader = csv.DictReader(csvfile)
    count = 0
    for row in reader:
        title = row.get("title", "").strip()
        body = row.get("content", "").strip()
        image_url = row.get("image", "").strip() or None
        reference_url = row.get("url", "").strip() or None

        if not title or not body:
            print(f"⚠️ 누락된 필드가 있어 건너뜀: {row}")
            continue

        if not Content.objects.filter(title=title, body=body).exists():
            Content.objects.create(
                title=title,
                body=body,
                image_url=image_url,
                reference_url=reference_url
            )
            count += 1

    print(f"{count}개의 콘텐츠가 추가되었습니다.")
