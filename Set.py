#SET---------COLLECTION OF UNIQUE ELEMENT-------HOMOGENOUS,HETROGENOUS
#UNORDERD COLLECTION
#INDEXING NOT SUPPORT
#SLICING NOT SUPPORTED
#MUTABLE IN NATURE
#REPERSNTED IN{} WITH COMMA SEPERATED ELEMNT


#EXMPLE
s={10,20,30,40,10,'atika','zahra','khan'}
s1={'pyhton','java','php'}
print(s)
print(type(s))
print(id(s))


#PYHTON INBUILT FUNCTION FOR SETS
#len()
#max()---eror
#min()---erro
#sum()---err
#type()
#id()

print(len(s))
#print(max(s))
#print(min(s))
#print(sum(s))
print(max(s1))
print(min(s1))
s2={12,34,54,56}
print(sum(s2))


#METHOD
#add() ---rondom elemnt ko upd
# update() ----multiple elemt ko add 
# pop() ----kese ek elemnt k htana
#   remove() ---elemnt ko pss krke 
#  discard() 
#  copy()  
# clear()

#methametical operation-----------
#create new set------union() intersection() differnce()  symmetric-differnce()
#update exixtinfg set-----intersecton-update()  differnce-update()   symmetric-differnce-update()
# isdisjoint(),issuperset(),issubset()


s3={10,20,'atika','khan'}
s3.add('php')
print(s3)

#update
s3.update('php','da')
print(s3)


#POP-----remove randomly elemnt
print(s3.pop())
print(s3)

#REMOVE
s3.remove(10)
print(s3)

#DISCARD
s3.discard('d')
print(s3)

#copy

s4=s3.copy()
print(id(s4),id(s3))

#clear
s3.clear()
print(s3)