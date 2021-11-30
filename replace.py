f1 = open('weight.txt', 'r', encoding='utf-8')
lines = f1.readlines()
f1.close()

f2 = open('weight.txt', 'w', encoding='utf-8')
for line in lines:
    f2.write(line.replace("'", '"'))
f2.close()