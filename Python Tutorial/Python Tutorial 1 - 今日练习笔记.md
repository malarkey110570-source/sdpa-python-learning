

title: Python Tutorial 1 - 今日练习笔记  
date: 2026-09-22  
tags:

- Python
    
- SDPA
    
- Tutorial-1
    
- 学习笔记  
    aliases:
    
- Python Tutorial 1
    

---

# Python Tutorial 1 - 今日练习笔记

> [!summary] 今日完成内容  
> 学习了变量、基础数据类型、输入输出、类型转换、字符串拼接、基础运算符、条件判断和基础代码格式；完成了 Tutorial 1 的全部练习与 Challenge。

## 1. 变量与赋值

变量可以理解为保存数据的名字。Python 使用 `=` 给变量赋值：左边是变量名，右边是要保存的值或表达式。

```
x = 1
y = x + 5
z = y

print(x)  # 1
print(y)  # 6
print(z)  # 6
```

这里的 `=` 表示“把右边的值赋给左边的变量”，不是数学中的“相等”。

```
x = 1
x = x + 1
print(x)  # 2
```

也可以在同一行给多个变量赋值：

```
a, b = 3, 4
print(a, b)
```

## 2. 基础数据类型

Python 中本节使用了四种基础数据类型：

|类型|含义|示例|
|---|---|---|
|`int`|整数|`1`、`22`、`-3`|
|`float`|浮点数（小数）|`1.0`、`1.75`|
|`bool`|布尔值|`True`、`False`|
|`str`|字符串（文本）|`"hello"`、`"22"`|

使用 `type()` 可以检查数据类型：

```
x = 1
print(type(x))  # <class 'int'>

x = 1.0
print(type(x))  # <class 'float'>

x = True
print(type(x))  # <class 'bool'>

x = "1"
print(type(x))  # <class 'str'>
```

> [!important] 数值和文本看起来可能一样，但类型不同  
> `22` 是整数，`"22"` 是字符串。它们能够进行的操作不同。

## 3. `input()` 与输入

`input()` 用来接收键盘输入，括号中的字符串是显示给用户的提示语。

```
name = input("Enter your name: ")
print(name)
```

### `input()` 默认返回 `str`

无论用户输入的是姓名还是数字，`input()` 的结果默认都是字符串。

```
x = input("Enter a number: ")
print(x)
print(type(x))  # <class 'str'>
```

因此下面的外层 `str()` 是多余的：

```
# 可以运行，但 str() 没有必要
name = str(input("Please enter your name: "))

# 更简洁
name = input("Please enter your name: ")
```

## 4. 类型转换

### 转换为整数：`int()`

```
x = input("Enter a number: ")
x = int(x)
print(type(x))  # <class 'int'>
```

也可以直接在输入时转换：

```
x = int(input("Enter a number: "))
```

如果输入内容不能表示整数，例如 `hello` 或 `1.5`，直接使用 `int()` 会报错。

### 转换为浮点数：`float()`

需要接收身高、体重等小数时，可以使用 `float()`：

```
height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))
```

### 转换为字符串：`str()`

需要把数值和文本拼接时，先用 `str()` 把数值转换成字符串：

```
age = 22
print("I am " + str(age) + " years old.")
```

## 5. 字符串拼接

字符串之间可以使用 `+` 拼接：

```
hello = "hello"
world = "world"
message = hello + " " + world
print(message)  # hello world
```

字符串不能直接和整数相加：

```
x = 5
print("The number is " + x)  # TypeError
```

修正方法是先进行类型转换：

```
x = 5
print("The number is " + str(x))
```

字符串的 `+` 是拼接，不是数学加法：

```
age = "22"
print(age + age)  # 2222
```

## 6. 基础运算符

### 算术运算符

|运算符|作用|示例|
|---|---|---|
|`+`|加法|`2 + 3` 得到 `5`|
|`-`|减法|`5 - 2` 得到 `3`|
|`*`|乘法|`4 * 3` 得到 `12`|
|`/`|普通除法，结果为浮点数|`17 / 3` 得到约 `5.67`|
|`//`|向下取整除法|`17 // 3` 得到 `5`|
|`%`|取余数|`17 % 3` 得到 `2`|
|`**`|幂运算|`2 ** 3` 得到 `8`|

本次练习重点比较了 `/`、`//` 和 `%`：

```
print(17 / 3)   # 5.666666666666667
print(17 // 3)  # 5
print(17 % 3)   # 2
```

利用商和余数可以还原原数：

```
number = 17
divisor = 3

original = (number // divisor) * divisor + (number % divisor)
print(original)  # 17
```

规律：

```
原数 = 商 × 除数 + 余数
```

### 比较运算符

|运算符|含义|
|---|---|
|`==`|等于|
|`!=`|不等于|
|`>`|大于|
|`<`|小于|
|`>=`|大于或等于|
|`<=`|小于或等于|

