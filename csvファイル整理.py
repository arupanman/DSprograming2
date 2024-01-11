import pandas as pd
import numpy as np
import os

df = pd.read_csv('/Users/aruha/DSprograming2/DSprograming2/sleepのコピー2.csv', encoding='shift_jis')

# 睡眠効率列から % を削除
df['睡眠効率'] = df['睡眠効率'].str.replace('%', '')

#不要な列を削除
columns_to_drop = ['就床時刻', '入眠時刻', '鳴動時刻', '起床時刻', '就床時間', '睡眠時間', '覚醒時間', '入眠潜時', '中途覚醒']
df = df.drop(columns=columns_to_drop)

# 日付列から "2024/1/" を削除
df['日付'] = df['日付'].str.replace('2024/1/', '')

print(df)

save_dir = '/Users/aruha/DSprograming2/DSprograming2/'
file_path = os.path.join(save_dir, 'sleep1.csv')
df.to_csv(file_path, index=False)