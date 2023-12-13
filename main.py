import random
from time import localtime
from requests import get, post
from datetime import datetime, date
from zhdate import ZhDate
import sys
import os
import requests
 
 
#def get_color():
#    colorArr = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
#    color = ""
#    for i in range(6):
#        color += colorArr[random.randint(0,14)]
#    return "\"#"+color+"\""

def get_color():
    # 获取随机颜色
    get_colors = lambda n: list(map(lambda i: "#" + "%06x" % random.randint(0, 0xFFFFFF), range(n)))
    color_list = get_colors(100)
    return random.choice(color_list)
 
 
def get_access_token():
    # appId
    app_id = config["app_id"]
    # appSecret
    app_secret = config["app_secret"]
    post_url = ("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}"
                .format(app_id, app_secret))
    try:
        access_token = get(post_url).json()['access_token']
    except KeyError:
        print("获取access_token失败，请检查app_id和app_secret是否正确")
        os.system("pause")
        sys.exit(1)
    # print(access_token)
    return access_token
 
 
def get_weather(region):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    key = config["weather_key"]
    region_url = "https://geoapi.qweather.com/v2/city/lookup?location={}&key={}".format(region, key)
    response = get(region_url, headers=headers).json()
    print(response)

    # 获取地区的location--id
    try:
        location_id = response['location'][0]["id"]
    except:
        if(region == "上海"):
            location_id = 101020100
        if(region == "杨浦区"):
            location_id = 101021700
        if(region == "长宁区"):
            location_id = 101021300
        if(region == "北京")
            location_id = 101010100
        if(region == "朝阳区"):
            location_id = 101010300
    
    
    weather_url = "https://devapi.qweather.com/v7/weather/3d?location={}&key={}".format(location_id, key)
    try:
        response = get(weather_url, headers=headers).json()
        # 天气
    except:
        weather = '唔姆，刮强风把系统吹走啦~'
        WindDir = '岂可休！'
        temp = '可恶...温度计也没有留下！'
        TempNew = '那今天就麻烦宝宝自己看下天气咯...'
    else:
        weather = '清晨'+response['daily'][0]["textDay"]+'，'+'傍晚'+response['daily'][0]["textDay"]
        # 当前温度
        temp = response['daily'][0]["tempMin"]+ u"\N{DEGREE SIGN}" + "C"+'~'+response['daily'][0]["tempMax"]+ u"\N{DEGREE SIGN}" + "C"
        if int(response['daily'][0]["tempMin"]) <= 18:
            TempNew = "天气变凉啦，多穿点衣服哦~"
        elif int(response['daily'][0]["tempMax"]) >= 35:
            TempNew = "温度有点高！要多补充补充水分~！"
        elif int(response['daily'][0]["tempMax"]) >= 25:
            TempNew = "天气有点热哦，注意防晒~"
        else:
            TempNew = "天气还不错呢！这不出来散步散步~"
        # 风向
        WindDir = response['daily'][0]["windDirDay"]
    finally:
        return weather, temp, WindDir, TempNew
 
def get_birthday(birthday, year, today):
    birthday_year = birthday.split("-")[0]
    # 判断是否为农历生日
    if birthday_year[0] == "r":
        r_mouth = int(birthday.split("-")[1])
        r_day = int(birthday.split("-")[2])
        # 获取农历生日的今年对应的月和日
        try:
            birthday = ZhDate(year, r_mouth, r_day).to_datetime().date()
        except TypeError:
            print("请检查生日的日子是否在今年存在")
            os.system("pause")
            sys.exit(1)
        birthday_month = birthday.month
        birthday_day = birthday.day
        # 今年生日
        year_date = date(year, birthday_month, birthday_day)
 
    else:
        # 获取国历生日的今年对应月和日
        birthday_month = int(birthday.split("-")[1])
        birthday_day = int(birthday.split("-")[2])
        # 今年生日
        year_date = date(year, birthday_month, birthday_day)
    # 计算生日年份，如果还没过，按当年减，如果过了需要+1
    if today > year_date:
        if birthday_year[0] == "r":
            # 获取农历明年生日的月和日
            r_last_birthday = ZhDate((year + 1), r_mouth, r_day).to_datetime().date()
            birth_date = date((year + 1), r_last_birthday.month, r_last_birthday.day)
        else:
            birth_date = date((year + 1), birthday_month, birthday_day)
        birth_day = str(birth_date.__sub__(today)).split(" ")[0]
    elif today == year_date:
        birth_day = 0
    else:
        birth_date = year_date
        birth_day = str(birth_date.__sub__(today)).split(" ")[0]
    return birth_day
 
 
def get_ciba():
    url = "http://open.iciba.com/dsapi/"
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    r = get(url, headers=headers)
    NoteEN_0 = r.json()["content"]
    NoteCH_0 = r.json()["note"]
    return NoteCH_0, NoteEN_0
 
 