> [!warning] `=` 和 `==` 不同  
> `=` 用于赋值；`==` 用于比较两个值是否相等。

```
number = 4          # 把 4 赋给 number
print(number == 4)  # 比较，结果是 True
```

## 7. 运算优先级与括号

在本节涉及的运算中：

1. 先计算括号中的内容。
    
2. 再计算 `*`、`/`、`//`、`%`。
    
3. 最后计算 `+`、`-`。
    

```
number = 1 + 2 * 3 / 4.0
print(number)  # 2.5
```

括号可以明确改变运算顺序：

```
x = 4
y = 3

result = (x + y) * (x + y)
print(result)  # 49
```

写 BMI 时，分母必须加括号：

```
bmi = weight / (height * height)
```

下面的写法会变成 `(weight / height) * height`，不再是 BMI 公式：

```
bmi = weight / height * height  # 错误公式
```

## 8. `if` / `else` 条件判断

条件判断可以让程序根据条件执行不同的代码。

```
number = int(input("Please enter an integer: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

需要注意：

- `if` 后面写条件，并以冒号 `:` 结束。
    
- `else` 后面也必须有冒号 `:`。
    
- 分支中的代码必须缩进，通常使用 4 个空格。
    
- 判断是否相等要使用 `==`，不能使用 `=`。
    

## 9. PEP 8 基础格式

PEP 8 是 Python 常用的代码格式规范。本次练习先记住以下几点。

### 运算符两侧留空格

```
# 推荐
result = (x + y) * (x + y)
tempo_pace_time = (7 * 60 + 12) * 3

