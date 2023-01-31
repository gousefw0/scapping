from flask import Flask,jsonify,request
import json
from bs4 import BeautifulSoup
from time import sleep
import requests
app = Flask(__name__)
###########################
from markupsafe import escape
@app.route("/stock/<stock>")
def stock(stock):
        url = 'https://english.mubasher.info/markets/EGX/stocks/' + stock + '/'
        result = requests.get(url)
        src = result.content
        soup = BeautifulSoup(src,'lxml')
        my_stock_data = {}
        my_stock_data['stock_price'] =soup.find('div',{'class' : 'market-summary__last-price down-icon-only'}).text
        return jsonify(my_stock_data)
@app.route("/")
def home():
    data = {'page':'home page','message':'ok'}
    return jsonify(data)
###########################
app.run(debug=False,host='0.0.0.0')
