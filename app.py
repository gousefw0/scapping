from flask import Flask,jsonify,request
import json
from json import loads, dumps
from tvDatafeed import TvDatafeed,Interval
from bs4 import BeautifulSoup
from flask_cors import CORS
from time import sleep
import requests
app = Flask(__name__)
CORS(app)
###########################
from markupsafe import escape
@app.route("/stock/<stock>")
def stock(stock):
        username = 'yousef014'
        password = 'yosef@123'
        tv = TvDatafeed(username=username,password=password)
        df=tv.get_hist(stock,'EGX',)
        result = df.to_json(orient="split")
        parsed = loads(result)
        dumps(parsed, indent=4)  
        return jsonify(parsed)
@app.route("/")
def home():
    data = {'page':'home page','message':'ok'}
    return jsonify(data)
###########################
app.run(debug=False,host='0.0.0.0')
