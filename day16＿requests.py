import requests

#发送 GET 请求，获取一句随机的话
url = "https://www.baidu.com"
try:
    #设置超过时间为 5 秒，防止网络卡死
    response = requests.get(url, timeout=5)

    #状态码 200 代表请求成功
    if response.status_code == 200:
        print("请求成功！白度服务器回应了！")
        #截取返回网页的前 50 个字符看看
        print("网页返回内容大概是：")
        print(response.text[:50])
    else:
        print(f"请求失败，服务器返回的状态码是：{response.status_code}")

except Exception as e:
    print(f"哎呀，网络好像出错了。错误信息：{e}")