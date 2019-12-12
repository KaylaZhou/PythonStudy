

# key_test = {[]: 'a Test'}
# print(key_test)

# 字典的书写方式:
# NASDAQ_code = {
#     'BIDU': 'Baidu',
#     'SINA': 'Sina',
#     'YOKU': 'Youku'
# }


# a = {'key': 123, 'key': 123}
# print(a)    #字典中的键值不会有重复,相同的键值只会出现一次


# 字典中增加单一元素
# NASDAQ_code = {'BIDU': 'Baidu', 'SINA': 'Sina'}
# NASDAQ_code['YOKU'] = 'youku'
# print(NASDAQ_code)
# 输出结果:  {'BIDU': 'Baidu', 'SINA': 'Sina', 'YOKU': 'youku'}


# 典中增加多个元素:update()
# NASDAQ_code = {'BIDU': 'Baidu', 'SINA': 'Sina'}
# NASDAQ_code.update({'youku': 'you', 'hhgo': 'hhgod', 'jio': 'jio'})
# print(NASDAQ_code)


# 字典的删除: del
# NASDAQ_code = {'BIDU': 'Baidu', 'SINA': 'Sina'}
# del NASDAQ_code['BIDU']
# print(NASDAQ_code)


# 元组
# letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
# letters[0]
# print(letters[0])


# 集合:
# asd = {1, 2, 3, 4, 5}
# asd.add(6)
# print(asd)

# asd = {1, 2, 3, 4, 5}
# asd.discard(5)
# print(asd)


# 多重循环
# num_list = [6, 2, 7, 4, 1, 3, 5]
# print(sorted(num_list))

# num_list = [1, 2, 3, 4, 5]
# sorted(num_list, reverse=True)
# print(num_list)

# num = [6, 2, 7, 4, 1, 3, 5]
# str = [9, 6]
# for a, b in zip(num, str):
#     print(a, 'is', b)


# num_list = [6, 2, 7, 4, 1, 3, 5]
# print(sorted(num_list))
# sorted(num_list, reverse=True)


# 推导式:
# a = []
# for i in range(1, 11):
#     a.append(i)
#     print(a)


# b = [i for i in range(1, 11)]
# print(b)


# 一下有疑问:
# import time

# a = []
# to = time.clock()
# for i in range(1, 20000):
#     a.append(i)
# print(time.clock() - to, seconds process time ")

# to = time.clock()
# b = [i for i in range(1, 20000)]
# print(time.clock() - to, seconds process time")


# a = [i ** 2 for i in range(1, 10)]
# c = [j + 1 for j in range(1, 10)]
# k = [n for n in range(1, 10) if n % 2 == 0]
# z = [letter.lower() for letter in 'ABCDEFGHIJKLMN']
# print(a)


# letters = ['a', 'b', 'c', 'd', 'e']
# a is 1
# b is 2
# c is 4
# d is 5
# e is 6

letters = ['a', 'b', 'c', 'd', 'e']
for num, letters in enumerate(letters):
    print(letters, 'is', num + 1)
