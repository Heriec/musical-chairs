import http.client
import json
import time

conn = http.client.HTTPSConnection("api.jingjia6.com")
row = 11
col = 2
payload = json.dumps({
    f"name.{row}_{col}": "何朝伟",
    "id": "34933",
    "zuo": [
        f'{row}_{col}'
    ]
})
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
target_time = int(time.mktime(time.strptime(
    "2024-08-27 12:00:00", "%Y-%m-%d %H:%M:%S")))
print(target_time)
while True:
    current_time = time.time()
    delay = target_time - current_time
    print("Delay: ", delay)
    # 0.12是防止对方服务器时间和本地时间不一致造成的延迟，可根据实际情况调整
    if delay > -0.12:
        continue
    conn.request("POST", "/zuo/selected", payload, headers)
    res = conn.getresponse()
    data = res.read()

    info = json.loads(data.decode("utf-8"))
    print(info)
    print(info['info'])
    if info['info'] == '选座失败，当前时间不允许选座位。':
        continue
    if info['status'] == 200 or info['status'] == 403:
        break
