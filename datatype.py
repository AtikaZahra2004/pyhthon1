#numeric

x=2
y=3
print(type(x+y))

x=11.9+2j
y=2.0+3j
z=x+y
print(type(z)) #complex-real+imaginary


#string -----collection of character-------represnt in '' ,"", ''' '''------index suppoterd-----silicing supported-------immutable in nature
#example
s='phton'
print(type(s))
print(id(s))

#string oprtation-----+,*
s1='atika'
s2='zahra'
print(s1+' '+s2)

s1='12'
s2='34'
print(s1+' '+ s2)

# repetation *
s1='sana'
s2=3
print(s1*s2)

#membership operator---
s='pyThon'
print('a' in s)
print('T' in s)

s1='baby'
s2='jhon'
print(s1 is s2)
print(id(s1))
print(id(s2))




