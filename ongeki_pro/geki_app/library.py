from django.shortcuts import render
from bs4 import BeautifulSoup
import requests, re


def get_weather(URL):
    # 気象庁URL
    #url = 'https://www.jma.go.jp/bosai/forecast/'
    # エンドポイント
    #area_type = 'offices'
    # 東京
    #area_code = '130000'
    # endpoint = '329.html'
    

    
    res = requests.get(URL)
    res.encoding = res.apparent_encoding
    soup = BeautifulSoup(res.text, "html.parser")
    containers = soup.find(class_='forecastCity')
    images = containers.findAll('img')
    img_today = images[0]['src']
    img_tomorrow = images[1]['src']
    
    # 成形する
    containers = [i.strip() for i in containers.text.splitlines()]
    containers = [i for i in containers if i != '']
    
    
    today = []
    tomorrow = []
    
    for i in range(len(containers)):
        if i < 18:
            today.append(containers[i])
        else:
            tomorrow.append(containers[i])
    context = {
        'today': today,
        'tomorrow': tomorrow,
        'img_today': img_today,
        'img_tomorrow': img_tomorrow,
    }
 
    return context