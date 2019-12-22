# class
# 类的属性 = 类的变量


# class cocacola:
#     formula = ['caffeine', 'sugar', 'water', 'sode']


# coke_for_me = cocacola()
# coke_for_you = cocacola()
# print(cocacola.formula)
# print(coke_for_me.formula)
# print(coke_for_you.formula)


# class cocacola:
#     formula = ['caffeine', 'sugar', 'water', 'sode']


# coke_for_me = cocacola()

# for element in coke_for_me.formula:
#     print(element)

#

#
#
# 实例属性(实例变量)
# class cocacola:
#     formula = ['caffeine', 'sugar', 'water', 'sode']


# coke_for_china = cocacola()
# coke_for_china.local_logo = '可口可乐'  # 创建实例属性
# print(coke_for_china.local_logo)  # 打印实例属性引用结果
#
#
#
#
#


# 实例方法1
# class cocacola:
#     formula = ['caffeine', 'sugar', 'water', 'sode']

#     def drink(self):
#         print('Energy!')


# coke = cocacola()
# coke.drink()
#
#
# 实例方法2
# class cocacola:
#     formula = ['caffeine', 'sugar', 'water', 'sode']

#     def drink(coke):       # HERE!
#         print('Energy!')


# coke = cocacola()
# coke.drink()

#
#
#
#
#

# class cocacola:
#     formula = ['caffeine', 'sugar', 'water', 'sode']

#     def drink(self, how_much):
#         if how_much == 'a sip':
#             print('cool~')
#         elif how_much == 'whole bottle':
#             print('headache!')


# ice_coke = cocacola()
# ice_coke.drink('a sip')


# a = 2 % 5
# print(a)


a = 3
b = 10
c = 3
# c %= a
# c **= a
c //= a
print('4-c的值为:', c)
