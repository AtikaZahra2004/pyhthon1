#dictionary method-------
#  1.copy()-------new object bnane k liye(create new obj)
#  2.clear() --------remove all pairs from dictionary
#  3.pop() -----------remove targetd key from dic
#  4.popitems()---------remove last pair/item from dict
#  5.get()--------------get value of targeted key
#  6.keys() -----------collect all key from dict in form of list
#  7.values()-----------'''''''''values'''''''''''
#  8.items()------------''''''''items(key.value)''''''''
#  9.formkey()-----------create newdict on the basis of given collection elemnt
#  10.setdefault()
#  11. update()

#dictionry------collection of key value pairs
#where key and value supported , 
#  reperented in {} with comma seprated pairs ,
#  indexing supported  ,,
#  slicing not supported,
#  maped data type,
#  key must be unique,
#  value may be duplicate,
#  mutable in nature

#d={'name':'atika' ,'age':20,'course':'bsc'}
d={'x':10,'y':20,'z':30}
print(d)
print(type(d))
print(id(d))
#inbulit function
#print(max(d))----value ko
#print(min(d))---key k dekhaega
#print(sum(d))----error
#print(len(d))
#print(type(d))
#print(id(d))

#COPY
d1=d.copy()
print(d,d1)
print(id(d),id(d1))

#CLEAR
d1.clear()
print(d,d1)
print(id(d),id(d1))
del d1   #mermory relize
#print(d1)

#POP
#d.pop('x')
#print(d)

#POPITEM
#d.popitem()
#print(d)

#GET
#new=d.get('x')
#print(new)
#print(d.get('x'))

#KEY
print(d.keys())

#VALUES
print(d.values())

#ITMES
print(d.items())

#FROMSKEYS
s='atika'
d=dict.fromkeys(s)  #none btayea
print(d)


#SETDEFAULT
d.setdefault('x',50)
print(d)


#DEFAULT
d1={'p':2,'q':3}
d.update(d1)
print(d)


#CRETAE
a={}
print(type(a))
a['key']='value'
print(a)
#UPDATE
a['key']='newvalue'
print(a)
#GET/READ
x=a['key']
print(x)
#delete
a.pop('key')
print(a)