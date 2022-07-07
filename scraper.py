import requests
import json
import redis
import rq


r = redis.Redis('localhost',49153,password='redispw')


def news_feed(ticker):
    header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'referer': 'https://www.nasdaq.com/market-activity/stocks/mrtn/earnings'
    }

    url = f"https://api.nasdaq.com/api/news/topic/articlebysymbol?q={ticker.lower()}|stocks&offset=0&limit=8&fallback=false"
    response = requests.get(url, headers=header)
    data = response.json()

    ticker_dict = {
            f"{ticker.upper()}": []
        }

    news_dict = {
        "news_feed": []
    }
    

    for items in data["data"]["rows"]:
        
        values = {
            "timestamp": items["ago"],
            "title": items["title"],
            "url": "https://www.nasdaq.com/"+items["url"]
        }
        
        ticker_dict[f"{ticker.upper()}"].append(values)
    
    news_dict["news_feed"].append(ticker_dict)

    r.set('news', json.dumps(news_dict))
    response = json.loads(r.get('news'))
    r.bgsave()

    return response
    
    




