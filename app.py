from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/spin')
def spin():
    prizes = ["💰 100 монет", "🎁 Подарок", "🍀 Удача", "❌ Пусто", "⭐ Бонус", "🎟 Билет"]
    return random.choice(prizes)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)