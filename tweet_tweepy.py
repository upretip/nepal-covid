import logging
from datetime import datetime

import tweepy

import creds
from main import make_covid_graph

logging.basicConfig(filename='nepal-covid.log', 
                    level=logging.INFO,
                    format='%(asctime)s-%(name)s - %(levelname)s - %(message)s', 
                    datefmt='%d-%b-%y %H:%M:%S')

today = datetime.now().date()

reported, reocvered, deaths = make_covid_graph()
logging.info('Chart created')

auth = tweepy.OAuthHandler(creds.api_key, creds.api_secret)
auth.set_access_token(creds.access_token, creds.access_secret)
api = tweepy.API(auth)
logging.info('API Authenticated')

tweet = f"""
    Nepal Covid graph for {today} with reporeted cases {reported}, deaths {deaths}, and recovered {reocvered}. 
    Source code on https://github.com/upretip/nepal-covid"""
image_path = f'output/{today}.png'
try:
    status = api.update_with_media(image_path, tweet)
    logging.info('Tweet sent')
except Exception as e:
     logging.error(f'{e}')
