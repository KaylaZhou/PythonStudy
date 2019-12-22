# 1 > 2
# 1 < 2 < 3
# 42 != '42'
# 'Name' == 'name'
# 'M' in 'Magic'
# number = 12
# number is 12


# 比较运算:
#  两个函数产生的结果进行比较
#  abs(-10) > len('length of this word')
#  'false'
# bool(0)
# 1 < 3 and 2 < 5

# for every_letter in 'hello world':
# print(every_letter)

# number = 12
# number is 12


# abs(-10) > len('length of this word')
# 'false'
# bool(0)

# 1 < 3 and 2 < 5

# is
# the_Eddie = 'Eddie'
# name = 'Eddie'
# the_Eddie == name
# the_Eddie is name


# print(1 < 3 and 2 > 5)
# print(5.0 == 5)
# print(True > False)
# print（True + False > False + False）
# print(1 <> 3)   #与 1!=3 是等价的


# album = Black Star David Bowie 25 True
# print(album)
# album.append('new song')
# lbum = 'Black Star David Bowie 25 True'
# print(album[0], album[-1])

# album = 'Black Star David Bowie 25, True'
# print('Black ' in album)


# print(bool(0))    # False
# print(bool([]))   # False
# print(bool(''))    # False
# print(bool(False))   # False
# print(bool(None))    # False

# a_thing = None

# print(1 < 3 and 2 < 5)  # Ture
# print(1 < 3 and 2 > 5)  # False
# print(1 < 3 or 2 > 5)     # Ture
# print(1 > 3 or 2 > 5)     # False

# 条件控制 if else
# def account_login():
#     account = input('账号:')
#     if account == "梅昌亮":
#         password = input('密码:')
#         if password == '12345':
#             print('登录成功')
#         else:
#             print('密码输入错误')
#             account_login()
#     else:
# print('死开,你谁啊')
# account_login()


# account_login()
#
#

# 条件控制 if else elif
# password_list = ['周蕊', '000111']    # 创建一个列表,用于储存用户的密码,初始密码和其他数据.(对实际数据库的简化模拟)


# def account_login():           # 定义函数
#     password = input('password:')    # 使用input获得用户输入的字符串并储存在变量password中.
#     password_correct = (password == password_list[-1])
#     # 当用户输入的密码等于密码列表中最后一个元素的时候(即用户最新设定的密码),登录成功.
#     password_reset = (password == password_list[0])
#     if password_correct:
#         print('Login success!')
#     elif password_reset:
#         new_password = input('Enter a new password:')
#         password_list.append(new_password)
#         print('Your password has changde successfully!')
#         account_login()
#     else:
#         print('wrong password or invalid input!')
#         account_login()


# account_login()


# password_list = ['周蕊', '000111']


# def account_login():
#     password = input('账号:')
#     password_1 = (password == password_list[-1])
#     password_2 = (password == password_list[0])
#     if password_1:
#         print('登录成功')
#     elif password_2:
#         new_password = input('重新输入:')
#         password_list.append(new_password)
#         print('Your password has changde successfully!')
#         account_login()
#     else:

#         print('wrong password or invalid input!')
#         account_login()


# account_login()


print('123123')
