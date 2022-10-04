from flask import Flask
from selenium import webdriver
app = Flask(__name__)


def t():
    # chromedriver位置 C:/chromedriver/chromedriver.exe
    
    user_id = "B103022043"
    user_pw = "raymond8130314"
    login = "https://cu.nsysu.edu.tw/mooc/login.php"
    index = "https://cu.nsysu.edu.tw/learn/index.php"
    calender = "https://cu.nsysu.edu.tw/learn/calender_alert.php"
    
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome('chromedriver',options=options)
    #driver.implicitly_wait(10)


    driver.get(login)

    #return driver.title
    return "ok"


@app.route('/')
def hello_world():
    return t()
    #'Hello, World!'

if __name__ == "__main__":
    app.run()

