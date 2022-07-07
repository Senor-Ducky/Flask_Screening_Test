import redis
import rq
from scraper import news_feed

r = redis.Redis('localhost',49153,password='redispw')
queue = rq.Queue(connection=r)
job = queue.enqueue(news_feed, 30)