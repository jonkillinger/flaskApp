from flask import Flask
from flask import render_template
from flask import request
import requests
import urllib
import json
app = Flask(__name__)

#Thank BeautifulSoup!

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        return perform_scrape(request.form['inputURL'])
    else:
        return render_template('landing.html')

@app.route('/', methods=['POST'])
def perform_scrape(myUrl):
    #test = urllib.parse.urlparse(myUrl, scheme='https')
    #if(test.)

    url = 'https://www.googleapis.com/urlshortener/v1/url'
    payload = {'longUrl': 'http://www.google.com/'}
    headers = {'content-type': 'application/json',}

    r = requests.post(url + '?key=AIzaSyComkfwDtEEUV65whc-zn5ElqrlplFIgEc', data=json.dumps(payload), headers=headers)
    if r.status_code == requests.codes.ok:
        minifiedUrl = r.json()
        return minifiedUrl['id']
    
    return r.status_code