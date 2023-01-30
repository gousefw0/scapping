from flask import Flask,jsonify,request
import json
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--disable-blink-features=AutomationControlled')
app = Flask(__name__)
###########################
from markupsafe import escape
@app.route("/stock/<stock>")
def home(stock):
    stkName = stock
    url = 'https://www.tradingview.com/symbols/EGX-' + stkName + '/'
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "lxml")
    driver.quit()
    my_stock_data = {}
    # stkPrice = soup.find('div',{'class' : 'tv-symbol-price-quote__value'}).text
    my_stock_data['stock_price'] = soup.find('div',{'class' : 'tv-symbol-price-quote__value'}).text
    # incRate = soup.find('span',{'class' : 'js-symbol-change tv-symbol-price-quote__change-value'}).text
    my_stock_data['inc_rate'] = soup.find('span',{'class' : 'js-symbol-change tv-symbol-price-quote__change-value'}).text
    # incpercentage = soup.find('span',{'class' : 'js-symbol-change-pt tv-symbol-price-quote__change-value'}).text
    my_stock_data['inc_percentage'] = soup.find('span',{'class' : 'js-symbol-change-pt tv-symbol-price-quote__change-value'}).text
    # nextEarning = soup.find('div',{'class' : 'js-symbol-next-earning'}).text
    my_stock_data['next_earning'] = soup.find('div',{'class' : 'js-symbol-next-earning'}).text
    # earningPerShare = soup.find('div',{'class' : 'js-symbol-eps'}).text
    my_stock_data['earning-per_share'] = soup.find('div',{'class' : 'js-symbol-eps'}).text
    # marketValue = soup.find('div',{'class' : 'js-symbol-market-cap'}).text
    my_stock_data['market_value'] = soup.find('div',{'class' : 'js-symbol-market-cap'}).text
    # stkEarning = soup.find('div',{'class' : 'js-symbol-dividends'}).text
    my_stock_data['stock_earning'] = soup.find('div',{'class' : 'js-symbol-dividends'}).text
    # priceToEarning = soup.find('div',{'class' : 'js-symbol-pe'}).text
    my_stock_data['price_to_earning'] = soup.find('div',{'class' : 'js-symbol-pe'}).text
    return jsonify(my_stock_data)
@app.route("/")
def home():
    data = {'page':'home page','message':'ok'}
    return jsonify(data)

###########################
app.run()
