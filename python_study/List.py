# 一个产品,需要列出产品的用户
User = ['douyin', 'bilibili', 'kuaishou']
print('1.产品用户:')
print(User)

# 统计有多少的平台
len(User)
print('\n2.统计有多少个用户:')
print(len(User))

# 查看具体用户
print('\n3.查看具体用户:')
print(User[0]+',' + User[1]+',' + User[2]+',')


# 新增一个用户
print('\n4.新增一个用户:')
User.append('百度')
print(User)

# 替换第一个用户
User[0] = '抖音'
print('\n5.替换第一个用户:')
print(User)


# 删除第二个用户
del User[1]
print('\n6.删除第二个用户:')
print(User)


# VIP用户,添加到指定位置
User.insert(0, 'VIP')
print('\n7.VIP用户调整到指定位置:')
print(User)

# 删除末尾用户
User.pop()
print('\n8.删除末尾用户:')
print(User)

# 删除指定位置的元素
User.pop(1)
print('\n9.删除指定位置的元素:')
print(User)

# 每个用户后面展现账号
new_User = [['VIP', 666666], ['kuaishou', 111111]]
print('\n10.每个用户后面展现账号:')
print(new_User)
