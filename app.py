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

line_msg=diagnosed_people('https://covid-19.nchc.org.tw/dt_005-covidTable_taiwan.php')

if __name__ == "__main__":
  total_people=line_msg[0]
  token = 'M8OZJMmL5p6BSOiBJZMt6f9gH4seLahLBF7GEIzXWvW'
  message = str(line_msg)  
  lineNotifyMessage(token, message)