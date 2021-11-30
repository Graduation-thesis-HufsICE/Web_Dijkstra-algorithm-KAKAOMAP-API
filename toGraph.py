import json
import sys
with open('linkId2.json', 'r', encoding='utf-8') as f1:
    json_data1 = json.load(f1)

with open('weight.json', 'r', encoding='utf-8') as f2:
    json_data2 = json.load(f2)

sys.stdout = open('graph_final.txt', 'w', encoding='utf-8')


dict = {}

for i in json_data1.keys(): 
    for j in json_data1.keys():
        if i ==j:
            dict[json_data1[0]] = {json_data1[1], json_data2[i]}

print('{')
for i in dict:
    print("'"+str(i)+"'",': ', dict[i],',')
print('}')

print(json_data1.keys())



# df1 = pd.read_csv("2020_10_4_seoul.csv", encoding = 'euc-kr')
# print(df1)
