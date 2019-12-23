#!/usr/bin/python3

# # def file_1(a):
#     a = 1
#     return(1, 11)

# file = open('C:\Users\zhour\OneDrive\桌面\file_1\.txt', 'w')

# 新建文件夹,和txt文档
# for name in range(1, 11):
#     desktop_path = 'C:\\Users\zhour\OneDrive\桌面'
#     full_path = desktop_path + str(name) + '.txt'
#     file = open(full_path, 'w')
#     file.close()

# 输出奇数/偶数 0代表奇数,1代表偶数
# n = 0
# while n < 10:
#     n = n + 1
#     if n % 2 == 1:
#         continue
# print(n)


# import math
# dir(math)

# ?
# import random
# random: 随机

# print("choice([1, 2, 3, 5, 9]) : ", random.choice([1, 2, 3, 5, 9]))
# print("choice(['A String']): ", random.choice(['A String']))
# choice:选择

# a = 17 // 3
# print(a)


# a = 2**7
# # complex(a, 8)
# print(a)


# a = 9*3/2.5+6.2
# print(a)


# tax = 12.5 / 100
# price = 100.50
# price * tax
# # print(price * tax)
# price + (price * tax)
# # print(price + (price * tax))
# round = (price + (price * tax), 2)
# print(round)


# print('hello world')


# if True:
# print('Answer')
# print('True')
# else:
# print('Answer')
# print('False')


# a = 17 // 3
# print(a)


# a = 28 % 5
# print(a)


# 练习:英制单位英寸与公制单位厘米互换
# value = float(input('请输入长度:'))
# unit = input('厘米:')
# if unit == 'in' or unit == '英寸':
#     print('%2f英寸=%2f厘米' % (value, value*2.54))
# elif unit == 'cm' or unit == '厘米':
#     print('%2f厘米=%2f英寸' % (value, value/2.54))
# else:
#     print('输入错误')


# 练习考试分数对应的等级
# score = float(input('请输入成绩:'))

# if score >= 90:
#     print('A')
# elif score >= 80:
#     print('B')
# elif score >= 70:
#     print('C')
# elif score >= 60:
#     print('D')
# else:
#     grade = "E"
#     print('对应的等级是:', grade)


# sum = 1
# for x in range(1, 10):

#     xxx = sum * x
#     print('结果:', xxx)
# 输出结果:
# 结果: 1
# 结果: 2
# 结果: 3
# 结果: 4
# 结果: 5
# 结果: 6
# 结果: 7
# 结果: 8
# 结果: 9


sum = 1
for x in range(1, 10):
    sum += x    # sum = sum*x
    print('结果:', sum)
