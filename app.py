from flask import Flask,jsonify,request
import json
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
        url = 'https://english.mubasher.info/markets/EGX/stocks/' + stock + '/'
        result = requests.get(url)
        src = result.content
        soup = BeautifulSoup(src,'lxml')
        my_stock_data = {}
        price=soup.find('div',{'class' : 'market-summary__last-price'}).text
        my_stock_data["price"]=price
        if price=="0.00" :
                price=soup.find_all('div',{'class' : 'market-summary__block-row'})
                price=price[1].find('span',{'class':"market-summary__block-number"}).text
                my_stock_data["price"]=price
        
        url='https://www.mubasher.info/markets/EGX/stocks/'+stock+'/profile'
        result = requests.get(url)
        src = result.content
        soup = BeautifulSoup(src,'lxml')
        data =soup.find_all('span',{'class' : 'company-profile__general-information__text2'})
        logo=soup.find('div',{'class' : 'company-profile__general-information__logo'})
        logo=logo.find('img')['src']
        about=data[1].text
        txt=data[0].text
        i=txt.find('(')
        name=txt[:i-1]
        ramz=txt[i+1:-1]
        my_stock_data['name']=name
        my_stock_data['ramz']=ramz
        my_stock_data['about']=about
        my_stock_data['logo']=logo
        url='https://www.mubasher.info/markets/EGX/stocks/'+stock+'/news'
        result = requests.get(url)
        src = result.content
        soup = BeautifulSoup(src,'lxml')
        data =soup.find_all('div',{'class' : 'mi-article-media-block__content'})
        news={}
        l=[]
        for x in data :
                 l.append({'title':x.find('a',{'class':'mi-article-media-block__title'}).text
                          ,'des':x.find('div',{'class':'mi-hide-for-small mi-article-media-block__text'}).text
                          ,'date':x.find('span',{'class':'mi-article-media-block__date'}).text
                          ,'link':'https://www.mubasher.info'+x.find('a',{'class':'mi-article-media-block__title'})['href']
                         })
            
        my_stock_data['news']=l
        return jsonify(my_stock_data)
@app.route("/")
def home():
    data = {'page':'home page','message':'ok'}
    return jsonify(data)
###########################
app.run(debug=False,host='0.0.0.0')
