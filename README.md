![Python application](https://github.com/upretip/nepal-covid/workflows/Python%20application/badge.svg)

# nepal-covid

We get the data from from [CSSE@JHU](https://github.com/CSSEGISandData/COVID-19) and use pandas and matplotlib to get the data for Nepal and plot the line graph for cumulative `reported`, `recovered` and `death` numbers. Then the plot is tweeted using `Twitter` api keys.

The tweet looks like this:

<blockquote class="twitter-tweet">
  <p lang="en" dir="ltr">
    Nepal Covid graph for 2020-05-20. Source code on 
    <a href="https://t.co/3ABqx0JfAB">https://t.co/3ABqx0JfAB</a> 
    <a href="https://t.co/JJRH13Opto">pic.twitter.com/JJRH13Opto</a></p>&mdash; PUPreti (@parashupreti) 
  <a href="https://twitter.com/parashupreti/status/1263326633340985344?ref_src=twsrc%5Etfw">May 21, 2020</a>
</blockquote> 

To reuse this code, you can clone this project then at the main direcetory of this project create a `creds.py` file. Sign up for developer account with twitter at https://developer.twitter.com/en/apps and add the `api key`, `api key secret`, `access token` and `access token secret`, need to make sure that the app has `read and write` access.

Here are the steps:

```
$> git clone git@github.com:upretip/nepal-covid
$> cd nepal-covid
$> python3 -m venv venv  # for windows python -m venv venv
$> source venv/bin/activate # for windows venv/source/activate
$> touch creds.py # below for how creds.py loos like
$> pip3 install -r requirements.txt 
$> python tweet_tweepy.py

```

`creds.py`  
```
api_key = 'xxxxxxxxxxx' 
api_secret = 'xxxxxxxxxxxxxxxxxxx'
access_token = 'zzzzzzzzzzzzzzzzz'
access_secret = 'zzzzzzzzzzzzzzzzzzzzzzz'

```

Pull Requests are welcome.
