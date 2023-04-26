n=int(input("enter your number:"))
for i in range(1,n+1):
    print("*"*i)
'''
 output
*
**
***
****
*****'''
#inverse of above 
n=int(input("enter your number:"))
for i in range(n,0,-1):
     print("*"*i)
'''
#output
*****
****
***
**
*
'''

n=int(input("enter your number:"))
for i in range(1,n+1):
    print(" "*(n-i)+"*"*i)
'''
    *
   **
  ***
 ****
*****'''
#n =int(input("enter your number:"))
for i in range(1,6):
    print(' '*(5-i)+'*'*(2*i-1) )
    '''
  output
    *
   ***
  *****
 *******
********* '''
#square pattern

n=5
for i in range(1,n+1):
    print("*"*5)
'''    
*****
*****
*****
*****
***** '''
# hollow square pattern

n=5
for i in range (1,6):
   if i==1 or i==5:
    print("*"*5)
   else:
     print("*"+" "*(5-2)+"*" )
'''
#output
*****
*   *
*   *
*   *
***** '''  
#print number

row=6
for num in range(row):
     for i in range(num):
         print(num,end=" ")
     print(" ")
'''
1  
2 2
3 3 3
4 4 4 4
5 5 5 5 5'''
#inverted

row=5
b=0
for i in range(row,0,-1):
    b+=1
    for j in range(1,i+1):
        print(b,end=' ')
    print('\r') 
'''    
1 1 1 1 1 
2 2 2 2 
3 3 3
4 4
5
    '''

n=7
for i in range(1,n+1):
  print(" "*(7-i)+"*"*i)
    
'''
      *
    **
     ***

    *****

   *******

  *********

 ***********
*************
 '''

n=5
for i in range(1,6):
  print('*'*i+" "*(5-i)*2+'*'*i)
'''  
*        *
**      **
***    ***
****  ****
**********
'''