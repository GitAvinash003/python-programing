#Q.1.calculate and display tha area of  respective figure
print("n=1 for ar.circle,n=2 for rectangle,n=3 for triangle ")
n=int(input("enter the value of n" ))
if n==1:
   print("you chooce circle")
   r=int(input('enter the value of radius' ))
   area=3.14*r**2
elif n==2:
    print("you choose rectangle")
    l=int(input('enter the length value ' ))
    w=int(input('enter the width value '))
    area=l*w
else:
    print("you choose triangle")
    b=int(input('enter the base value'))
    h=int(input('enter the height value')) 
    area=1/2*b*h

print(area)


#Q2.check whether a triangle formed or not

sum=0
for i in range(3):
    n=int(input("input values:-"))
    sum+=n
if sum==180:
    print("yes:-)")
else:
    print("no:-(")

#Q3.find smallest no. i.e-greater or equal to n & also power of 2

n=int(input("enter the no.:"))
p=1
while n>p:
    p=p*2
print(p) 

#Q4.convert n into binary number

n=int(input("enter value of n:-"))
while n>0:
     r=n%2
     print(r,end="")
     n=n//2


    

