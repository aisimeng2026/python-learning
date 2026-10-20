names = ["小明", "小红", "小刚", "小美"]
scores =[85, 92, 78, 92]

#用zip（）把名字和成绩组合并转成列表
data =list(zip(names, scores))
print("组合后：", data)

#按成绩降序排序
#lambad x: x[1] 的意思是：按每个元素的第二个值（索引为1，即为成绩）排序
sorted＿data = sorted(data, key=lambda x: x[1], reverse=True)

#遍历并打印排名
for index, item in enumerate(sorted＿data, start=1):
    name = item[0]
    score = item[1]
    print(f"第{index}名：{name}，成绩：{score}")