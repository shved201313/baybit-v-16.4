from flask import Flask, request, jsonify
import hmac
import hashlib
import os
import requests

app = Flask(__name__)

BYBIT_API_KEY = os.getenv("BYBIT_API_KEY", "your_api_key")
BYBIT_API_SECRET = os.getenv("BYBIT_API_SECRET", "your_api_secret")

@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    print("Получен сигнал:", data)

    side = data.get("side", "").upper()
    symbol = data.get("symbol", "BTCUSDT")
    quantity = data.get("quantity", "0.01")

    if side in ["BUY", "SELL"]:
        place_order(symbol, side, quantity)
        return jsonify({"status": "order sent"})
    else:
        return jsonify({"error": "invalid side"}), 400

def place_order(symbol, side, qty):
    print(f"Заказ: {side} {qty} {symbol}")
    # Здесь будет отправка на Bybit

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)