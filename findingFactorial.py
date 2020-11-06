def factorial(num):
      if num == 1:
            return num
      else:
            result = num * factorial(num-1)
            return result

num = int(input("Enter number to find factorial: "))
print("factorial of",num,"is",factorial(num))