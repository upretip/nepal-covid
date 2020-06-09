import logging
import subprocess
from datetime import datetime
import base64

import requests

from creds import *
from main import make_covid_graph

logging.basicConfig(filename='nepal-covid.log', 
                    level=logging.INFO,
                    format='%(asctime)s-%(name)s - %(levelname)s - %(message)s', 
                    datefmt='%d-%b-%y %H:%M:%S')

# media post modified from https://iq.opengenus.org/post-image-twitter-api/

today = str(datetime.now().date())
make_covid_graph() # saves the covid graph in output dir
logging.info('Chart Created')
# create headers to pass on our web post request
# need oauth1.0 key api + token
bearer_keys = base64.b64encode(f'{api_key}:{api_secret}'.encode('ascii'))
bearer_keys = bearer_keys.decode('ascii')
response = requests.post(
    "https://api.twitter.com/oauth2/token",
    headers={'Authorization': bearer_keys,
             'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'},
    data={"grant_type": "client_credentials"})
print(response.status_code)
bearer_token = response.json()['access_token']

headers = {'Authorization': f'Bearer {bearer_token}'} # bearer token created already

upload_api = 'https://upload.twitter.com/1.1/media/upload.json'
tweet_api = 'https://api.twitter.com/1.1/statuses/update.json'

# post the media to twitter backend and get the media id
with open(f'output/{today}.png', 'rb') as image:
    upload_data ={'media': image.read(),
                 'media_category':'tweet_image'}
logging.info('Chart binary payload created')

try:
    # api returns media_id by default
    media_id = requests.post(upload_api, headers=headers, data=upload_data)
    logging.info(f'status code  {media_id.status_code}')
    logging.info(f'Media posting ... got media_id={media_id}')

    # can assign metadata to the media (but probably not necessary)
    if media_id.status_code == 200:
        try:
            # create the tweet
            tweet = {'status':f'Nepal Covid graph for {today}. Source code on github',
                    'media_ids': media_id,
                    'attachment_url': 'https://github.com/upretip/nepal-covid'}
            logging.info(f'Tweet payload created {tweet}')

            post_tweet = requests.post(tweet_api, headers=headers, params=tweet)
            logging.info(f'Posting tweet ... HTTP response {post_tweet.status_code}')
            logging.info(f'Tweet_id {post_tweet["id"]}')
        except Exception as e:
            logging.error(f'{e}')
except Exception as e:
    logging.error(f'{e}')

