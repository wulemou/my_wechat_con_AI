# create by h3c s31362


import os
from dotenv import load_dotenv


# 读取本项目内的 .env 文件变量
env_path = os.path.join(os.path.dirname(__file__), "..", '.env')
load_dotenv(env_path)


class itchat_manage():

    ACCESS_TOKEN = ''

    # 加载 .env 文件下的变量
    AppID = os.getenv('SZ_AppID')
    AppSecret = os.getenv('SZ_AppSecret')


    def create_my_access_token(self):
        import requests
        url = (f'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={self.AppID}&secret'
               f'={self.AppSecret}')

        res = requests.get(url)

        print("接收 access token 是:", res.json())

        if res.json()['errcode']:
            raise Exception(res.json()['errmsg'])

        self.ACCESS_TOKEN = res.json()['access_token']

        return res.json()['access_token']


    def get_my_access_token(self):
        return self.ACCESS_TOKEN


    def refresh_my_access_token(self):
        pass


if __name__ == '__main__':

    im = itchat_manage()

    im.create_my_access_token()

    print("ACCESS_TOKEN:\n", im.get_my_access_token())
