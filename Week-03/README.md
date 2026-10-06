# Week 03 — Compound Data Types & Looping
# 第 03 周：复合数据类型与循环应用

> **Course:** EMATM0048 — Software Development: Programming and Algorithms (SDPA)  
> **Topics:** Objects · Tuples · Lists · Dictionaries · Sets · Unpacking · Zip · Enumerate · Looping

---

# 1. Week Overview | 本周概览

本周主要学习 Python 中的 **Compound Data Types（复合数据类型）**：

- Tuple | 元组
- List | 列表
- Dictionary | 字典
- Set | 集合

同时继续使用之前学过的：

- `for`
- `if`
- `in`
- `not in`

把数据结构和控制流程结合起来解决问题。

本周最重要的思维：

```text
先判断数据是什么
↓
再判断需要进行什么操作
↓
选择合适的方法
↓
使用 for / if 将它们组合起来
```

例如：

```text
需要遍历每个元素
→ for

需要判断
→ if

需要判断是否存在
→ in / not in

需要往 list 末尾加入元素
→ append()

需要 dictionary 的 key + value
→ items()
```

---

# 2. Everything in Python is an Object
# Python 中一切都是对象

Python 中的数据都可以看成 object。

一个 object 主要具有：

- Value | 值
- Type | 类型
- Identity | 身份

例如：

```python
x = 10

print(type(x))
print(id(x))
```

变量本身可以理解为：

> 一个指向 object 的 reference。

---

# 3. `==` vs `is`

## `==`

比较两个对象的 **value 是否相等**。

```python
a = [1, 2]
b = [1, 2]

print(a == b)
```

输出：

```text
True
```

因为两个 list 的内容相同。

---

## `is`

比较两个变量是否指向 **同一个 object**。

```python
print(a is b)
```

可能得到：

```text
False
```

虽然内容一样，但它们不是同一个 object。

简单记：

```text
== → value 相不相同
is → 是不是同一个 object
```

---

# 4. Tuple | 元组

Tuple 是：

> Ordered and Immutable

也就是：

- 有顺序
- 不可修改

创建 tuple：

```python
data = (1, 2, 3)
```

也可以混合不同类型：

```python
student = ("Yang", 22, "Data Science")
```

---

## 4.1 Tuple Indexing

和 string 类似：

```python
student = ("Yang", 22, "Data Science")

print(student[0])
print(student[1])
```

输出：

```text
Yang
22
```

---

## 4.2 Tuple Slicing

```python
data = (1, 2, 3, 4)

print(data[1:3])
```

输出：

```text
(2, 3)
```

---

## 4.3 Tuple is Immutable

不能直接修改其中一个元素：

```python
data = (1, 2, 3)

data[0] = 10
```

会报错。

因为 tuple 是 immutable。

---

# 5. Tuple Unpacking | 元组解包

如果 tuple 中有多个元素，可以直接放入多个变量：

```python
student = ("Yang", 22, "Data Science")

name, age, major = student
```

相当于：

```text
name = "Yang"
age = 22
major = "Data Science"
```

所以看到：

> 把 tuple 中的值分别保存进变量

应该想到：

```text
unpacking
```

---

# 6. Nested Unpacking | 嵌套解包

例如：

```python
studentData = (
    "John Smith",
    11743,
    ("Computer Science", "Mathematics")
)
```

可以：

```python
name, student_id, (major, minor) = studentData
```

得到：

```text
name
student_id
major
minor
```

---

# 7. List | 列表

List 是：

> Ordered and Mutable

也就是：

- 有顺序
- 可以修改

创建：

```python
numbers = [1, 2, 3]
```

---

# 8. List Mutation | 修改列表

因为 list 是 mutable：

```python
numbers = [10, 20, 30]

numbers[0] = 100
```

现在：

```python
[100, 20, 30]
```

---

# 9. `.append()`

在 list **末尾加入一个元素**：

```python
names = ["Amy", "Bob"]

names.append("Jack")
```

结果：

```python
["Amy", "Bob", "Jack"]
```

记忆：

```text
末尾加入一个元素
→ append()
```

---

# 10. `.extend()`

把另一个 iterable 中的元素加入当前 list：

```python
a = [1, 2]
b = [3, 4]

a.extend(b)
```

结果：

```python
[1, 2, 3, 4]
```

区别：

```text
append(x)
→ 把 x 当成一个完整元素加入

extend(x)
→ 把 x 里面的元素一个一个加入
```

---

# 11. List Concatenation `+`

```python
a = [1, 2]
b = [3, 4]

c = a + b
```

得到：

```python
[1, 2, 3, 4]
```

`+` 会产生新的 list。

---

# 12. Removing Elements

