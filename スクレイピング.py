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

print(data)