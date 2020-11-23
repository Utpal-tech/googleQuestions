a = 0
num = int(input("enter a number"))
for i in range(1, num+1):
    if num%i == 0:
        print(i, "is a factor of", num)
        a = a+1
print("there are",a, "factore of", num)