## `.remove()`

根据 **value** 删除：

```python
numbers = [1, 2, 3]

numbers.remove(2)
```

变成：

```python
[1, 3]
```

---

## `.pop()`

删除某个 index 的元素，并返回这个元素：

```python
numbers.pop(0)
```

---

## `del`

```python
del numbers[0]
```

也是通过 index 删除。

---

# 13. Sorting Lists

## `sorted()`

```python
numbers = [3, 1, 2]

new_numbers = sorted(numbers)
```

不会修改原始 list。

---

## `.sort()`

```python
numbers.sort()
```

直接修改原始 list。

---

## `.reverse()`

```python
numbers.reverse()
```

直接修改原始 list 顺序。

---

# 14. Mutation Side Effect

List 是 mutable，因此多个变量可能指向同一个 list。

修改其中一个可能影响另一个。

所以：

> 修改 list 时需要注意 side effects。

特别重要：

## 不建议一边遍历 list，一边修改同一个 list

例如：

```python
for number in numbers:
    numbers.remove(number)
```

可能产生意外结果。

更安全的方法：

```python
numbers_copy = numbers[:]

for number in numbers_copy:
    if condition:
        numbers.remove(number)
```

原则：

```text
遍历 copy
修改 original
```

---

# 15. Dictionary | 字典

Dictionary 使用：

```text
key : value
```

保存数据。

例如：

```python
student = {
    "name": "Amy",
    "age": 20,
    "score": 85
}
```

Dictionary：

- mutable
- key 必须唯一
- key 必须是 immutable / hashable 类型
- value 可以是各种类型

例如 value 可以是：

```python
{
    "name": "Amy",
    "scores": [85, 90]
}
```

这里：

```text
"name"   → key
"Amy"    → value

"scores" → key
[85, 90] → value
```

---

# 16. Access Dictionary Value

通过 key：

```python
student["name"]
```

得到：

```text
Amy
```

所以：

```text
知道具体 key
→ dictionary[key]
```

---

# 17. `.get()`

也可以使用：

```python
student.get("name")
```

来获取 value。

---

# 18. `.keys()`

只需要所有 keys：

```python
student.keys()
```

例如：

```python
for key in student.keys():
    print(key)
```

记忆：

```text
只需要 key
→ .keys()
```

---

# 19. `.values()`

只需要 values：

```python
student.values()
```

例如：

```python
for value in student.values():
    print(value)
```

记忆：

```text
只需要 value
→ .values()
```

---

# 20. `.items()`

同时需要：

```text
key + value
```

使用：

```python
.items()
```

例如：

```python
scores = {
    "Amy": 85,
    "Bob": 72,
    "Jack": 90
}

for name, score in scores.items():
    print(name, score)
```

每一轮类似：

```text
name = "Amy"
score = 85
```

然后：

```text
name = "Bob"
score = 72
```

---

# 21. keys / values / items

非常重要：

```text
只要 key
→ .keys()

只要 value
→ .values()

key + value 都要
→ .items()
```

例如：

题目：

> 打印所有分数

用：

```python
for score in scores.values():
    print(score)
```

题目：

> 打印学生和分数

用：

```python
for name, score in scores.items():
    print(name, score)
```

---

# 22. Membership | `in`

检查某个元素是否存在：

```python
if "score" in student:
    print("Found")
```

Dictionary 默认检查 key。

所以：

```python
"score" in student
```

是在判断 `"score"` 是不是一个 key。

---

## 判断 value

如果要检查 value：

```python
if 90 in scores.values():
    print("Found")
```

记忆：

```text
是否存在
→ in

是否不存在
→ not in
```

---

# 23. Dictionary + List

Dictionary 的 value 可以是 list：

```python
students = {
    "Amy": [85, 90],
    "Bob": [70, 75],
    "Jack": [88, 92]
}
```

使用：

```python
for name, scores in students.items():
    print(name, scores)
```

第一轮：

```text
name = "Amy"
scores = [85, 90]
```

所以 `.items()` 已经同时取出了：

```text
key + value
```

这里不需要再使用 `.values()`。

---

# 24. Dictionary + `for` + `if`

例如：

```python
scores = {
    "Amy": 85,
    "Bob": 72,
    "Jack": 90
}
```

找出大于 80 分的学生：

```python
for name, score in scores.items():
    if score > 80:
        print(name)
```

逻辑：

```text
需要 name + score
→ items()

每个学生都要处理
→ for

筛选 score > 80
→ if
```

---

# 25. Filtering + Collecting

非常常见的结构：

```python
result = []

for element in data:
    if condition:
        result.append(element)
```

例如：

