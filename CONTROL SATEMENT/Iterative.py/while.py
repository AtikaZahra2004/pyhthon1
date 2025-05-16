#WAP TO PRINT 5DIGIT FABONACHI SERIES
'''n=int(input('enter a number'))
x,y,i=0,1,1
while i<=n:
    z=x+y
    if i<n:
        print(z,end=',') 
    else:
        print(z)
    x,y=y,z
    i=i+1       '''

#WAP TO CHECK GIVEN NO IS ARMSTRONG OR NOT
'''n=int(input('enter a num'))
x=y=n
digit=0
sum=0
while n>0:
    digit =digit+1
    n=n//10
print(digit)
print(n)

while x>0:
    last_digit=x%10
    sum=sum+last_digit**digit
    x=x//10
print(sum)
print(x)

if y==sum:
    print(f'given no {y} is armstrong')
else:
    print(f'given no {y} is not armstrong')    '''

#PALLINDROM REVERSE WALAA STRING KA
s='pyhton'
l=len(s)
s1=''
i=-1
while l>0:
    x=s[i]
    s1=' '.join((s1,x))
    i=i-1
    l=l-1
print(s1)    
if s==s1:
    print(f'given number {s} is pallindrom')
else:
    print(f'given number {s} is  not pallindrom') 

# wap to print factorial of any given number
n=int(input("enter a number"))
fact=1

if n<0:
    print('factorial is not define for negative numbers')
else:
    i=1
    while i<=n:
        fact=fact*i
        i=i+1
        print("Factorial of",n,"is",fact) 

#wap to print multiplication of n nutral number
n=int(input('enter a numbers'))
num=1
i=1
while i<=n:
    num=num*i
    if i<=(n-1):
        print(i,end='*')
    else:
        print(i,end='=')
    i=i+1
print("multiplication",n,"natural number is",num)             


