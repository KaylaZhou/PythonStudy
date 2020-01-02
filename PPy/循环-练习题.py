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


# sum = 1
# for x in range(1, 10):
#     sum += x    # sum = sum+x
#     print('结果:', sum)


# 求和方法一:
# sum = 0
# for x in range(2, 10):  #
#     sum += x
#     print('结果为:', sum)

# 求和方法二:
# sum = 0
# for x in range(0, 10):
#     if x % 1 == 0:  # %取模,返回除法的余数(a % b,输出结果 1)
#         sum += x
#         print(sum)


# 猜数字游戏:whlie循环
# import random

# answer = random.randint(1, 100)
# counter = 0
# while True:
#     counter += 1
#     number = int(input('请输入:'))
#     if number < answer:
#         print('大一点')
#     elif number > answer:
#         print('小一点')
#     else:
#         print('恭喜你猜对了!')
#         break
# print('你总共猜了%d次' % counter)
# if counter > 7:
#     print('你的智余额明显不足')


# 嵌套循环:九九乘法表
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('%dx%d=%d' % (i, j, i*j), end='\t')
#     print()


# def duble_num(num):
#     if num < 10:
#         return ' ' + str(num)
#     return str(num)


# string = ""
# for a in range(1, 10):

#     for b in range(1, 10):
#         if a < b:
#             string += "\n"
#             break
#         else:
#             string += '{}x{}={} '.format(a, b, a * b)

# print(string)

# for b in range(1, 10):

# for a in range(1, 10):
#     print(a)

# xx = 0
# for a in range(1, 10):
#     xx = a
# print(xx)
# 输出结果为：9

# xx = 0
# for a in range(1, 10):
#     xx = a
#     print(xx)
# 输出结果为：1-9


for a in range(1, 10):
    xx = a
    print(xx)
