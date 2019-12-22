# set 无序,不重复的集合
# set1 = set([123, 456, 789])
# print(set1)

# 添加新元素
# set1 = set([123, 456, 789])
# print(set1)
# set1.add(100)
# print(set1)
# set1.add(100)
# print(set1)


# set1 = set([123, 456, 789])
# set1.remove(456)
# print(set1)


set1 = set('hello')
set2 = set(['p', 'y', 'y', 'h', '0', 'n'])
print(set1)
print(set2)
# 输出结果:
# {'o', 'l', 'h', 'e'}
# {'n', '0', 'p', 'y', 'h'}

# 求交集(求两个set集合中相同的元素)
set3 = set1 & set2
print('\n交集 set3:')
print(set3)
# 输出结果:
# 交集 set3:
# {'h'}


# 求并集(合并两个集合的元素,并去除重复的值)
set4 = set1 | set2
print('\n并集 set4:')
print(set4)
# 输出结果:
# 并集 set4:
# {'p', '0', 'o', 'y', 'n', 'l', 'e', 'h'}


# 求差集
set5 = set1 - set2
set6 = set2 - set1
print('\n差集 set5:')
print(set5)
print('\n差集 set6:')
print(set6)
# 输出结果:
# 差集 set5:
# {'l', 'e', 'o'}
# 差集 set6:
# {'n', 'p', 'y', '0'}


# 去除重复元素(set)
list1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8]
set7 = set(list1)
print('\n去除列表中重复元素 set7:')
print(set7)
# 输出结果:
# 去除列表中重复元素 set7:
# {1, 2, 3, 4, 5, 6, 7, 8}
