from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests
from requests.api import head

app = Flask(__name__)
@app.route('/', methods = ["GET","POST"])

def index():
#Scraping Algorithm

    url = "https://www.businesstoday.in/technology/news"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")

    outerdata = soup.find_all("div", class_ = "widget-listing", limit = 10)
    headlines = ""
    for data in outerdata:
        news = data.div.div.a["title"]
        headlines += "\u2022 " + news + "\n"
    
    return render_template("index.html", News = headlines)

#Scraping Algo End