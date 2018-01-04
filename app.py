from flask import Flask
from flask import render_template
from flask import request
import requests
import urllib
import json
import sys
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def idx():
    if request.method == 'GET':
        return render_template('landing.html')
    elif request.method == 'POST':
        url = 'https://www.googleapis.com/urlshortener/v1/url'
        #payload = {'longUrl': 'http://www.google.com/'}
        myUrl = request.form['myUrl']
        print('URL is: ' + myUrl, file=sys.stderr)
        payload = {'longUrl': str(myUrl)}
        headers = {'content-type': 'application/json',}
        r = requests.post(url + '?key=AIzaSyComkfwDtEEUV65whc-zn5ElqrlplFIgEc', data=json.dumps(payload), headers=headers)
        if r.status_code == requests.codes.ok:
            minifiedUrl = r.json()
            #return minifiedUrl['id']
            return render_template('landing.html', minifiedUrl = minifiedUrl['id'])
        else:
            return render_template('landing.html', error = 'Bad URL.')
        #return idx()

    else:
        return r.status_code


'''
@app.route('/', methods=['GET','POST'])
def perform_scrape(myUrl):
    if request.method == 'GET':
        return hello_world()
    elif request.method == 'POST':
        url = 'https://www.googleapis.com/urlshortener/v1/url'
        payload = {'longUrl': 'http://www.google.com/'}
        headers = {'content-type': 'application/json',}

        r = requests.post(url + '?key=AIzaSyComkfwDtEEUV65whc-zn5ElqrlplFIgEc', data=json.dumps(payload), headers=headers)
        if r.status_code == requests.codes.ok:
            minifiedUrl = r.json()
            return minifiedUrl['id']
        
    return r.status_code
'''