```python
numbers = [3, 8, 12, 5, 20]

result = []

for number in numbers:
    if number > 10:
        result.append(number)
```

结果：

```python
[12, 20]
```

所以看到：

> 筛选符合条件的元素，然后保存起来

想到：

```text
list
+ for
+ if
+ append()
```

---

# 26. Set | 集合

Set 的特点：

- unordered
- unique / distinct elements
- 不保存重复元素

例如：

```python
numbers = [1, 2, 2, 3, 3, 3]

unique_numbers = set(numbers)
```

得到：

```python
{1, 2, 3}
```

所以：

```text
去重
→ set()
```

---

# 27. Set Intersection `&`

找两个 set 都有的元素：

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a & b)
```

得到：

```python
{3, 4}
```

记忆：

```text
共同元素
→ &
```

---

# 28. Set Difference `-`

找：

> a 中有，但是 b 中没有

```python
a - b
```

例如：

```python
{1, 2, 3, 4} - {3, 4, 5, 6}
```

得到：

```python
{1, 2}
```

记忆：

```text
左边有、右边没有
→ -
```

---

# 29. Other Set Operations

Union：

```python
a | b
```

表示两个 set 中所有元素。

Symmetric Difference：

```python
a ^ b
```

表示：

> 在其中一个 set 中，但不同时存在于两个 set 中。

---

# 30. `zip()`

`zip()` 用来把多个 sequence **相同位置的元素配起来**。

例如：

```python
names = ["Amy", "Bob", "Jack"]
scores = [85, 72, 90]

zipped = zip(names, scores)
```

会配成：

```text
("Amy", 85)
("Bob", 72)
("Jack", 90)
```

所以看到：

```text
对应位置
```

想到：

```python
zip()
```

---

# 31. `zip()` Stops at the Shortest Iterable

例如：

```python
a = ["a", "b", "c", "d"]
b = [1, 2, 3]
```

```python
list(zip(a, b))
```

结果：

```python
[
    ("a", 1),
    ("b", 2),
    ("c", 3)
]
```

因为 `b` 比较短。

---

# 32. `enumerate()`

如果需要同时得到：

```text
index + value
```

使用：

```python
enumerate()
```

例如：

```python
numbers = [10, 20, 30]

for index, value in enumerate(numbers):
    print(index, value)
```

结果：

```text
0 10
1 20
2 30
```

所以：

```text
dictionary：
key + value
→ .items()

list / tuple：
index + value
→ enumerate()
```

这是今天容易混淆的一个点。

---

# 33. `for` Loop Revisited

`for` 的作用可以理解成：

> 一个一个遍历 iterable 中的元素。

例如：

```python
numbers = [10, 20, 30]

for number in numbers:
    print(number)
```

执行过程：

```text
第 1 轮
number = 10

第 2 轮
number = 20

第 3 轮
number = 30
```

`number` 是 loop variable。

---

# 34. `for` + `if`

非常常见：

```python
for number in numbers:
    if number > 10:
        print(number)
```

可以理解成：

```text
for
→ 一个一个拿

if
→ 对当前拿到的元素进行判断
```

---

# 35. `for person, animal in dictionary.items()`

例如：

```python
fav_animals = {
    "Jack": "dog",
    "Ayush": "dog"
}
```

写：

```python
for person, animal in fav_animals.items():
```

第一轮：

```text
person = "Jack"
animal = "dog"
```

第二轮：

```text
person = "Ayush"
animal = "dog"
```

这里是：

```text
items()
→ 提供 key-value pair

for
→ 一对一对遍历

person, animal
→ unpacking
```

---

# 36. Flipping a Dictionary

原始：

```python
{
    "Jack": "dog",
    "Ayush": "dog"
}
```

希望得到：

```python
{
    "dog": ["Jack", "Ayush"]
}
```

基本结构：

```python
flipped = {}

for person, animal in fav_animals.items():

    if animal not in flipped:
        flipped[animal] = []

    flipped[animal].append(person)
```

理解：

```text
items()
→ 每轮得到 person + animal

if animal not in flipped
→ 第一次遇到这个 animal

flipped[animal] = []
→ 创建一个空 list

append(person)
→ 把这个人加入对应 animal 的 list
```

例如：

```text
Jack + dog
```

第一次遇到 dog：

```python
"dog": []
```

然后：

```python
"dog": ["Jack"]
```

第二次：

```text
Ayush + dog
```

dog 已经存在，所以不重新创建 list。

直接：

```python
"dog": ["Jack", "Ayush"]
```

---

# 37. `.split()` + Dictionary Word Count

例如：

```python
sentence = input("Enter sentence: ")

words = sentence.split()
```

`.split()` 把句子拆成多个单词。

然后可以使用 dictionary 统计：

```python
word_count = {}

