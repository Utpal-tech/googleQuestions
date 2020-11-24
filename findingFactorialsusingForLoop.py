'''factorial'''

num = int(input("enter a number"))
factorial = 1
if num > 1:
    for i in range(num, 1, -1):
        factorial = factorial*i
print(factorial)
