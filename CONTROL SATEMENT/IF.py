
#IF
'''n=int(input('enter any num'))
if n%2==0:
    print(f'given num {n} is even')#fstring
    print('even num')'''


#IF-ELSE

'''n=int(input('enter any num'))
if n%2==0:
    print(f'given num {n} is even')#fstring
else:
    print(f'given num {n} is odd')'''

# IF-ELIF
'''n=int(input('enter any num'))
n1=int(input('enter any num'))
n2=int(input('enter any num'))
if n>n1 and n>n2:
    print(f'{n} is grater than {n1} and{n2}')#fstring
elif n1>n and n1>n2:
    print(f'{n1} is grater than {n} and{n2}')
elif n2>n and n2>n1:
    print(f'{n2} is grater than {n} and{n1}')
else:
    print('invalid')'''


#QUESTUON
'''num=int(input('enter year :'))
if num%400==0:
    print('leap year ',num)
elif num%4==0:
    print('leap year ', num) 
else:
    print('not leap year')   '''

#--------------OR------
'''y=int(input('enter year :'))
if (y%4==0 and y%100!=0):
    print('leap year')
#----------------or---
if(y%4==0 and y%100!=0 or y%400==0):
    print('leap year')'''


#QUESTION
'''h=int(input("enter hindi marks :-"))
e=int(input("enter hindi marks :-"))
m=int(input("enter hindi marks :-"))

if h>=0 and h<=100 and e>=0 and e<=100 and m>=0 and m<=100:
  avg=(h+e+m)/3
if avg>60:
    print('first division')
elif avg>=45 and avg<=59:
    print('second division')
elif avg>=35 and avg<=44:
    print('third division')

else:
    print('fail')'''

#QUESTIONS


n=eval(input('enter any value'))
if int(n)==int:
    print('integer value ',{n})
elif str(n)==str:
    print('string value' ,{n})   
