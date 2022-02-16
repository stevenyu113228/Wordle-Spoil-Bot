import requests
import configparser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime

config = configparser.ConfigParser()
config.read("/app/config.ini")
token = config["Telegram"]["token"]
chatid = config["Telegram"]["chatid"]

options = Options() 
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')

driver = webdriver.Chrome(options=options)
driver.get("https://www.nytimes.com/games/wordle/index.html")
res = driver.execute_script("return (new wordle.bundle.GameApp()).solution")
r = 'Today answer is : ' + res.upper()

requests.post(f"https://api.telegram.org/bot{token}/sendMessage",
data = {
    "chat_id" : chatid,
    "text" : r
})
