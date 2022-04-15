from bs4 import BeautifulSoup
import requests
import cfscrape
import re


emoji_list={'0':'0️⃣','1':'1️⃣','2':'2️⃣','3':'3️⃣','4':'4️⃣','5':'5️⃣','6':'6️⃣','7':'7️⃣','8':'8️⃣','9':'9️⃣',',':''}

emoji_list={0:'0️⃣',1:'1️⃣',2:'2️⃣',3:'3️⃣',4:'4️⃣',5:'5️⃣',6:'6️⃣',7:'7️⃣',8:'8️⃣',9:'9️⃣'}


def diagnosed_people(url):
  headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36", #使用者代理
"Referer": "https://www.google.com/"  #參照位址
} 

  proxie = { 'http' : 'http://211.72.89.27:80'}


  scraper = cfscrape.create_scraper()

  response = scraper.get(f"{url}" ,headers=headers,proxies=proxie)
 
# HTML原始碼解析
  soup = BeautifulSoup(response.text, "html.parser")

#  total_people = str(soup.find_all("div", class_="num _big _red")).strip('[<div class="num _big _red</div>]')
  total_people=str(soup.find("h1",class_='country_recovered mb-1 text-info').text).strip('+')
  
  total_people1=''
  for h in range(len(total_people)):
  
    total_people1+=emoji_list[total_people[h]]
    
  


  local0 = soup.find_all("span", class_="country_confirmed_percent")
  local=str(local0[1]).strip(' <span class="country_confirmed_percent"><small>/本土病例 ')

  imported=str(int(total_people.replace(',',''))-int(local))
  

  dead=str(soup.find("span", class_="country_deaths_change").text).strip('+')

  
  update_time=str(soup.find("span", style="font-size: 0.8em; color: #333333; font-weight: 500;").text).replace('Updatedon','')


  LID_list = soup.find_all("div", class_="num _small")
  print(response.text)
  update_time=str(soup.find("div", class_="sub")).strip('[<div class="num _big _red</div>]')  
  local=str(LID_list[0]).strip('[<div class="num _big _red</div>]')
  imported=str(LID_list[1]).strip('[<div class="num _big _red</div>]')
  dead=str(LID_list[2]).strip('[<divclass="num _big _red</div>]')

  local1=''
  imported1=''
  dead1=''
  for i in range(len(local)):
    local1+=emoji_list[local[i]]
    
  for j in range(len(imported)):
    imported1+=emoji_list[imported[j]] 

  for k in range(len(dead)):
    dead1+=emoji_list[dead[k]]    
    


  split_strings = update_time.split()
  print(split_strings)
  split_strings.remove('Updated')
  split_strings.remove('on')
  split_strings.remove('UTC')
  split_strings.remove('+8')
  final_string = ' '.join(split_strings)

  msg=str('\n確診人數：'+total_people1+'人\n本土病例：'+local1+'人\n境外移入：'+imported1+'人\n死亡人數：'+dead1+'人\n'+'更新時間：'+final_string+' UTC+8')
  
  return msg
  


