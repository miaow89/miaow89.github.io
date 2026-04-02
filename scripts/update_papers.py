import requests
from bs4 import BeautifulSoup
import json
import re
import os
from datetime import datetime

# 설정
SCHOLAR_ID = "C5-jvk8AAAAJ"
SCHOLAR_URL = f"https://scholar.google.com/citations?user={SCHOLAR_ID}&hl=ko&view_op=list_works&sortby=pubdate"
DATA_FILE = "papers/data.js"

def fetch_google_scholar_papers():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    print(f"Fetching papers from: {SCHOLAR_URL}")
    response = requests.get(SCHOLAR_URL, headers=headers)
    
    if response.status_code != 200:
        print(f"Error fetching page: {response.status_code}")
        return []
        
    soup = BeautifulSoup(response.text, "html.parser")
    papers = []
    
    for row in soup.select(".gsc_a_tr"):
        title_tag = row.select_one(".gsc_a_at")
        title = title_tag.text.strip()
        link = "https://scholar.google.com" + title_tag["href"]
        
        meta = row.select(".gs_gray")
        authors = meta[0].text.strip()
        venue_info = meta[1].text.strip()
        
        year_tag = row.select_one(".gsc_a_y")
        year = year_tag.text.strip()
        
        # venue와 year 분리 로직 (가끔 venue에 연도가 없을 수 있음)
        venue = venue_info
        
        paper = {
            "title": title,
            "authors": authors,
            "venue": venue,
            "year": int(year) if year.isdigit() else 0,
            "links": {
                "url": link
            }
        }
        papers.append(paper)
        
    return papers

def load_existing_data():
    if not os.path.exists(DATA_FILE):
        return {"yourName": "Damsub Lim", "papers": []}
        
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        content = f.read()
        # JS 파일에서 JSON 부분만 추출
        match = re.search(r"(?:window\.)?papersData\s*=\s*({.*});", content, re.DOTALL)
        if not match:
            print("Failed to find papersData object. Returning empty template.")
            return {"yourName": "Damsub Lim", "papers": []}
        json_str = match.group(1)
        # Trailing commas 제거 (JSON 호환성 위함)
        json_str = re.sub(r",\s*([\]}])", r"\1", json_str)
        try:
            return json.loads(json_str)
        except json.JSONDecodeError:
            print("Failed to parse existing JS file. Returning empty template.")
            return {"yourName": "Damsub Lim", "papers": []}

def is_korean(text):
    # 한글 문자가 포함되어 있는지 확인
    return bool(re.search("[가-ih]", text))

def merge_papers(existing_data, new_papers):
    existing_papers = existing_data.get("papers", [])
    existing_titles = {p["title"].lower(): p for p in existing_papers}
    
    updates_count = 0
    adds_count = 0
    
    merged_list = []
    
    # 새로운 논문 처리
    for new_p in new_papers:
        title_key = new_p["title"].lower()
        
        if title_key in existing_titles:
            # 이미 존재하는 논문: 기존 메타데이터(isSCI, category 등) 유지하고 최신 정보로 업데이트할 게 있으면 수행
            # 여기서는 기존 데이터를 그대로 유지하되, 링크나 연도 등이 바뀌었을 수 있으므로...
            # 하지만 사용자가 수동으로 수정한 태그(isSCI 등)를 날리면 안됨.
            # 기존 데이터를 우선 사용하되, 정보가 비어있다면 업데이트
            existing_p = existing_titles[title_key]
            merged_list.append(existing_p)
        else:
            # 새로운 논문 발견!
            print(f"New paper found: {new_p['title']}")
            
            # 카테고리 자동 추론
            if is_korean(new_p["venue"]) or is_korean(new_p["title"]):
                new_p["category"] = "domestic"
                # 국내 논문이면 KSCI일 확률이 높지만 확신할 순 없음. 일단 false
                new_p["isKSCI"] = False 
            else:
                new_p["category"] = "international"
                # 해외 논문이면 SCI일 확률이 높지만 확신할 순 없음.
                new_p["isSCI"] = False
            
            new_p["id"] = f"auto-{datetime.now().strftime('%Y%m%d')}-{adds_count}"
            merged_list.append(new_p)
            adds_count += 1
            
    # 기존에 있었지만 스크래핑 목록에 없는 논문(삭제됐거나 누락된 것)은?
    # 안전을 위해 유지하는 것이 좋음. (수동으로 추가한 논문일 수 있음)
    scraped_titles = {p["title"].lower() for p in new_papers}
    for old_p in existing_papers:
        if old_p["title"].lower() not in scraped_titles:
            merged_list.append(old_p)
            
    # 정렬: 연도 내림차순
    merged_list.sort(key=lambda x: x.get("year", 0), reverse=True)
    
    existing_data["papers"] = merged_list
    return existing_data, adds_count

def save_js_data(data):
    # index.html이 그대로 읽을 수 있도록 window.papersData 형식으로 저장
    json_str = json.dumps(data, indent=2, ensure_ascii=False)
    js_content = f"// This file is automatically loaded by index.html to avoid CORS issues with local file fetching\nwindow.papersData = {json_str};\n"
    
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        f.write(js_content)

def main():
    print("Starting Scholar Update Process...")
    new_papers = fetch_google_scholar_papers()
    if not new_papers:
        print("No papers found or error occurred.")
        return

    existing_data = load_existing_data()
    updated_data, new_count = merge_papers(existing_data, new_papers)
    
    if new_count > 0:
        print(f"Adding {new_count} new papers...")
        save_js_data(updated_data)
        print("Update complete.")
        # GitHub Actions를 위한 output 설정 (변경사항 있음)
        with open(os.environ.get('GITHUB_OUTPUT', 'output.txt'), 'a') as f:
            f.write("updated=true\n")
    else:
        print("No new papers to add.")
        with open(os.environ.get('GITHUB_OUTPUT', 'output.txt'), 'a') as f:
            f.write("updated=false\n")

if __name__ == "__main__":
    main()
