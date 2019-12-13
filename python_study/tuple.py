# 修改元组
# list1 = [123, 456]
# tuple = ('两点水', 'douyin', '百度', list1)
# print(tuple)
# list1[0] = 789
# list1[1] = 100
# print(tuple)


# tuple1 = (('两点水', 'douyin', '百度', [123, 456]))
# print(tuple1)
# del tuple1


tuple1 = ('一点水', '两点水', '三点水', '四点水', '五点水',)
tuple2 = ('1点点', '2点点', '3点点', '4点点', '5点点',)
list1 = [1, 2, 3, 4, 5]

# print(len(tuple1))
# print(tuple1+tuple2)
# print((tuple2) * 2)
# print('三点水'in tuple1)
# print(max(tuple2))  # 大写的数字无法识别 max
# print(min(tuple2))
print(tuple(list1))
