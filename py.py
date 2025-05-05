from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import threading
import websocket
import json

app = Flask(__name__)
socketio = SocketIO(app)

def start_ws():
    def on_message(ws, message):
        data = json.loads(message)
        price = data['p']
        socketio.emit('btc_price', {'price': price})

    def on_error(ws, error):
        print("Ошибка:", error)

    def on_close(ws):
        print("Соединение закрыто")

    def on_open(ws):
        print("Соединение WebSocket открыто")

    ws = websocket.WebSocketApp("wss://stream.binance.com:9443/ws/btcusdt@trade",
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.run_forever()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    threading.Thread(target=start_ws).start()
    socketio.run(app, debug=True)
