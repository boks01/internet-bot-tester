from selenium import webdriver
import time

class InternetSpeedBot:
    """making internet speed tester bot with selenium webdriver, you must have path and url example:  
    path = 'C:/bot/chromedriver.exe,
    url = 'https.www.example.com',
    Bot = InternetSpeedBot(path, url)"""
    def __init__(self, path, url):
        self.driver = webdriver.Chrome(executable_path=path)
        self.url = url
        self.download_ms = 0
        self.upload_ms = 0

    def test_internet(self):
        self.driver.get(self.url)
        time.sleep(1)
        go_button = self.driver.find_element_by_css_selector('.start-button a')
        go_button.click()
        time.sleep(60)
        download_ms_taking = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        upload_ms_taking = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        self.download_m = f"{float(download_ms_taking.text)} Mbps"
        self.upload_ms = f'{float(upload_ms_taking.text)} Mbps'
        print(self.download_m)
        print(self.upload_ms)