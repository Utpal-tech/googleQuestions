'''lcm'''

smaller = int(input("enter a number: "))
greater = int(input("enter a number: "))
lcm = smaller*greater
for i in range(smaller*greater+1, greater-1, -1):
    if i%smaller == 0 and i%greater == 0:
        lcm = i
print(lcm)
