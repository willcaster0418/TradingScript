class Order:
    def __init__(self):
        return None

class OrderEvent:
    def __init__(self):
        return None

class Balance:
    def __init__(self):
        return None

class Account:
    def __init__(self):
        return None

from flask import request
class OrderManager:
    def __init__(self):
        self.gid = 0

        self.orders = {}
        self.order_events = {}
        self.balances = {}
        self.accounts = {}
        
        return None

    def execute(self):
        print(request.method)
        print(request.data)
        #import pdb;pdb.set_trace()
        self.gid += 1
        return f"execute : {self.gid}"

    def query(self, info):
        return None

    def confirm(self, order):
        return None

    def synchronize(self, order):
        return None

if __name__ == "__main__":
    from flask import Flask
    app = Flask(__name__)
    oms = OrderManager()

    app.route('/{}'.format(oms.execute.__name__), methods=['POST'])(oms.execute)

    app.run(host="localhost", port=5000, debug=True)