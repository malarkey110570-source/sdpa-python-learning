# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Write a Python program to calculate the sum of the digits in an integer (of 4 digits).
#写一个程序，计算一个 4 位整数各位数字之和。

number = int(input("Please Enter a four-dugit number")) # 1234

digit1 = number % 10 # 4
number = number // 10 # 123.4 -> 123

digit2 = number % 10 # 3
number = number // 10 # 12.3 -> 12

digit3 = number % 10 # 2
number = number // 10 # 1.2 -> 1

digit4 = number % 10 # 1

result = digit1 + digit2 + digit3 + digit4
print(result)


# 6:52 a.m. 离开家，先以 8:15/mile 跑 1 mile，然后以 7:12/mile 跑 3 miles，再以 8:15/mile 跑 1 mile，问几点回家吃早餐？

easy_pacetime = 8 * 60 + 15
tempo_pacetime = (7 *60 + 12) * 3

total_time = easy_pacetime * 2 + tempo_pacetime
total_time % 60

total_minute = total_time // 60
total_secound = total_time % 60

start_hour = 6
start_minute = 52

final_minute = start_minute + total_minute
final_hours = start_hour + (final_minute // 60)
final_minute2 = final_minute % 60

print(str(final_hours) + ":" + str(final_minute2) + ":" + str(total_secound) + " am")
 