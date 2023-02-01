from flask import Flask,jsonify,request
import json
from bs4 import BeautifulSoup
from time import sleep
import requests
app = Flask(__name__)
from markupsafe import escape
###########################
@app.route("/")
def home():
        url = 'https://english.mubasher.info/markets/EGX/stocks/' + 'abuk' + '/'
        result = requests.get(url)
        src = result.content
        soup = BeautifulSoup(src,'lxml')
        my_stock_data = {}
        my_stock_data['stock_price'] =soup.find('div',{'class' : 'market-summary__last-price down-icon-only'}).text
        return jsonify(my_stock_data)
###########################
app.run(debug=False,host='0.0.0.0')
