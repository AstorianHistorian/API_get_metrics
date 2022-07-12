from datetime import datetime
from pickle import TRUE
import pytz
import time
import requests  

s1 = 'http://maria.ru'
s2 = 'http://rose.ru'
s3 = 'http://sina.ru'



slist = [s1,s2,s3]

def checker():
    for s in slist:
        now = datetime.now(pytz.timezone('Europe/Moscow'))
        current_time=now.strftime("%Y-%M-%d %H:%M:%S")
        response =requests.get(s + 'api/count', params={'query': 'count'}) 
        results = response.json()['data']['result']
        for result in results:
            print('{current_time} {s}: {value}'.format(**result))

while True:
    checker()
    time.sleep(60)