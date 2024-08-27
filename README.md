suda 2024级计算机科学与技术学院选宿舍的脚本

针对`选座位`的小程序进行抓包处理

其域名为：api.jingjia6.com

总共涉及两个接口

- /zuo/read
- /zuo/selected

对应的header参数说明：

```json
headers = {
    'Refer': 'https://servicewechat.com/wxee63c38f3aa6f658/70/page-frame.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/11177',
    'appid': 'wxee63c38f3aa6f658',
    'token': 'g61+iYeXo4G5jqiQsIikcgx?=',
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Host': 'api.jingjia6.com',
    'Connection': 'keep-alive',
}
```

- appid为小程序的标识符，不变
- token为自己的token，请抓包时自行替换为自己的

----

while-musical.py中的逻辑为在未到达指定时间内循环等待，到达后延迟0.12防止对方服务器判定为未在指定时间内选座位导致的频繁操作；到达指定时间抢座位

read.py是对座位表信息的读取，并未做其他开发研究

