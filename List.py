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

#dictionry------collection of key value pairs
#where key and value supported , 
#  reperented in {} with comma seprated pairs ,
#  indexing supported  ,,
#  slicing not supported,
#  maped data type,
#  key must be unique,
#  value may be duplicate,
#  mutable in nature

d={'name':'atika' ,'age':20,'course':'bsc'}
print(d)
print(type(d))
print(id(d))
#inbulit function
#print(max(d))----value ko
#print(min(d))---key k dekhaega
#print(sum(d))----error
print(len(d))
print(type(d))
print(id(d))

