'''lopping ko iteration krne k liye
1.for--finite iteraation
2.while--infinite iteration
    while--
    1.define statr point
    2.check condtion
    3.if conditon true then while stemnt excute'''
#########
'''count=1
while count<=5:
    print('hello')
    count += 1'''
#NATURAL NUMBER
n=int(input('enter any number'))
i=1
while i<=n:
    print(i)
    i=i+1

###COLUMN----
'''n=int(input('enter any number'))
i=1
while i<=n:
   if i<=(n-1):
       print(i,end=',')
   else:
       print(i)  
   i=i+1  '''
#------------column +
'''n=int(input('enter any number'))
i=1
while i<=n:
   if i<=(n-1):
       print(i,end='+')
   else:
       print(i)  
   i=i+1  '''


#--------sum---------------
n=int(input('enter any number'))
i=1
sum=0
while i<=n:
   sum=sum+i
   if i<=(n-1):
       print(i,end='+')
   else:
       print(i)  
   i=i+1  
print(sum)   
#-----------------multiplication----------------
n=int(input('enter any number'))
i=1
multi=1
while i<=n:
   multi=multi*i
   if i<=(n-1):
       print(i,end='*')
   else:
       print(i)  
   i=i+1  
print(multi)   


#------------factorial-----------
n=int(input('enter any num'))
x=n
fact=1
while n>0:
    fact=fact*n
    n=n-1
print(f'factorial of given number {x} is{fact}')


# WAP to print n even natural numbers and their sum using while loop

n = int(input("Enter the value of n: "))
i=1
while i<=n:
    print(2*i)
    i=i+1




















#INBUILT PRINT()
print(sep='' ,end='\n')
print('hello' , end=',')
print('welcome')
###
x=10
y=20
print(x,y)
print(x,y,sep=',')



