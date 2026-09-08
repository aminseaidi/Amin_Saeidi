import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return '<H1>.سلام من محمد امین سعیدی هستم 15 ساله از ارومیه<H1>'


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    