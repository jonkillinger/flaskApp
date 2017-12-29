from flask import Flask
from flask import render_template
from flask import request
#from bs4 import BeautifulSoup
import bz2
import requests
import re
import urllib
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
    page = requests.get(myUrl)
    comp = bz2.compress(page.content)

    '''
    source = urllib.request.urlopen(myUrl).read().decode('utf-16')
    links = []
    for link in re.findall(r'(?:http\:|https\:)?\/\/.*\.(?:png|jpg)', source):
        links.append(link)
    '''

    '''
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, 'html.parser')
        links = []
        for link in soup.find_all('link'):
            links.append(link.get('href'))

        scripts = []
        for script in soup.find_all('script'):
            scripts.append(script.get('src'))
        '''
        #imgs = []
        #for img in soup.findAll('img', attrs={'src': re.compile(r'(?:http\:|https\:)?\/\/.*\.(?:png|jpg)', source)}):
            #imgs.append(img.get('src'))
        #for img in soup.find_all('img',re.compile("https")):
            #imgs.append(img.get('src', ))



    return str(comp)
    #else:
        #return "Unable to obtain content. (Bad URL?)"