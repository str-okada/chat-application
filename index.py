import requests 
import os
from dotenv import load_dotenv

# .envファイルの内容を読み込見込む
load_dotenv()

# os.environを用いて環境変数を表示させます
# print(os.environ['API_KEY'])

TOKEN = os.environ['API_KEY']
api_url = 'https://notify-api.line.me/api/notify'
send_contens = 'Taro'

TOKEN_dic = {'Authorization' : 'Bearer' + ' ' + TOKEN}
send_dic = {'message' : send_contens}

# print(TOKEN_dic)
# print(send_dic)
# requests.post(api_url, headers=TOKEN_dic, data=send_dic)

image_file = './students.png'
binary = open(image_file, mode="rb")
image_dic = {'imageFile':binary}

requests.post(api_url, headers=TOKEN_dic, data=send_dic, files=image_dic)