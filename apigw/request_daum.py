import requests, re, time
from bs4 import BeautifulSoup as bs
def get_article(snap = {}):
    article_dict = {}
    headers = {"User-Agent" : "Mozilla/5.0", "connect" : "close"}
    article_requests = requests.get("https://news.daum.net/", headers = headers)
    article_soup = bs(article_requests.text, "html.parser")
    article_data = article_soup.select("a[data-tiara-layer='article_main']")
    for article in article_data:
        # replace text to remove special characters and space
        article_text = article.text.replace("\n", "").replace("\t", "").replace("\xa0", "").replace("\u200b", "").replace("  ", "")
        if article_text == "":
            continue
        #print(article_text, article['href'])
        contents_requests = requests.get(article['href'], headers=headers)
        contents_soup = bs(contents_requests.text, "html.parser")
        contents_data = contents_soup.select("div[id='mArticle']")
        for contents in contents_data:
            contents_text = contents.text.replace("\n", "").replace("\t", "").replace("\xa0", "").replace("\u200b", "").replace("  ", "")
            for key in snap.keys():
                if snap[key]['종목명'] in contents_text:
                    print(key)
                    if not "article" in snap[key].keys():
                        snap[key]["article"] = []
                    if not article_text in snap[key]["article"]:
                        snap[key]["article"].append(article_text)
            time.sleep(0.1)
    return snap

if __name__ == "__main__":
    print(get_article(snap = {"005930" : {"종목명" : "삼성전자"}}))