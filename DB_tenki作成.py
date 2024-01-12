import sqlite3
import pandas as pd
import numpy as np

df = pd.read_csv('/Users/aruha/DSprograming2/DSprograming2/tenki1.csv')

print(df)

# SQLiteデータベースへの接続
path = '/Users/aruha/DSprograming2/DSprograming2/'
db_name = 'tenki_db.sqlite'
con = sqlite3.connect(path + db_name)

# テーブル作成のSQLを実行
sql_create_table_tenki = 'CREATE TABLE IF NOT EXISTS tenki(睡眠指数 INTEGER);'
con.execute(sql_create_table_tenki)

# データフレームをSQLiteに挿入
df.to_sql('tenki', con, if_exists='replace', index=False)

# データ挿入のためのSQL
sql_insert_many = "INSERT INTO tenki VALUES (?);"

# データを挿入
cur = con.cursor()
cur.executemany(sql_insert_many, df.values.tolist())
con.commit()

# 削除対象の行を特定する条件
delete_condition = "ROWID <= 7;"

# DELETE文を実行して指定した条件の行を削除
sql_delete = f"DELETE FROM tenki WHERE {delete_condition}"
cur.execute(sql_delete)
con.commit()

# データを取得して表示
sql_select = 'SELECT * FROM tenki;'
cur.execute(sql_select)
for row in cur:
    print(row)

# DB接続を閉じる
con.close()