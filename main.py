from selenium import webdriver
from process import InternetSpeedBot
import time
path = "your path"
driver = webdriver.Chrome(executable_path=path)
url = "https://www.speedtest.net/"

bot = InternetSpeedBot(path, url)
bot.test_internet()
