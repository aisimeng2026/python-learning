text = "Hello wold! Hello Python. Python is great, and hello world is fun."

#去空格两端
text = text.strip()

#替换标点并转小写
text = text.replace(", ", "").replace(".","")
text = text.lower()

#拆分
words = text.split()

#字典统计
word＿count = {}
for word in words:
    if word in word＿count:
        word＿count[word] += 1
    else:
        word＿count[word] = 1

print(word＿count)