# 不推荐
result=(x+y)*(x+y)
tempo_pace_time = (7 * 60 + 12) *3
```

### 变量名清楚并使用下划线

```
easy_pace_seconds = 8 * 60 + 15
tempo_pace_seconds = 7 * 60 + 12
```

变量名应尽量准确。例如代码中的 `star_time` 容易被理解为“星星时间”，实际应写成 `start_time`。

### 注释与代码保持清晰

```
print(17 // 3)  # 商（向下取整）
```

行尾注释前通常留两个空格，`#` 后留一个空格。

### 使用英文半角符号写代码

Python 代码必须使用英文半角括号 `()`。中文输入法下的全角左括号 `（` 是 Unicode 字符 `U+FF08`，Python 无法把它识别为正常代码括号。

```
# 正确
print("Hello")

# 错误：使用了中文全角括号
print（"Hello"）
```

## 10. 今日练习过程

### 练习 1：计算平方和立方

思路：接收一个整数，分别将它乘两次和乘三次。

```
number = int(input("Enter a number: "))

squared = number * number
cubic = number * number * number

print(squared)
print(cubic)
```

本题练习了：`input()`、`int()`、变量和乘法。

### 练习 2：计算 BMI

公式：

```
BMI = 体重（kg）÷ 身高²（m²）
```

```
height = float(input("Enter your height in metres: "))
weight = float(input("Enter your weight in kilograms: "))

bmi = weight / (height * height)

print("Your BMI is " + str(bmi))
```

修正点：身高和体重可能带小数，所以使用 `float()`；分母 `height * height` 必须放在括号中。

### 练习 3：计算 `(x + y) * (x + y)`

```
x = int(input("Please enter an integer: "))
y = int(input("Please enter an integer: "))

result = (x + y) * (x + y)

print("Your result is " + str(result))
```

本题重点是使用括号改变并明确运算顺序。示例 `x = 4`、`y = 3` 时，结果为 `49`。

### 练习 4：12 小时制时间

题目：早上 8 点的 9 小时后是几点？

```
start_time = 8
hours_later = 9

final_time = (start_time + hours_later) % 12

print(str(final_time) + " pm")
```

计算过程：`8 + 9 = 17`，`17 % 12 = 5`，所以答案是下午 5 点。

本题中 `% 12` 用来把超过 12 的小时数转换回 12 小时制。

### 练习 5：姓名输入与输出

输入姓名并输出问候：

```
name = input("Please enter your name: ")
print("Hello " + name + ", would you like to learn some Python today?")
```

这里不需要写 `str(input(...))`，因为 `input()` 已经返回字符串。

输入姓和名，再按“姓 名”的顺序输出：

```
first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")

print("Welcome " + last_name + " " + first_name + "!")
```

本题练习了变量、输入和字符串拼接。

### Challenge 1：计算 `n + nn + nnn`

以 `n = 5` 为例：

```
5 + 55 + 555 = 615
```

```
n = input("Please enter an integer: ")
nn = n * 2
nnn = n * 3

result = int(n) + int(nn) + int(nnn)

print(result)
```

这里先利用字符串重复得到 `nn` 和 `nnn`，再用 `int()` 转换后进行数学加法。

### Challenge 2：判断奇数或偶数

```
number = int(input("Please enter an integer: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

判断依据：一个数除以 2 后余数为 0，它就是偶数；否则是奇数。

本题修正了 `=` 与 `==` 的区别，并确认 `else` 后需要冒号。

### Challenge 3：四位数各位数字之和

```
number = int(input("Enter a four-digit integer: "))

digit1 = number % 10
number = number // 10

digit2 = number % 10
number = number // 10

digit3 = number % 10
number = number // 10

digit4 = number % 10

result = digit1 + digit2 + digit3 + digit4
print(result)
```

拆位规律：

- `number % 10` 取得当前个位数字。
    
- `number // 10` 去掉当前个位数字。
    
- 重复以上两步，依次取出四个数字。
    

例如 `1234`：

|步骤|当前数|`% 10` 取得|`// 10` 后剩下|
|---|---|---|---|
|1|1234|4|123|
|2|123|3|12|
|3|12|2|1|
|4|1|1|-|

所以各位数字之和为 `4 + 3 + 2 + 1 = 10`。

### Challenge 4：6:52 跑步时间

题目过程：

- 6:52 a.m. 出发。
    
- 以 8 分 15 秒每英里的速度跑 1 英里。
    
- 以 7 分 12 秒每英里的速度跑 3 英里。
    
- 再以 8 分 15 秒每英里的速度跑 1 英里。
    

关键思路：分钟和秒不能直接当成小数相加，先把每段时间统一换算成秒。

```
easy_pace_seconds = 8 * 60 + 15
tempo_pace_seconds = 7 * 60 + 12

total_seconds = easy_pace_seconds * 2 + tempo_pace_seconds * 3

elapsed_minutes = total_seconds // 60
final_second = total_seconds % 60

start_hour = 6
start_minute = 52

total_minutes = start_minute + elapsed_minutes
final_hour = start_hour + total_minutes // 60
final_minute = total_minutes % 60

print(str(final_hour) + ":" + str(final_minute) + ":" + str(final_second) + " am")
```

计算过程：

```
轻松跑一次：8 × 60 + 15 = 495 秒
节奏跑一次：7 × 60 + 12 = 432 秒
总时间：495 × 2 + 432 × 3 = 2286 秒
2286 秒 = 38 分 6 秒
6:52:00 + 0:38:06 = 7:30:06 a.m.
```

最终答案：**7:30:06 a.m.**

当前代码会显示 `7:30:6 am`，计算结果是正确的，只是秒数没有补成两位。显示格式可以在以后学习字符串格式化时再优化。

## 11. 今日易错点

|易错点|错误表现|正确做法|
|---|---|---|
|中文全角括号|出现 `U+FF08` 或语法错误|切换英文输入法，使用 `()`|
|`input()` 外层多写 `str()`|代码冗余|记住 `input()` 默认返回 `str`|
|BMI 分母没有括号|计算顺序错误|写成 `weight / (height * height)`|
|变量命名不准确|`star_time` 容易产生误解|改为 `start_time`|
|运算符两侧没有空格|可读性较差|写成 `x + y`、`value * 3`|
|字符串与数值直接 `+`|出现 `TypeError`|用 `str()` 转换数值|
|混淆 `=` 与 `==`|条件判断写错|赋值用 `=`，比较用 `==`|
|`else` 后漏掉冒号|出现语法错误|写成 `else:`|
|不理解 `% 10` 与 `// 10`|不知道如何拆位|`% 10` 取个位，`// 10` 去个位|
|时间单位没有统一|分钟和秒相加出错|先统一换算成秒，再换回分和秒|
|忘记运算优先级|公式结果与预期不同|用括号明确希望的计算顺序|

## 12. 复习清单

- 我能解释变量和 `=` 的作用。
    
- 我能区分 `int`、`float`、`bool` 和 `str`。
    
- 我记得 `input()` 默认返回 `str`。
    
- 我会使用 `int()`、`float()` 和 `str()` 做类型转换。
    
- 我知道字符串和整数不能直接使用 `+` 拼接。
    
- 我能说出 `/`、`//` 和 `%` 的区别。
    
- 我会使用括号控制运算顺序。
    
- 我能区分赋值运算符 `=` 和比较运算符 `==`。
    
- 我会正确写出带冒号和缩进的 `if` / `else`。
    
- 我会用 `% 2` 判断奇偶。
    
- 我会用 `% 10` 取个位，用 `// 10` 去掉个位。
    
- 我会先统一时间单位，再进行时间计算。
    
- 我会在运算符两侧留空格，并使用清楚的变量名。
    

## 13. 今日一句话总结

Python 的数据类型决定了数据可以怎样运算；写程序时要先确认输入的类型，再通过类型转换、运算符、括号和条件判断一步步完成计算。