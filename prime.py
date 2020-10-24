#this program prints prime number in a given interval.
def prime():
    try:
        a = int(input("enter smaller no."))
        b = int(input("enter larger no."))
        for i in range (a,b+1):
            if  i>1:
                for c in range(2,i):
                    if i%c == 0:
                        break
                else:
                    print(i)
        retry()
    except:
        print("try again with correct input")
        retry()
def retry():
    print("do you want to try again\nenter y for yes or any other key to exit")
    choice = input()
    if choice.lower() == "y":
        prime()
    else:
        print("thank you")

        
    
prime()
