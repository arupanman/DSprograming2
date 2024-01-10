from bs4 import BeautifulSoup
import requests #HTTP操作用

# アクセスしたいWebサイトのURL
url = 'https://tenki.jp/indexes/sleep/3/16/4410/13102/'

# Webサーバにリクエストを出す．レスポンスを変数に格納しておく
r = requests.get(url)

# HTMLソースをBeautifulSoupオブジェクトに変換する
soup = BeautifulSoup(r.text, "html.parser")

#リポジトリ名を抽出してリストに格納
#1月3日~9日までのスクレイピング
data_list = soup.find_all('p', class_='indexes-telop-0')

data= [a.get_text(strip=True) for a in data_list]

# CSVファイルに保存
converted_data = []
for value in data:
    if '暖房は必須！' in value:
        converted_data.append(1)
    elif '夜も朝も暖房' in value:
        converted_data.append(2)
    elif '寝る前に暖房' in value:
        converted_data.append(3)
    elif '翌朝少し寒い' in value:
        converted_data.append(4)
    elif 'よく眠れそう' in value:
        converted_data.append(5)
    else:
        converted_data.append(0)  # 何も該当しない場合
data=converted_data
print(data)

import os
import pandas as pd
data = pd.DataFrame({'睡眠指数': data})
file_path = 'tenki1.csv'
data.to_csv(file_path, index=False)


save_dir = '/Users/aruha/DSprograming2/DSprograming2/'
file_path = os.path.join(save_dir, 'tenki1.csv')
data.to_csv(file_path, index=False)