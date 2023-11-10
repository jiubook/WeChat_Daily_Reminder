# coding=utf-8
import requests

yburl = 'https://free-api.heweather.com/s6/weather/forecast'
cyurl = 'https://free-api.heweather.com/s6/weather/lifestyle'

value = {
    'location': '北京',
    'key': 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
    'lang': 'zh'
}

ybreq = requests.get(yburl, params=value)
cyreq = requests.get(cyurl, params=value)

ybjs = ybreq.json()
cyjs = cyreq.json()

for i in range(2):
    yb = ybjs['HeWeather6'][0]['daily_forecast']
    cy = cyjs['HeWeather6'][0]['lifestyle'][1]
    gj = cyjs['HeWeather6'][0]['lifestyle'][0]
    d1 = u'北京' + '  ' + yb[i]['date'] + ' ' + yb[i]['cond_txt_d']
    d2 = gj['txt'] + ' ' + cy['txt']
    d3 = d1 + '\n' + d2
    print(d3)