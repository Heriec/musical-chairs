import http.client
import json

conn = http.client.HTTPSConnection("api.jingjia6.com")
payload = json.dumps({
   "id": "34933"
})
headers = {
   'Refer': 'https://servicewechat.com/wxee63c38f3aa6f658/70/page-frame.html',
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/11177',
   'appid': 'wxee63c38f3aa6f658',
   'token': 'g61+iYeXo4G5jqiQsIikcg==',
   'Content-Type': 'application/json',
   'Accept': '*/*',
   'Host': 'api.jingjia6.com',
   'Connection': 'keep-alive',
}
conn.request("POST", "/zuo/read", payload, headers)
res = conn.getresponse()
data = res.read()

info = json.loads(data.decode("utf-8"))
print(json.dumps(info, indent=2))