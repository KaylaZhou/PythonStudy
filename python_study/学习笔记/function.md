# 函数

> [函数介绍](https://docs.python.org/3/library/functions.html)

## 创建函数的语法:

```py
def function():
    reture 'something'

```

```py
注释:

def
关键字

function( ):
函数名(参数)冒号

     return'something'
缩进 关键字 '返回结果'
```

## 数学函数:

### 1.abs()

- 含义:表示函数返回数字的绝对值.

- 语法:

  ```py
  abs(x)
  ```

> 注:
>
> 参数 x -- 数值表达式,可以是整数,浮点数,复数. (abs 只能有一个参数)
>
> 返回值: 函数返回 x(数字)的绝对值,如果参数是一个复数,则返回它的大小.

- 例子:

  ```py
    例子1:
     print('abs(40.50):', abs(40.50))

  ```

  ```
    输出结果:abs(40.50): 40.5
  ```

  ```py
    例子 2:

      v = complex(3, 4)
      abs(v)
      print(abs(v))

  ```

  ```
   输出结果:5.0
  ```

### 2.ceil(x)

- 含义: 表示函数返回一个`大于`,或`等于` x 的`最小整数`.(负浮点数取最小,正浮点数取最大)

- 语法:

  ```py
    import math

    math.ceil(x)
  ```

  注:ceil( )不能被直接访问,需要导入`math`模块.通过静态对象调用该方法.

- 例子:

  ```py
   import math

   print('math.ceil(-98.1):', math.ceil(-98.1))
   print('math.ceil(98.1):', math.ceil(98.1))
   print('math.ceil(math.pi):', math.ceil(math.pi))

  ```

  ```py
  输出结果:
     math.ceil(-98.1):  -98
     math.ceil(98.1):    99
     math.ceil(math.pi):  4
  ```

  注意:

  math.ceil(math.pi)中的 `pi` 是`圆周率` ;

  **math** 是数字,用于定义 pi;

  (math.pi)必须一起使用,否则会提示 pi 没有被定义.

### 3.fabs()

- 含义:返回数字的绝对值,如 math.fabs(-10)返回 10.0
- 区别:fabs()与 abs()
  | abs( ) | fabs( ) |
  | :---------------------- | :--------------------- |
  | 内置函数 | 需要在 math 模块中定义 |
  | 可以运用在复数中 | 只对浮点型,整型数值有效 |
- 语法:

  ```py
     import math

     math.fabs(x)
  ```

- 例子:

  ```py
    import math

    print('math.fabs(-98.19):', math.fabs(-98.19))
    print('math.fabs(100.12):', math.fabs(100.12))
    print('math.fabs(math.pi):', math.fabs(math.pi))

  ```

  ```py
  输出结果:
     math.fabs(-98.19): 98.19
     math.fabs(100.12): 100.12
     math.fabs(math.pi): 3.141592653589793
  ```

### 4.exp()

- 含义: exp(x)是返回 x 的指数. e 的 x 次幂,如 math.exp(1)返回 2.718281828459045
- 语法:

  ```py
      import math

      math.exp(x)
  ```

- 例子:

  ```py
     import math

     print('math.exp(-98.19):', math.exp(-98.19))
     print('math.exp(100.12):', math.exp(100.12))
     print('math.exp(math.pi):', math.exp(math.pi))

  ```

  ```py
  输出结果:
    math.exp(-98.19): 2.2731328695379347e-43
    math.exp(100.12): 3.0308436140742566e+43
    math.exp(math.pi): 23.140692632779267
  ```

````
###  5.()

- 含义:

- 语法:

  ```py
     import math
  ```

- 例子:

  ```py

  ```

  ```py
  输出结果:

  ```
````

### 5.floor()

- 含义:返回数字的`下舍整数`,`小于` 或`等于` x.

- 语法:

  ```py
     import math

     math.floor(x)
  ```

- 例子:

  ```py
     import math

     print('math.floor(-98.19):', math.floor(-98.19))
     print('math.floor(100.12):', math.floor(100.12))
     print('math.floor(100.82):', math.floor(100.82))
     print('math.floor(math.pi):', math.floor(math.pi))

  ```

  ```py
  输出结果:
      math.floor(-98.19): -99
      math.floor(100.12): 100
      math.floor(100.82): 100
      math.floor(math.pi): 3
  ```

```

```
