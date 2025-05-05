from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import websocket
import json

app = Flask(__name__)
socketio = SocketIO(app)

def start_ws():
    def on_message(ws, message):
        try:
            print("Получено сообщение:", message)  
            data = json.loads(message)
            price = data.get('p')  
            if price is not None:
                socketio.emit('btc_price', {'price': price}, namespace='/')
            else:
                print("Ошибка: поле 'p' отсутствует в данных")
        except Exception as e:
            print("Ошибка обработки сообщения:", e)

    def on_error(ws, error):
        print("Ошибка WebSocket:", error)

    def on_close(ws, close_status_code, close_msg):
        print(f"Соединение закрыто: код={close_status_code}, сообщение={close_msg}")

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
    socketio.start_background_task(start_ws)
    socketio.run(app, debug=True)