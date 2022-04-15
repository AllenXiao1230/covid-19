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
  line_msg=diagnosed_people('https://covid-19.nchc.org.tw/dt_005-covidTable_taiwan.php')
  total_people=line_msg[0]
  token_e9 = 'M8OZJMmL5p6BSOiBJZMt6f9gH4seLahLBF7GEIzXWvW'
  token_me = 'UINKkQgYr1tpwBT3W9Klw1kmZZO8xG8GTXQ1jyETPxn'
  message = str(line_msg)  
  lineNotifyMessage(token_e9, message)
  lineNotifyMessage(token_me, message)