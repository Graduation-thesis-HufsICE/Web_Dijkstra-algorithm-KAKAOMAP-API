import pandas as pd
import sys

sys.stdout = open('linkId2.txt', 'w', encoding='utf-8')


df1 = pd.read_csv("2021_seoul.csv", encoding = 'utf-8')
node = df1[["시점명", "종점명", "링크아이디"]] 

dict = {}

for i in range (len(df1)): 
    if df1.loc[i, "링크아이디"] not in dict:
        dict[str(df1.loc[i, "링크아이디"])] = [0, 0]
    dict[str(df1.loc[i, "링크아이디"])][0] = df1.loc[i, "시점명"]
    dict[str(df1.loc[i, "링크아이디"])][1] = df1.loc[i, "종점명"]

# print(dict)

print('{')
for i in dict:
    print("'"+str(i)+"'",': ', dict[i],',')
print('{')