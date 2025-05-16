'''name=input('enter your name :')
print( 'welcome', name)'''


'''val=input('enter some value')
print(type(val),val)'''


'''name=input('enter name')
age=int(input('enter age'))
marks=float(input('enter marks'))

print(name,age,marks)'''


'''f1=int(input('enter first number'))
f2=int(input('enter secon number'))
sum=f1+f2
print(sum)'''

'''s=float(input('enter side of sqr'))
print(s*s)'''


'''fl=float(input('enter flotin one:='))
fll=float(input('enter another fp:'))
print((fl+fll)/2)'''

'''srt='atika'
str='zahra'
print(str+ " "+ srt)
print(len(str))'''

'''str='atika zhara'
print(str[3])'''


'''slicing'''
'''str='atika zahra'
print(str[-3:-1])'''


#ENDSWITH------true/flase
"""str='i am student of pyhton'
print(str.endswith('ton'))"""


#CAPITALIZE
"""str='i am student of pyhton'
print(str.capitalize())"""

#REPLACE
"""str='i am student of pyhton'
print(str.replace('of','php'))"""

#FIND
"""str='i am student of pyhton'
print(str.find('i'))"""

#COUNT
"""str='i am  of student of pyhton'
print(str.count('o'))"""


"""s=str(input('enter your first name'))
print(s)
print(len(s))"""

#CONDITIONAL
"""age=20
if(age>12):
    print('this apply for vote')"""
"""
n=int(input('enter any  number :'))
if(n%2==0):
    print('even number')
else:
    print('odd number')"""


"""n=int(input('enter number'))
if(n%7==0):
    print('mutliple of 7')
else:
    print('invalid')"""


#LIST

#APPEND----ADD ELEMNT
list=[1,2,3,4]
print(list.append(5))
print(list)

#SORT-----ACCENDING
listt=[4,2,5,1,6]
print(listt.sort())
print(listt)

#REVERSE----revese the elemnt
lisst=['atika','zahra','khan']
print(lisst.reverse())
print(lisst)

#INSORT---insort elmet at index

#POP
list=[2,3,4,1,2]
list.pop(3)
print(list)


#TUPLE
tup=(2,1,3,1)
print(tup.index(3)) #index
print(tup.count(3))  #count

#QUESTION
moveis=[]
m=str(input('first movei'))
m1=str(input('second move'))
m2=str(input('third movei'))
moveis.append(m)
moveis.append(m1)
moveis.append(m2)
print(moveis)


s = {10, 20, 30}
item = s.pop()
print(item)      # Output: random (e.g., 10)
print(s)         # Remaining items
