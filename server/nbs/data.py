from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ChromeOptions

DEFAULT_URL = "https://www.amazon.com/Ghost-Tsushima-Directors-Cut-PlayStation-4/dp/B098TV2ZS3/ref=sr_1_1?sr=8-1"

def scrape(url=DEFAULT_URL):
  # BRAVE_PATH = "/opt/brave.com/brave/brave"
  options = ChromeOptions()
  # options.binary_location = BRAVE_PATH
  html = ''
  with webdriver.Chrome(options=options) as driver:
    # driver = driver.get(HEALTH_URL) # makes u see the recaptcha
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html)
    productTitle = (soup.find('span', id='productTitle')).text.strip()
    productPriceText = "".join([x for x in (soup.find_all('span', class_='a-price-whole'))[0].text.strip() if x.isdigit()])
    productPriceFloat = float(productPriceText)
  return {
    'product_title': productTitle,
    'product_price': productPriceFloat
  }