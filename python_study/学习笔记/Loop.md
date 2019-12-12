布尔运算符:
and,or

条件控制:
if...else
elif

for 循环
于...其中的每一个元素,做...事情
for item in interable:
do something

---

## 第五章 循环与判断

### 布尔类型(Ture,False)

> 就是指输出结果为 `Ture` 或 `False` 的循环
> 例子:
>
> > 1>2
> > False
>
> > 1<2<3
> > Ture
>
> > 42 != '42'
> > Ture
>
> > 'Name'=='Name'
> > False
>
> > 'M' in 'Magic'
> > Ture
>
> > number = 12
>
> > number is 12
> > Ture

> 能返回(Ture,False)这两种布尔类型的, 称为**布尔表达式**.

**1.比较运算**

> 两个函数产生的结果进行比较
>
> > (比较试成立则返回结果 Ture,不成立则返回 False)

> 比较运算符号:
>
> > | ==  | 左右两边等值的时候返回 Ture       |
> > | --- | :-------------------------------- |
> > | !=  | 左右两边不相等时返回 Ture         |
> > | >   | 左边大于右边的时候返回 Ture       |
> > | <   | 左边小于右边的时候返回 Ture       |
> > | <=  | 左边小于或等于右边的时候返回 Ture |
> > | >=  | 左边大于或等于右边的时候返回 Ture |

- 条件的比较
  > 先给变量赋值，并在多条件下比较大小:
  >
  > > middle = 5
  > > 1 < middle < 10
- 变量的比较
  > 将两个运算结果储存在不同的 变量中,再进行比较:
  >
  > > two =1 + 1
  > > three = 1 + 3
  > > two < three
- 字符串的比较
  > 就是对比左右两边的字符串是否完全一致,下面的代码就是不一致的,因为在 Python 中有着严格的大小写区分:
  >
  > > 'Eddie Van Helen' == 'eddie van helen'
- 两个函数产生的结果进行比较

  > 比较运算符 两边会先行调用函数后再进行比较，真结果等价 于 10 > 19 :
  >
  > > abs(- 10) > len(' length of this word')

  ```
  注 :abs( )是一个会返回输入参数的绝对值的函数。
  ```

**2.成员运算符与身份运算符**

- in 与 is
  把 in 放在两个对象中间的含义是，测试前者是否存在于 in 后面的集合中.
- is 和 is not
  表示身份鉴别的布尔运算符.
- in 和 not in
  则是表示归属关系的布尔运算符号.

```py
注：当你想设定一个变量，但又没想好它应该等于什么值时，可以这样设置:

a_thing = None
```

**3.布尔运算符**

- `and,or` 用于布尔值的之间的运算

> 具体规则如下:
>
> > | 运算符  | 描述                                                                                                 |
> > | ------- | :--------------------------------------------------------------------------------------------------- |
> > | not x   | 如果 x 是 Ture，则返回 False，否则返回 Ture                                                          |
> > | x and y | and 表示“并且”， 如果 x 和 y 都是 Ture，否则返回 Ture ; 如果 x 和 y 有一个是 False，否则返回 False   |
> > | x or y  | or 表示“或者”，如果 x 或 y 又其中一个是 Ture，否则返回 Ture ; 如果 x 和 y 都是 False，否则返回 False |

```py
例子：

print(1 < 3 and 2 < 5)     # Ture
print(1 < 3 and 2 > 5)     # False
print(1 < 3 or 2 > 5)      # Ture
print(1 > 3 or 2 > 5)      # False

```

### 条件控制

- `if ... else` (如果.....条件成立的, 就做......; 反之,就做......)

```py
例子:

 def account_login():
       account = input('账号:')
     if account == "000":
         password = input('密码:')
     if password == '12345':
       print('登录成功')
     else:
       print('密码输入错误')
       account_login()
     else:
       print('请重新输入')
       account_login()

account_login()

```

- `if ... elif ... else`

```py
例子:

password_list = ['周蕊', '000111']


def account_login():
    password = input('账号:')
    password_1 = (password == password_list[-1])
    password_2 = (password == password_list[0])
    if password_1:
        print('登录成功')
    elif password_2:
        new_password = input('重新输入:')
        password_list.append(new_password)
        print('Your password has changde successfully!')
        account_login()
    else:

        print('wrong password or invalid input!')
        account_login()


account_login()


```

### 循环(Loop)

- `for` 循环 (于 ... 其中的每一个元素, 做 ...事情)

```py
使用方法:


for item in iterable:
    do somthing


```

```py
注:

for (关键词,后面是一个可以容纳"每一个元素"的变量名称,但变量不能和关键词重复)
item (元素)
in (关键词,in后面跟的是一个具有"可迭代"集合形态的对象,即可以连续的提供其中的每一个元素的对象)
iterable 集合
: 冒号
  缩进

```

> 例子 1:
>
> > ```py
> > for every_letter in 'Zhou rui':
> >     print(every_letter)
> > ```
>
> > > ```py
> > > 输出结果:
> > >
> > > Z
> > > h
> > > o
> > > u
> > > r
> > > u
> > > i
> > > ```

> 例子 2:
>
> > ```py
> > for num in range(1, 11):
> >     print(str(num)+'+1 =', num+1)
> > ```

> > > ```py
> > > 输出结果:
> > >
> > > 1+1 = 2
> > > 2+1 = 3
> > > 3+1 = 4
> > > 4+1 = 5
> > > 5+1 = 6
> > > 6+1 = 7
> > > 7+1 = 8
> > > 8+1 = 9
> > > 9+1 = 10
> > > 10+1 = 11
> > >
> > > ```

> 例子 3:
>
> > ```py
> > (把 for 和 if 结合起来用:)
> >
> > songslist = ['青花瓷', '嚣张', '后来']
> >
> > for song in songslist:
> >    if song == '青花瓷':
> >       print(song, '--周杰伦')
> >    if song == 'that':
> >       print(song, '--en')
> >    if song == '后来':
> >       print(song, '--刘若英')
> >
> > ```

> > > ```py
> > > 输出结果:
> > >
> > >  青花瓷 --周杰伦
> > >  后来 --刘若英
> > >
> > > ```

- 嵌套循环 (Nested Loop)
- `While` 循环 (只要 ... 条件成立,就一直做 ... )

  ```py
    使用方法:

  while condition:
        do something

  ```

  ```py
    例子:
  ```
