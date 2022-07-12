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

class OrderManager:
    def __init__(self):
        self.orders = {}
        self.order_events = {}
        self.balances = {}
        self.accounts = {}
        return None

    def execute(self, order):
        return "execute"

    def query(self, info):
        return None

    def confirm(self, order):
        return None

    def synchronize(self, order):
        return None

from flask import Flask
app = Flask(__name__)
oms = OrderManager()

@app.route('/execute')
def execute():
    global oms
    return oms.execute(None)

app.run(host="localhost", port=5000, debug=True)