#Write a python program for check whether the number is Prime or not
num=int(input("Enter a Number 0 to 100: "))
if num <= 1:
    print("It is not a prime number")
else:
    for i in range(2,num):
        if num % (i/2)==0:
            print("It is not a prime number")
            break
    else:
        print("It is a prime number")