for word in words:

    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
```

核心逻辑：

```text
第一次出现
→ 创建 key
→ count = 1

再次出现
→ count += 1
```

---

# 38. Element-wise Tuple Sum

例如：

```python
x = (1, 2, 3, 4)
y = (3, 5, 2, 1)
z = (2, 2, 3, 1)
```

希望：

```python
(6, 9, 8, 6)
```

可以先：

```python
zip(x, y, z)
```

得到：

```text
(1, 3, 2)
(2, 5, 2)
(3, 2, 3)
(4, 1, 1)
```

再使用：

```python
sum(group)
```

---

# 39. How to Recognise What Tool to Use
# 看到题目怎么想到指令

这是今天复习最重要的部分。

```text
“每一个”
→ for

“如果”
→ if

“是否存在”
→ in

“不存在”
→ not in

“末尾加入一个元素”
→ append()

“只要 dictionary key”
→ keys()

“只要 dictionary value”
→ values()

“dictionary key + value”
→ items()

“根据具体 key 找 value”
→ dict[key]

“去重”
→ set()

“共同元素”
→ &

“左边有、右边没有”
→ -

“对应位置”
→ zip()

“index + value”
→ enumerate()

“拆 tuple”
→ unpacking

“筛选并保存”
→ for + if + append()
```

---

# 40. Problem-Solving Process | 做题思路

现在做题不要首先尝试回忆完整代码。

先回答下面几个问题：

```text
1. 数据是什么类型？

list?
tuple?
dictionary?
set?

↓

2. 我要处理每一个元素吗？

Yes
→ for

↓

3. 我要判断条件吗？

Yes
→ if

↓

4. 我要从 dictionary 得到什么？

key
→ keys()

value
→ values()

key + value
→ items()

↓

5. 我要保存筛选结果吗？

Yes
→ 创建 empty list
→ append()
```

例如：

题目：

> 把分数大于 80 的学生名字加入新的 list。

思考：

```text
students 是 dictionary

需要学生名字 + score
→ items()

每个人都要检查
→ for

score > 80
→ if

符合条件的名字需要保存
→ empty list + append()
```

最后才写代码：

```python
result = []

for name, score in students.items():
    if score > 80:
        result.append(name)
```

---

# 41. Important Distinctions | 容易混淆

## `.items()` vs `.values()`

```text
只要分数
→ values()

需要名字 + 分数
→ items()
```

---

## `.items()` vs `enumerate()`

```text
dictionary key + value
→ items()

sequence index + value
→ enumerate()
```

---

## Tuple vs List vs Set vs Dictionary

```python
[1, 2, 3]
# list

(1, 2, 3)
# tuple

{1, 2, 3}
# set

{"a": 1, "b": 2}
# dictionary
```

---

# 42. Current Understanding | 当前掌握情况

目前已经能够理解：

- Tuple 不可修改
- List 可以修改
- Dictionary 使用 key:value
- Set 自动去重
- `for` 用来遍历
- `if` 用来判断
- `append()` 添加元素
- `items()` 获取 key + value
- `values()` 获取 values
- `keys()` 获取 keys
- `set()` 去重
- `&` 求共同元素
- `-` 求差集
- `zip()` 配对对应位置
- `enumerate()` 得到 index + value
- Tuple unpacking
- `for + if + append()` 筛选并保存结果

目前需要继续强化的是：

```text
题目描述
↓
判断数据结构
↓
判断需要什么信息
↓
快速选择正确 method
↓
将多个工具组合
```

尤其需要继续区分：

```text
.keys()
.values()
.items()
enumerate()
```

---

# 43. Week 03 Summary | 第三周总结

本周可以概括为：

```text
Objects
↓
Tuple
↓
List
↓
Mutation
↓
Dictionary
↓
Set
↓
Unpacking
↓
Zip / Enumerate
↓
for + if
↓
Compound Data Types + Looping
↓
Problem Solving
```

本周真正的核心不是单独背：

```python
.append()
.items()
.values()
zip()
```

而是学会：

> 根据数据结构和实际需求选择正确的 Python 工具。

例如：

```text
筛选 list
→ for + if

筛选后保存
→ for + if + append()

处理 dictionary 的 key 和 value
→ items() + for

检查某个 value
→ values() + in

寻找共同元素
→ set() + &

多个序列对应配对
→ zip()
```

---

# 44. Next Session | 下一节

下一节 Lecture：

**Functions and Modules**

也就是开始学习如何把代码组织成可以重复使用的 function。

```python
def function_name(...):
    ...
```

从这一周：

```text
如何组织数据
```

逐渐进入：

```text
如何组织代码
```
