name = input("Enter your name")
print(name)


print("What is your name?")
name = input()
print(name)


x = input("Enter a number: ")
print(type(x))


x = int(input("Enter a number: "))
print(type(x))


x = 5
print("The number is " + str(x))

one = 1
two = 2
three = one + two
print(three)


hello = "hello"
world = "world"
helloword = hello + " " + world
print(helloworld)

one = 1
two = 2
hello = "hello"
print(one + two + hello)


number = 1 + 2 * 3 / 4.0
print(number)
print(type(number))


remainder = 11 % 3
print(remainder)


# Exercise 1

weight = float(input("Please Enter your weight: "))
height = float(input("Please Enter your height: "))

bmi = weight / height * 2
print("your BMI is  " +str(bmi) )


# Exercise 2


x = int(input("Please Enter a integer: "))
y = int(input("please Enter a integer: "))


result = (x + y) * (x + y)

print("your result is  "+ str(result))


# Exercise 3
start_time = 8
past_time = 9

now_time = (start_time + past_time) % 12
print("now time is  " + str(now_time) + " pm")


name = input(print("please Enter your name:  "))
print("Hello " + name + "," + "would you like to learn some Python today?" )


# Exercise 4

first_name = input(print("Please Enter your first name: "))
last_name = input(print("Please Enter your last name: "))

print("welcome"+ " " + last_name + " " +  first_name + "!" )


# challenge yourself
# 1
n = input("Please Enter a integer: ")
nn = n * 2
nnn = n * 3 
result = int(n) + int(nn) + int(nnn) 
print(result)

# 2
number = int(input("Please Enter an integer: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
    
    
# 3
num = int(input("Enter a 4-digit integer: "))

d1 = num // 1000
d2 = (num // 100) % 10
d3 = (num // 10) % 10
d4 = num % 10

sum_digits = d1 + d2 + d3 + d4

print("Sum of digits =", sum_digits)

   
 