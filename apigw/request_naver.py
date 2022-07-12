import requests, re, time
from bs4 import BeautifulSoup as bs

def get_last_page(url = "https://finance.naver.com/sise/sise_market_sum.naver?&", sosok=0):
    headers = {"Content-Type" : "application/json", "Connect" : "Close"}
    html = requests.get(url + f"sosok={sosok}", headers = headers)
    html_soup = bs(html.text, "html.parser")
    data = html_soup.select("td > a")
    return int(data[-1]['href'][-2:])
    
def get_last_market_data(url = "https://finance.naver.com/sise/sise_market_sum.naver?", sosok=0, page = 1, market_data_agg_dict = {}):
    headers = {"Content-Type" : "application/json", "Connect" : "Close"}
    html = requests.get(url + f"sosok={sosok}&page={page}", headers = headers)
    html_soup = bs(html.text, "html.parser")
    datas = html_soup.select("table[class='type_2'] > thead > tr > th")
    data_keys = [data.text for data in datas]
    datas = html_soup.select("table[class='type_2'] > tbody > tr")
    for data in datas:
        if "href" in str(data):
            tmpsoup = bs(str(data), "html.parser")
            data_dict = {}
            idx = 0
            for tmpdata in tmpsoup.find_all("td"):
                try:
                    if tmpdata.has_attr("class"):
                        if tmpdata['class'][0] == "no":
                            data_dict[data_keys[idx]] = int(tmpdata.text)
                        elif tmpdata['class'][0] == "number":
                            data_dict[data_keys[idx]] = float(tmpdata.text.replace(",", "").replace("\n", "").replace("%",""))
                    if not data_keys[idx] in data_dict.keys():
                        data_dict[data_keys[idx]] = tmpdata.text
                        if data_keys[idx] == "종목명":
                            data_dict['code'] = tmpdata.select("a")[0]['href'].replace("/item/main.naver?code=", "")
                except Exception as e:
                    if data_keys[idx] == "종목명":
                        data_dict['code'] = None
                    data_dict[data_keys[idx]] = None
                    pass
                idx += 1
            if data_dict['code'] != None:
                data_dict['time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if data_dict['code'] in market_data_agg_dict.keys():
                    market_data_agg_dict[data_dict['code']].update(data_dict)
                else:
                    market_data_agg_dict[data_dict['code']] = data_dict
    return market_data_agg_dict