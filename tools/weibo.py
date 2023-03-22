import requests
import json

# 填入您的微博账号和密码
username = "wengrui2046@sina.com"
password = "sina1991827"


# 获取登录所需的参数
def get_login_params():
    login_url = "https://passport.weibo.cn/sso/login"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
        "Referer": "https://passport.weibo.cn/signin/login?entry=mweibo&r=https://m.weibo.cn/",
    }
    data = {
        "username": username,
        "password": password,
        "savestate": "1",
        "r": "",
        "ec": "0",
        "pagerefer": "",
        "entry": "mweibo",
        "wentry": "",
        "loginfrom": "",
        "client_id": "",
        "code": "",
        "qq": "",
        "mainpageflag": "1",
        "hff": "",
        "hfp": "",
    }
    response = requests.post(login_url, headers=headers, data=data)
    login_params = json.loads(response.content.decode())["data"]
    return login_params


# 获取微博列表
def get_weibo_list(uid):
    weibo_list = []
    page = 1
    while True:
        weibo_url = f"https://m.weibo.cn/api/container/getIndex?type=uid&value={uid}&containerid=107603{uid}&page={page}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
            "Referer": "https://m.weibo.cn/",
            "X-Requested-With": "XMLHttpRequest",
        }
        response = requests.get(weibo_url, headers=headers)
        weibo_data = json.loads(response.content.decode())["data"]
        print(weibo_data)
        weibo_json = json.dumps(weibo_data)
        print(weibo_json)
        weibos = weibo_data["cards"]
        for weibo in weibos:
            # if weibo["card_type"] == 9:
            weibo_list.append(weibo)
        if not weibos or len(weibos) < 10:
            break
        page += 1
    return weibo_list


# 下载微博中的图片
def download_images(weibo):
    weibo_id = weibo["mblog"]["id"]
    pics = weibo["mblog"].get('pics', None)
    if pics:
        for pic in pics:
            pic_url = pic["large"]["url"]
            response = requests.get(pic_url)
            with open(f"{weibo_id}.jpg", "wb") as f:
                f.write(response.content)


# 下载微博
def download_weibo(weibo):
    weibo_id = weibo["mblog"]["id"]
    created_at = weibo["mblog"]["created_at"]
    text = weibo["mblog"]["text"]
    with open(f"{weibo_id}.txt", "w", encoding="utf-8") as f:
        f.write(f"微博ID：{weibo_id}\n")
        f.write(f"发布时间：{created_at}\n")
        f.write(f"微博内容：{text}\n")
    download_images(weibo)


# 下载所有微博
def download_all_weibos(uid):
    weibo_list = get_weibo_list(uid)
    for weibo in weibo_list:
        download_weibo(weibo)


# 测试代码
if __name__ == "__main__":
    uid = "1220078652"
    # login_params = get_login_params()
    download_all_weibos(uid)