def send_message(to_user, access_token, region_1, weather_1, temp_1, TempNew_1, WindDir_1, region_2, weather_2, temp_2, TempNew_2, WindDir_2, NoteCH_0, NoteCH_1, NoteCH_2, NoteEN_0, NoteEN_1, NoteEN_2):
    url = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={}".format(access_token)
    week_list = ["周日", "周一", "周二", "周三", "周四", "周五", "周六"]
    year = localtime().tm_year
    month = localtime().tm_mon
    day = localtime().tm_mday
    today = datetime.date(datetime(year=year, month=month, day=day))
    week = week_list[today.isoweekday() % 7]
    # 获取在一起的日子的日期格式
    love_year = int(config["love_date"].split("-")[0])
    love_month = int(config["love_date"].split("-")[1])
    LoveDay = int(config["love_date"].split("-")[2])
    love_date = date(love_year, love_month, LoveDay)
    # 获取在一起的日期差
    LoveDays = str(int(str(today.__sub__(love_date)).split(" ")[0]))
    # 获取所有生日数据
    birthdays = {}
    for k, v in config.items():
        if k[0:5] == "birth":
            birthdays[k] = v
    data = {
        "touser": to_user,
        "template_id": config["template_id"],
        "url": "",
        "topcolor": "#FF0000",
        "data": {
            "NowDate": {
                "value": "{} {}".format(today, week),
            },
            "NowRegion_1": {
                "value": region_1,
            },
            "NowWeather_1": {
                "value": weather_1,
            },
            "NowTemp_1": {
                "value": temp_1,
            },
            "WindDir_1": {
                "value": WindDir_1,
            },
            "NowRegion_2": {
                "value": region_2,
            },
            "NowWeather_2": {
                "value": weather_2,
            },
            "NowTemp_2": {
                "value": temp_2,
            },
            "WindDir_2": {
                "value": WindDir_2,
            },
            "LoveDay": {
                "value": LoveDays,
            },
            "NoteEN_0": {
                "value": NoteEN_0,
            },
            "NoteCH_0": {
                "value": NoteCH_0,
            },
            "NoteEN_1": {
                "value": NoteEN_1,
            },
            "NoteCH_1": {
                "value": NoteCH_1,
            },
            "NoteEN_2": {
                "value": NoteEN_2,
            },
            "NoteCH_2": {
                "value": NoteCH_2,
            },
            "TempNew_1":{
                "value": TempNew_1,
            },
            "TempNew_2":{
                "value": TempNew_2,
            }
        }
    }
    for key, value in birthdays.items():
        # 获取距离下次生日的时间
        birth_day = get_birthday(value["birthday"], year, today)
        if birth_day == 0:
            birthday_data = "今天是{}生日！祝{}生日快乐！".format(value["name"], value["name"])
        else:
            birthday_data = "距离{}生日还有{}天呢！".format(value["name"], birth_day)
        # 将生日数据插入data
        data["data"][key] = {"value": birthday_data}
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    response = post(url, headers=headers, json=data).json()
    if response["errcode"] == 40037:
        print("推送消息失败，请检查模板id是否正确")
    elif response["errcode"] == 40036:
        print("推送消息失败，请检查模板id是否为空")
    elif response["errcode"] == 40003:
        print("推送消息失败，请检查微信号是否正确")
    elif response["errcode"] == 0:
        print("推送消息成功")
        print(data)
    else:
        print(data)
 
 
if __name__ == "__main__":
    try:
        with open("config.txt", encoding="utf-8") as f:
            config = eval(f.read())
    except FileNotFoundError:
        print("推送消息失败，请检查config.txt文件是否与程序位于同一路径")
        os.system("pause")
        sys.exit(1)
    except SyntaxError:
        print("推送消息失败，请检查配置文件格式是否正确")
        os.system("pause")
        sys.exit(1)
 
    # 获取accessToken
    accessToken = get_access_token()
    # 接收的用户
    users = config["user"]
    # 传入地区获取天气信息
    region_1 = config["region_1"]
    weather_1, temp_1, WindDir_1,TempNew_1 = get_weather(region_1)
    #地区1
    region_2 = config["region_2"]
    weather_2, temp_2, WindDir_2,TempNew_2 = get_weather(region_2)
    #地区2
    NoteCH_0 = config["note_ch"]
    NoteEN_0 = config["note_en"]
    NoteCH_1 = ""
    NoteEN_1 = ""
    NoteCH_2 = ""
    NoteEN_2 = ""
    if NoteCH_0 == "" and NoteEN_0 == "":
        # 获取词霸每日金句
        NoteCH_0, NoteEN_0 = get_ciba()
    if NoteCH_0 != "" and NoteEN_0 != "":
        #当有词霸金句有内容时
        #判断中文
        if len(NoteCH_0) > 30 :
            NoteCH_2 = NoteCH_0[30:45]
            NoteCH_1 = NoteCH_0[15:30]
            NoteCH_0 = NoteCH_0[0:15]
        elif len(NoteCH_0) > 15 :
            NoteCH_2 = ""
            NoteCH_1 = NoteCH_0[15:30]
            NoteCH_0 = NoteCH_0[0:15]
        #判断英文
        Notewords = NoteEN_0.split()
        if len(Notewords) > 30:
            for i in range(0,15):
                NoteEN_0 = NoteEN_0 + Notewords[i] + " "
            for i in range(15,30):
                NoteEN_1 = NoteEN_1 + Notewords[i] + " "
            for i in range(30,len(Notewords)):
                NoteEN_1 = NoteEN_1 + Notewords[i] + " "
        elif len(Notewords) > 15:
            for i in range(0,15):
                NoteEN_0 = NoteEN_0 + Notewords[i] + " "
            for i in range(15,len(Notewords)):
                NoteEN_1 = NoteEN_1 + Notewords[i] + " "
    # 公众号推送消息
    for user in users:
        send_message(user, accessToken, region_1, weather_1, temp_1, TempNew_1, WindDir_1, region_2, weather_2, temp_2, TempNew_2, WindDir_2, NoteCH_0, NoteCH_1, NoteCH_2, NoteEN_0, NoteEN_1, NoteEN_2)
    os.system("pause")
