# 前言
- 一 首先注意编辑文件的时候把浏览器自动翻译关了

- 二 运行失败 点开可以看报错原因 自己多试试

- 三 不要有任何空格 编辑的时候仔细一点 

- 四 输出的消息样子以模版为准 想去掉某些东西的话 最简单的方法是去改模板 


# 新版成功实例
![image](https://github.com/jiubook/Wechat_daily_reminder/blob/main/others/WechatNewSample.png?raw=true)

# 旧版成功实例
![image](https://github.com/jiubook/Wechat_daily_reminder/blob/main/others/WechatSample.png?raw=true)
- 注：现在已经没有彩色字体了，参考以下文章

- [GitHub issue: 如何修复因2023-05-04微信推送服务规范整改，导致推送服务异常？ #326](https://github.com/wangxinleo/wechat-public-account-push/issues/326)

# 图文教程
- [酷安链接: 微信公众号消息每日自动推送(纯小白保姆级教程)](https://www.coolapk.com/feed/38579891?shareKey=NGI3ZGZlZTM4MDBjNjMwMzdlM2M)

- *注意不要挂梯子访问*

- 有实在解决不了的问题

- Email: jiubook@qq.com

*本人为二次修改，原作者vx OWI7404*


### 微信测试平台
- (如果自己有公众号的，去后台→左上角三条横线→基本配置。然后就能看到了)

- http://mp.weixin.qq.com/debug/cgi-bin/sandboxinfo?action=showinfo&t=sandbox/index


### 和风天气控制台
- https://id.qweather.com/


---


# 模板内容
- (这个可以自由发挥)
- 参数前面必须加文字或者Emoji

>日期：{{NowDate.DATA}}
> 
>☁️{{NowRegion_1.DATA}}的天气：{{NowWeather_1.DATA}}
>
>🌡️{{NowRegion_1.DATA}}的气温：{{NowTemp_1.DATA}} {{WindDir_1.DATA}} 
>
>温度提示：{{TempNew_1.DATA}}
> 
>☁️{{NowRegion_2.DATA}}的天气：{{NowWeather_2.DATA}}
>
>🌡️{{NowRegion_2.DATA}}的气温：{{NowTemp_2.DATA}} {{WindDir_2.DATA}} 
>
>温度提示：{{TempNew_2.DATA}}
> 
>💞自定义文本💞 
>
>今天是我们恋爱的第{{love_day.DATA}}天 
>
>生日1：{{birthday1.DATA}} 
>
>生日2：{{birthday2.DATA}}
>
>每日金句英文：{{NoteEN_0.DATA}}{{NoteEN_1.DATA}}{{NoteEN_2.DATA}}
>
>每日金句中文：{{NoteCH_0.DATA}}{{NoteCH_1.DATA}}{{NoteCH_2.DATA}}
>

# 关于自动运行
- 目前设定的时间是：早上六点半(6:30 am)

- 记得把\.github\workflows\目录下的weixin.yml.bak

- 更名为weixin.yml

- 而后手动运行一次确认成功后即可

- *(建议设置提前十分钟 有一定的延迟)*

- 有延迟是正常的，如果延迟很大很大，可以参考这篇文章

- https://blog.csdn.net/l1937gzjlzy/article/details/117753465


# 更改时间的步骤
![image](https://github.com/jiubook/Wechat_daily_reminder/blob/main/others/ChangeTimeSample.png?raw=true)


# 天气key生成教程
![image](https://github.com/jiubook/Wechat_daily_reminder/blob/main/others/HeFengSample.png?raw=true)


# 天行数据
- 可以申请各种各样的接口用来推送

![image](https://github.com/jiubook/Wechat_daily_reminder/blob/main/others/TianXingSample1.png?raw=true)
![image](https://github.com/jiubook/Wechat_daily_reminder/blob/main/others/TianXingSample2.png?raw=true)


# 有别的建议欢迎留言
- 建议先发Issue，再发邮箱

- Email: jiubook@qq.com

*本人为二次修改，原作者vx OWI7404*