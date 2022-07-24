import time
import pandas as pd
from urllib.parse import urlparse
from urllib.parse import parse_qs
from bs4 import BeautifulSoup
import requests, json, lxml, re
from selenium import webdriver
from selenium.webdriver.common.by import By

params = {
    "q": 'Offroad Pickup Cargo Truck3 D‏',
    "gl": 'tn',
    "c": 'apps'
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.79 Safari/537.36",
}
chtml = requests.get("https://play.google.com/store/search", params=params, headers=headers)
soup = BeautifulSoup(chtml.text, "html.parser")

# browser = webdriver.Chrome('webdriver/chromedriver.exe')
# browser.get(chtml.url)
try:
    s_html = requests.get(f'https://play.google.com{soup.select_one(".Qfxief")["href"]}')
    m_soup = BeautifulSoup(s_html.content, "html.parser")
    print(m_soup.select_one('.Fd93Bb').findChild('span').text)
except:
    s_html = requests.get(f'https://play.google.com{soup.select_one(".Si6A0c.Gy4nib")["href"]}')
    m_soup = BeautifulSoup(s_html.content, "html.parser")
    print(m_soup.select_one('.Fd93Bb').findChild('span').text)

# parsed_url = urlparse(browser.current_url)
# app_id = parse_qs(parsed_url.query)['id'][0]
# company = None
# rating = None
# browser.quit()