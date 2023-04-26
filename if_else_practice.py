#basics of python 
#q1.
print("enter your first number") 
a=int(input())
print("enter your second number")
b=int(input())
c=a+b
print("addition of a and b is",c )
if c%7==0 :
    print("yes")
else :
    print("no") 

#q2. multiple of five
n=int(input())
if n%5==0 :
   print("hello")
else :
    print("bye")

 #q3.calculate electricity bill

amt=0
print("enter your electricity bill") 
n=int(input())
if n<=100:
    amt =0
if n>100 and n<200:
    amt=(n-100)*5
    print("amount to pay is:",amt)
if n>200:
    amt=500+((n-200)*10)
    print("amount to pay:",amt)  

    #q4.display the last digit of number


print("enter your digit") 
n=int(input())
print("last number is:",n%10)  

#q5.check whether the last diogit of number  is divisible by 3 or not
print("enter your digit") 
n=int(input())
n=n%10
if n%3==0:
    print("yes last digit  is divisible by 3")
else :
    print ("no last digit is not divisible by 3") 
 
 ##PRactice 2
#q7.percentage to grade program

n=int(input())

if n>90:
    print("A")
if n>80 and n<=90:
    print("B")
if n>=60 and n<=80:
    print("C")  
if n<60:
    print("D")  

#q8.cost price of bike and display road tax

tax=0
print("enter the  price of bike")
cost_price=int(input())
if cost_price>100000:
    tax=15/100*cost_price
elif cost_price>50000 and cost_price<=100000:
    tax=10/100*cost_price
else:
    tax=5/100*cost_price
print("tax to be paid is",tax) 

#q9. year is leap or not

print("enter your year")
year=int(input())
if year%100==0:
   if year%400==0 :
    print("it is leap year")
   else:
      print("not a leap year")
   if year%4==0 :
       print("it is a leap year") 
   else:
      print("not a leap year")



       
