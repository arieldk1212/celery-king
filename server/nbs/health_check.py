from time import sleep
from selenium import webdriver
from selenium.webdriver import ChromeOptions

BRAVE_PATH = "/opt/brave.com/brave/brave"

options = ChromeOptions()
options.binary_location = BRAVE_PATH

HEALTH_URL = "https://www.amazon.com/Ghost-Tsushima-Directors-Cut-PlayStation-4/dp/B098TV2ZS3/ref=sr_1_1?sr=8-1"

with webdriver.Chrome(options=options) as driver:
  driver.get(HEALTH_URL)
  sleep(5)