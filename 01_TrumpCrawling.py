import requests
from bs4 import BeautifulSoup
import csv

# 특정 status의 URL 형식
base_url = "https://trumpstruth.org/statuses/"

status_start = 1
status_end = 28815

# 요청 헤더 설정
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# 상태별로 데이터 추출 및 저장
batch_size = 1000
current_batch = 1
status_data = []

for status_id in range(status_start, status_end + 1):
    url = f"{base_url}{status_id}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        try:
            # 작성자 이름
            author_name = soup.select_one(".status-info__account-name").get_text(strip=True) if soup.select_one(".status-info__account-name") else "N/A"
            
            # 사용자 ID
            user_id = soup.select_one(".status-info__meta-item").get_text(strip=True) if soup.select_one(".status-info__meta-item") else "N/A"
            
            # 게시 시간
            post_time = soup.select(".status-info__meta-item")[1].get_text(strip=True) if len(soup.select(".status-info__meta-item")) > 1 else "N/A"
            
            # 게시 내용
            post_content = soup.select_one(".status__content").get_text(strip=True) if soup.select_one(".status__content") else "N/A"

            # 데이터 저장
            status_data.append({
                "status_id": status_id,
                "author_name": author_name,
                "user_id": user_id,
                "post_time": post_time,
                "post_content": post_content
            })

        except Exception as e:
            print(f"Error processing status {status_id}: {e}")
    else:
        print(f"Failed to fetch status {status_id}. Status code: {response.status_code}")

    # Batch 저장 조건 확인
    if len(status_data) >= batch_size or status_id == status_end:
        file_name = f"status_data_batch_{current_batch}.csv"
        with open(file_name, "w", encoding="utf-8", newline="") as csv_file:
            fieldnames = ["status_id", "author_name", "user_id", "post_time", "post_content"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(status_data)

        print(f"Batch {current_batch} saved to {file_name}.")
        current_batch += 1
        status_data = []  # 데이터 초기화

print("모든 데이터를 저장했습니다.")