import sqlite3


# DBファイルを保存するためのファイルパス

# Google Colab
path = '/content/'

# ローカル（自分のMac）
# path = '../db/'

# DBファイル名
db_name = 'sleep.sqlite'

# DBに接続する（指定したDBファイル存在しない場合は，新規に作成される）
con = sqlite3.connect(path + db_name)

# DBへの接続を閉じる
con.close()

# 1．DBに接続する
con = sqlite3.connect(path + db_name)
# print(type(con))

# 2．SQLを実行するためのオブジェクトを取得
cur = con.cursor()

# 3．実行したいSQLを用意する
# テーブルを作成するSQL
sql_create_table_sleep = 'CREATE TABLE sleep(sleep text);'

# 4．SQLを実行する
cur.execute(sql_create_table_sleep)

# 5．必要があればコミットする（データ変更等があった場合）
# 今回は必要なし

# 6．DBへの接続を閉じる
con.close()

"""# スクレイピング"""

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

converted_data = []
for value in data:
    if '暖房は必須！' in value:
        converted_data.append(1)
    elif '夜も朝も暖房' in value:
        converted_data.append(2)
    elif '翌朝少し寒い' in value:
        converted_data.append(4)
    else:
        converted_data.append(0)  # 何も該当しない場合
data=converted_data
data

#テーブルを作る
# 1．DBに接続する
con = sqlite3.connect(path + db_name)
# print(type(con))

# 2．SQLを実行するためのオブジェクトを取得
cur = con.cursor()

# 3．SQLを用意
# データを挿入するSQL
# INSERT INTO テーブル名 VALUES (列に対応したデータをカンマ区切りで);
sql_insert_data = "INSERT INTO sleep VALUES (?);"


# 4．SQLを実行
cur.executemany(sql_insert_data, [(value,) for value in data])

# 5．コミット処理（データ操作を反映させる）
con.commit()

# 6．DBへの接続を閉じる
con.close()

# 1．DBに接続する
con = sqlite3.connect(path + db_name)
# print(type(con))

# 2．SQLを実行するためのオブジェクトを取得
cur = con.cursor()

# 3．SQLを用意
# SELECT * FROM テーブル名;
# *の部分は取得したい列の名前をカンマ区切りで指定することもできる
sql_select = 'SELECT * FROM sleep;'

# 4．SQLを実行
cur.execute(sql_select)

for r in cur:
  print(r)

# 6．DBへの接続を閉じる
con.close()



import pandas as pd
import numpy as np
df = pd.read_csv('/sleep.csv')


# 睡眠効率列から % を削除
df['睡眠効率'] = df['睡眠効率'].str.replace('%', '')
# 7行目と8行目を削除
df = df.drop([7, 8])
#不要な列を削除
columns_to_drop = ['就床時刻', '入眠時刻', '鳴動時刻', '起床時刻', '就床時間', '睡眠時間', '覚醒時間', '入眠潜時', '中途覚醒', 'スヌーズ']
df=df.drop(columns=columns_to_drop)
# 日付の順番とデータベースの順番を合わせる
df = df.sort_values(by='日付', ascending=True)

data

