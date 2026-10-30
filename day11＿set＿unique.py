text = "apple banana apple orange banana apple grape"

#1.拆分成列表
words＿list = text.split()
print("原始列表：", words＿list)

#2.转换成集合去重
unique＿words = set(words＿list)
print("去重后的集合：", unique＿words)

#3.交集运算
my＿fruits = {"apple", "pear", "grape"}
common＿fruits = unique＿words & my＿fruits
print("共同关注的水果：", common＿fruits)

#4.排序输出（把集合转成列表，再用 sorted 排序）
sorted＿fruits = sorted(list(unique＿words))
print("按字母排序后的水果：", sorted＿fruits)
