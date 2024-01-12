import pandas as pd
import numpy as np
import sqlite3

# CSVファイルからデータを読み込む
df = pd.read_csv('/Users/aruha/DSprograming2/DSprograming2/sleepのコピー2.csv', encoding='shift_jis')

# 睡眠効率列から % を削除
df['睡眠効率'] = df['睡眠効率'].str.replace('%', '')

# 不要な列を削除
columns_to_drop = ['就床時刻', '入眠時刻', '鳴動時刻', '起床時刻', '就床時間', '睡眠時間', '覚醒時間', '入眠潜時', '中途覚醒']
df = df.drop(columns=columns_to_drop)

# 日付列から "2024/1/" を削除
df['日付'] = df['日付'].str.replace('2024/1/', '')
print(df)

# SQLiteデータベースへの接続
path = '/Users/aruha/DSprograming2/DSprograming2/'
db_name = 'sleep_db.sqlite'
con = sqlite3.connect(path + db_name)

# テーブル作成のSQLを実行
sql_create_table_sleep = 'CREATE TABLE IF NOT EXISTS sleep(日付 TEXT, スヌーズ INTEGER, 睡眠効率 REAL, 快眠スコア REAL);'
con.execute(sql_create_table_sleep)

# データフレームをSQLiteに挿入
df.to_sql('sleep', con, if_exists='replace', index=False)

# データ挿入のためのSQL
sql_insert_many = "INSERT INTO sleep VALUES (?, ?, ?, ?);"

# データを挿入
cur = con.cursor()
cur.executemany(sql_insert_many, df.values.tolist())
con.commit()

# 削除対象の行を特定する条件
delete_condition = "ROWID <= 7;"

# DELETE文を実行して指定した条件の行を削除
sql_delete = f"DELETE FROM sleep WHERE {delete_condition}"
cur.execute(sql_delete)
con.commit()

# データを取得して表示
sql_select = 'SELECT * FROM sleep;'
cur.execute(sql_select)
for row in cur:
    print(row)

# DB接続を閉じる
con.close()
