#while loop practice
n=64
p=1
while n>p:
    p=p*2
print(p)

#Armstrong number

s=0
n=int(input("enter your number"))
c=n
p=len(str(n))
while n>0:
    r=n%10
    s=s+r**3
    n=n//10

if c==s:
     print(" is a armstong number")
else:
        print("not an armstrong")
        

#prime number
#print square of first 10 integer

n=int(input("enter your number"))
  

num=1
while num<=10:
    print(num**2)
    num=num+1

#while loop print series

def fizzBuzz(n):
    # Write your code here
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            print("Fizzbuzz")
        elif i%3==0 and i%5!=0:
            print("fizz")
        elif i%5==0 and i%3!=0:
            print("Buzz")
        else:
            print(i)



