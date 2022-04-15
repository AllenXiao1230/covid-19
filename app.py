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
  token = 'oSVbmpG1KETazWdSmkkTgdpwu5QhiBDnIJNTw7sHjaS'
  message = str(line_msg)  
  lineNotifyMessage(token, message)