
from bs4 import BeautifulSoup
import requests
import cfscrape
import re

emoji_list={'0':'0️⃣','1':'1️⃣','2':'2️⃣','3':'3️⃣','4':'4️⃣','5':'5️⃣','6':'6️⃣','7':'7️⃣','8':'8️⃣','9':'9️⃣',',':''}   #emoji對照表

def diagnosed_people(url):
  headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36", #使用者代理
"Referer": "https://www.google.com/"  #參照位址
} 

  scraper = cfscrape.create_scraper()   #初始化cfscrape

  response = scraper.get(f"{url}" ,headers=headers)   #從傳入的網址取得HTML
 

  soup = BeautifulSoup(response.text, "html.parser")    #將HTML轉為BeautifulSoup的格式

  total_people=str(soup.find("h1",class_='country_recovered mb-1 text-info').text).strip('+')   #取得當日總確診人數
  
  local0 = soup.find_all("span", class_="country_confirmed_percent")                        #    ㇕
  local=str(local0[1]).strip(' <span class="country_confirmed_percent"><small>/本土病例 ')   #    ㇘-->取得當日本土病例人數

  imported=str(int(total_people.replace(',',''))-int(local))    #取得當日境外移入人數
  
  dead=str(soup.find("span", class_="country_deaths_change").text).strip('+')   #取得當日死亡人數

  
  update_time=str(soup.find("span", style="font-size: 0.8em; color: #333333; font-weight: 500;").text).replace('Updatedon','')    #取得更新時間

  total_people1=''#   ㇕
  local1=''       #    |
  imported1=''    #    |-->定義「將數字轉為emoji」的字串
  dead1=''        #   ㇘

  for h in range(len(total_people)):            #   ㇕
    total_people1+=emoji_list[total_people[h]]  #    |
                                                #    |
  for i in range(len(local)):                   #    |
    local1+=emoji_list[local[i]]                #    |
                                                #    |-->將數字轉為emoji
  for j in range(len(imported)):                #    |
    imported1+=emoji_list[imported[j]]          #    |
                                                #    |
  for k in range(len(dead)):                    #    |
    dead1+=emoji_list[dead[k]]                  #   ㇘
    


  split_strings = update_time.split()     #   ㇕
  split_strings.remove('Updated')         #    |
  split_strings.remove('on')              #    |
  split_strings.remove('UTC')             #    |-->處理「更新時間」的字串
  split_strings.remove('+8')              #    |
  final_string = ' '.join(split_strings)  #   ㇘

  msg=str('\n確診人數：'+total_people1+'人\n本土病例：'+local1+'人\n境外移入：'+imported1+'人\n死亡人數：'+dead1+'人\n'+'更新時間：'+final_string+' UTC+8')   #定義回傳格式
  
  return msg    #回傳資料
  
