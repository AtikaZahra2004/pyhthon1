#list----coleection of elemnt---1.homogenous(same data type) 2..hetrogenous(diff data type)
#repersented in[] with comma , seprated

#in bulit function for list
#1 len(),max(),min(),type(),id(),sum()

l=[2,1,3,4,8,5] #start with 1
#print(len(l))
#print(max(l))
#print(min(l))
#print(sum(l))
print(type(l))


#LIST METHOD
# append()--add single elemnt in last position.,
# extend()----add multiple elemmnt in last position,
# insert()---add single elemnt in targeted position,
# pop()---remove last elemnt from list
# remove()---remove targeted elemnt from list
# copy()---create new objject with same elemnt
# clear()-----remove all elemnt from list []
# reverse()-----reverse all elemnt from list
# sort()------arrange assending order
# index()---- finding elemnt position
# count()-----calculated props occurance of any elemnt

#l=[2,4,6,8,'pyhton','java']



#28 aprail

#tuple--collection of elemnets-----homogenous--hetrognous
t=(10,20,30,'python','java')
#pyhton inbuilt function for tuple
#len(),max(),min(),sum(),id(),type()
#print(len(t))
#print(max(t))---error
#print(min(t))---error
#print(sum(t))---error
#print(id(t))
#print(type(t))

#methods
#1.index()   2.count()

t=(10,20,30,'pythpon')
print(t.index(30))
print(t.count(20))#---0 btayega tab vho nhi rhega,1 jo available hai

import sys
t=(10,20,30,40)
t1=[10,20,30,40]
print(sys.getsizeof(t))
print(sys.getsizeof(t1))



#append method:---last m 1 elemnt ko add krta 
l=[1,2,3,4,5,6,7]
l.append(10)
print(l)

l=[1,2,3,4,5,6,7]
t1=(20,30)
t2=[50,40]
s='python'
l.extend(t1)
l.extend(t2)
l.extend(s)
print(l)

#EXTEND METHOD---multiple element ko add karta h
l=[1,2,3,4,5]
s1='pyhton'
s2='java'
l.extend(s1)
l.extend(s2)
print(l)

#INSERT METHOD
l=[1,2,3,4,5]
a=[6,7,8,9,0]
a1=['pyhton','java','php']
l.insert(0,'a')
a.insert(10,'a')
a1.insert(5,2)
print(a1)
print(a)