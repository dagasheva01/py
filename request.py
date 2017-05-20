import requests
from bs4 import BeautifulSoup

print("What's your name?")
username = input()

print(username,",Almaty or Astana?")
cityname = input()

if cityname == "Almaty" or "Astana":
    if cityname == "Almaty":
        url = "https://www.gismeteo.kz/city/daily/5205/"
    else: 
        url = "https://www.gismeteo.kz/city/daily/5164/"
else:
    print("Invalid city")
    
r = requests.get(url)
html = r.text
soup = BeautifulSoup(html, "html.parser")
gradus = int(soup.select(dd.value m_temp c))
weathertype = soup.select(dt.png dd table tbody tr td)

print ("Погода на данный момент:%d",%gradus,",",weathertype)

if "асмурно" or "ождь" is in weathertype: """ варинаты - Дождь, дождь"""
    print("Лучше прихватите с собой зонтик,%s", %username)
if "нег" is in weathertype:
    if gradus <= -15:
        print("На улице оооочень холодно и идет снег,%s", %username,"одевайтесь как можно теплее.")
    else:
        print("на улице холодно и идет снег %s,", %username, "одевайтесь теплее")
if "олнечно" is in weathertype:
    if gradus >= 30:
        print("Не забудьте крем от загара и солнцезащитные очки! На улице очень жарко")
    else:
        print("Не забудьте солнцезащитные очки!")
        