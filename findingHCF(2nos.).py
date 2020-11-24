''' finding hcf'''

smaller = int(input("enter a number: "))
greater = int(input("enter a number: "))
if smaller > greater:
    smaller,greater = greater, smaller
hcf = 1
for i in range(1, smaller+1):
    if smaller%i == 0 and greater%i == 0:
        hcf = i

print("hcf is",hcf)
