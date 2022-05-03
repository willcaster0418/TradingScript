#--*--coding:utf-8--*--
from mw.Gandan import *
from mw.GandanPub import *
from mw.GandanSub import *
from mw.GandanMsg import *

from flask import Flask, request
import json
import requests
import datetime

app = Flask(__name__)

@app.route('/post', methods=['POST'])
def first_callback():
    try:
        if request.method == 'POST':
            post_data = request.data
            logging.info(str(post_data))
            client_ip = request.remote_addr
            post_dict = json.loads(post_data.decode().replace("\'", "\""))
            logging.info(str(post_dict))
            port = post_dict['port']
            requests.post(f"http://127.0.0.1:{port}/post", data = str(post_dict).replace("\'","\""))
    except Exception as e:
        logging.info(str(e))
        pass

    return "OK"

#@app.route('/get', methods=['GET'])
#def second_callback():
#    if request.method == 'GET':
#         #....
#         pass
#    return "OK"

if __name__ == '__main__':
    Gandan.setup_log("/root/log/%s.webhook_gateway.log" % (datetime.datetime.now().strftime("%Y%m%d")))
    app.debug = True
    app.run("0.0.0.0", 80)
