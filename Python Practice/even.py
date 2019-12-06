'''
def pal(n):
        if n==n[::-1]:
            print("is a palandrome")
        else:
            print("is not a palandrome")
n=str(input("enter the number"))
pal(n)

def armst(n):
    for i in range(1,n):
        temp=i
        sum=0
        while i!=0:
            rem=i%10
            sum=sum+rem**3
            i=i//10
        if sum==temp:
            print(sum,end=',')
        #else:
            #print(sum,"is not an Armstrong number")
n=int(input("enter number:"))

armst(n)
n=input("enter the range")
def even(n):
    for i in range(0,n):
        if(i%2==0):
            print(i,"is even")
        else:
            print(i,"is odd")
even(int(n))

n=input("enter the range")
def prime(n):
    
    for num in range(1,n+1):
        count=0
        for i in range(1,num+1):
            if num%i==0:
                count=count+1
                #print(num,count)
                
        if count==2:
            print(num,"is prime")
        else:
            print(num,"not a prime")
prime(int(n))

n=input("enter the number")
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i

    print(n,"fact:",fact)
factorial(int(n))


def perfect(n):
    for num in range(1,n):
        sum=0
        for i in range(1,num):
            if num%i==0:
                sum+=i
        if sum==num:
            print(sum,end=',')
        #else:
            #print(sum,"not a perfect number")
n=int(input("enter the range"))
perfect(n)    

def perfect(n):
    sum = 0
    for i in range(1,n):
        if n % i == 0:
            sum += i
            print(i)
    if sum == n:
        print(sum,"perfect numbr")
    else:
        print(sum,"not a perfect number")
            
n=int(input("enter the number"))
perfect(n) 
'''
def check_email_contains(email_address, characters, min_length=6):
    while True:
        for character in characters:
            if character not in email_address:
                email_address = input("Your email address must have '{}' in it\nPlease write your email address again: ".format(character))
                #continue
        if len(email_address) <= min_length:
            email_address = input("Your email address is too short\nPlease write your email address again: ")
            #continue
        return email_address
email_address = check_email_contains(input("What is your email address? "), "@.")



