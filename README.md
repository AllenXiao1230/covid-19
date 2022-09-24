# 讓Line Notify來告訴你今天的確診人數
* 使用Python爬蟲，並推播到Line Notify

Hi,今天來分享我寫的小程式，他可以取得每天的確診人數，並且推播的個人或群組，聽起來很方便吧！跟著我，帶著你一步步設定😎

### 下面是我們的步驟
1. 建立一個Line Notify
2. 建立一個Heroku App
3. 取得我為你撰寫的程式碼
4. 修改程式碼裡的參數
5. Push到Heroku的伺服器
6. [設定定時觸發程序](https://github.com/AllenXiao1230/covid-19/blob/main/README.md#6-%E8%A8%AD%E5%AE%9A%E5%AE%9A%E6%99%82%E8%A7%B8%E7%99%BC%E7%A8%8B%E5%BA%8F)

### 1. 建立一個Line Notify
### 2. 建立一個Heroku App
### 3. 取得我為你撰寫的程式碼
### 4. 修改程式碼裡的參數
### 5. Push到Heroku的伺服器
### <p id =“6”>6. 設定定時觸發程序</p>

### App.py
```python=
from covid import *
import requests

def lineNotifyMessage(token, msg):

headers = {
    "Authorization": "Bearer " + token, 
    "Content-Type" : "application/x-www-form-urlencoded"
}

payload = {'message': msg }
r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
return r.status_code



if __name__ == "__main__":
    line_msg=diagnosed_people('https://covid-19.nchc.org.tw/dt_005-covidTable_taiwan.php')        #呼叫函式，取得當日疫情資料
    token_e9 = 'M8OZJMmL5p6BSOiBJZMt6f9gH4seLahLBF7GEIzXWvW'      #定義Line Notify的token
    token_me = 'UINKkQgYr1tpwBT3W9Klw1kmZZO8xG8GTXQ1jyETPxn'      #定義Line Notify的token

lineNotifyMessage(token_e9, line_msg)       #發送Line Notify
lineNotifyMessage(token_me, line_msg)       #發送Line Notify
```
___
