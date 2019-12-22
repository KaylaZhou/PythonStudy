
# for every_letter in 'Zhou rui':
#     print(every_letter)
# 输出结果:
# Z
# h
# o
# u

# r
# u
# i

# for num in range(1, 11):
#     print(str(num)+'+1 =', num+1)


# num = 1
# print(str(num)+'+1 =', num+1)
# num = 2
# print(str(num)+'+1 =', num+1)


# songslist = ['青花瓷', '嚣张', '后来']
# for song in songslist:
#     if song == '青花瓷':
#         print(song, '--周杰伦')
#     if song == 'that':
#         print(song, '--en')
#     if song == '后来':
#         print(song, '--刘若英')


# 嵌套循环
# for a in range(1, 10):
#     for b in range(1, 10):
#         print('{}x{}={}'.format(a, b, a*b))


# def duble_num(num):
#     if num < 10:
#         return '' + str(num)
#     return str(num)


# string = ""
# for a in range(1, 10):
#     for b in range(1, 10):
#         if a < b:
#             string += "\n"
#             break
#         else:
#             string += '{}x{}={}  '.format(a, b, duble_num(a * b))

# print(string)


# while 循环
# count = 0
# while True:
#     print('Repent this line!')
#     count = count + 1
#     if count == 3:
#         break

# count = 0
# while True:
#     print('一直做!')
#     count = count + 1
#     if count == 4:
#         break


# while 1 < 3:
#     print('我爱你')    #这是一个死循环


password_list = ['*#*#', '12345']


def account_login():
    tries = 3
    while tries > 0:
        password = input('密码:')
        password_correct = password == password_list[-1]
        password_reset = password == password_list[0]

        if password_correct:
            print('登录成功!')
        elif password_reset:
            new_password = input('输入新密码:')
            password_list.append(new_password)
            print('密码已修改成功!')
            account_login()
        else:
            print('密码错误或输入无效!')
            tries = tries - 1
            print('尝试' '剩余次数')
    else:
        print('您的账户已被冻结!')


account_login()
