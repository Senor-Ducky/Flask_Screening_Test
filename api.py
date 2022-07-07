from flask import Flask, request, jsonify
from scraper import news_feed

app = Flask(__name__)

@app.route('/get_news', methods=['GET'])
def get_news():
    ticker = request.args.get('ticker')
    news = news_feed(ticker)
    return jsonify(news)


app.run(debug=True)