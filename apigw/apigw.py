# -*- coding: utf-8 -*- 
from flask import Flask, make_response, request  # 서버 구현을 위한 Flask 객체 import
from flask_restx import Api, Resource  # Api 구현을 위한 Api 객체 import
import json
from request_naver import *
from request_daum import *
import threading

app = Flask(__name__)  # Flask 객체 선언, 파라미터로 어플리케이션 패키지의 이름을 넣어줌.
api = Api(app)  # Flask 객체에 Api 객체 등록
krx_snap = {}

def _loop(krx_snap):
    pagenum = get_last_page()
    while True:
        for num in range(1, pagenum+1):
            krx_snap.update(get_last_market_data(page=num, market_data_agg_dict = krx_snap))
        krx_snap = get_article(snap = krx_snap)
        time.sleep(10)

@api.route('/request_mkt')
class RequestMkt(Resource):
    def get(self):  # GET 요청시 리턴 값에 해당 하는 dict를 JSON 형태로 반환
        try:
            resp = make_response(json.dumps(krx_snap[request.values['code']], ensure_ascii=False))
            resp.headers['Content-Type'] = 'application/json; charset=utf-8'
            return resp
        except Exception as e:
            print(str(e))
            resp = make_response("{}")
            resp.headers['Content-Type'] = 'application/json; charset=utf-8'
            return resp
    def post(self):
        return "POST"

if __name__ == "__main__":
    t = threading.Thread(target=_loop, args=(krx_snap, ))
    t.start()

    app.run(debug=True, host='0.0.0.0', port=3000)