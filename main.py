import requests
import os

class BlogPost:
    def __init__(self, title, description, link):
        self.title = title.replace("<b>", "").replace("</b>", "")
        self.description = description.replace("<b>", "").replace("</b>", "")
        self.link = link

    def __str__(self):
        return f"Title: {self.title}\nDescription: {self.description}\nURL: {self.link}\n"

class NaverBlogSearcher:
    def __init__(self):
        self.client_id = os.getenv("NAVER_CLIENT_ID")  # 환경변수에서 Client ID 읽어오기
        self.client_secret = os.getenv("NAVER_CLIENT_SECRET")  # 환경변수에서 Client Secret 읽어오기

        # 환경변수 값이 없을 때 예외 처리
        if not self.client_id or not self.client_secret:
            raise ValueError("NAVER_CLIENT_ID and NAVER_CLIENT_SECRET must be set as environment variables.")

    def get_blog_posts(self, query, display=10):
        # 요청 URL 및 헤더 구성
        url = f"https://openapi.naver.com/v1/search/blog.json?query={query}&display={display}&sort=date"
        headers = {
            "X-Naver-Client-Id": self.client_id,
            "X-Naver-Client-Secret": self.client_secret,
        }

        # 네이버 API에 요청 보내기
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            return self.parse_response(response.json())
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return []

    def parse_response(self, data):
        # 응답 데이터 파싱
        blogs = data.get("items", [])
        blog_posts = [BlogPost(blog.get("title"), blog.get("description"), blog.get("link")) for blog in blogs]
        return blog_posts

if __name__ == "__main__":
    # "동탄" 검색어로 최신 블로그 정보 가져오기
    try:
        searcher = NaverBlogSearcher()
        blog_posts = searcher.get_blog_posts("동탄", 3)
        for post in blog_posts:
            print(post)
    except ValueError as e:
        print(e)
