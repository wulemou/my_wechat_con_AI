# create by h3c s31362

import os
from dotenv import load_dotenv


# 读取本路径下的 .env 文件变量
env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(env_path)


# 加载 .env 文件下的变量
AppID = os.getenv('SZ_AppID')
AppSecret = os.getenv('SZ_AppSecret')


ACCESS_TOKEN = ''


def get_my_access_token():
    import requests
    url = f'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={AppID}&secret={AppSecret}'
    res = requests.get(url)
    print(res.json())
    if res.json()['errcode']:
        raise Exception(res.json()['errmsg'])
    return res.json()['access_token']


if __name__ == '__main__':
    ACCESS_TOKEN = get_my_access_token()
    print("ACCESS_TOKEN:\n",ACCESS_TOKEN)