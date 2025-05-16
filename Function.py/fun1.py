#avoid same loop repetation
#write once call multiple
#code resuability


#type---inbuilt,userdefined
#inbuilt function=print(),type(),max(),min(),id(),len()

#userdefined---declartion,calling

#1.DECLARATION
#syntax-----
#def fun-name(parameters):
#      |used variable are declared as a parameter
#      | perfoem operation,return
# fun-name(arguments)



'''def hello():
    return ''        #'' denge tuo blank ayega ,return lekhrnge tuo none btayega, string likeng tuo string btega
print(hello())

def hello():
    print('hello')
hello()    

def hello():
    print('hello')
x=hello()
print(x)


def hello():
    return 'hello'
x=hello()
print(x)


#natural number
def natrualno(n):
    for i in range(1,n+1):
        print(i)
x=int(input('enter natural num'))
natrualno(x)




#even
def evenno(n):
    for i in range(1,n+1):
        if i%2==0:
            print(i)
x=int(input('enter even num'))
evenno(x)


#odd
def oddno(n):
    for i in range(1,n+1):
        if i%2!=0:
            print(i)
x=int(input('enter even num'))
oddno(x)

#sum of natural number
def ns(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    return sum
n=int(input('enter even num'))   
totalsum=ns(n) 
print(totalsum)

#sum of even no
def sumofeven(n):
    sum=0
    for i in range(2,n+1,2):
        sum=sum+i
    return sum
    
n=int(input('enter even num'))   
totalsum=sumofeven(n) 
print(totalsum)


#sum of odd no
def sumofodd(n):
    sum=0
    for i in range(2,n+1,2):
        sum=sum+i
    return sum
    
n=int(input('enter even num'))   
totalsum=sumofodd(n) 
print(totalsum)

#factorial of any number
def factorial(n):
    result=1
    for i in range(1,n+1):
        result=result*i
    return result
print(factorial(5))


#factor of any number
def find_factor(n):
    factors=[]
    for i in range(1,n+1):
        if n%i==0:
            factors.append(i)
    return factors

# n=int(input('enter any number'))
# print('factor of',n,"are",find_factor(n))
#--------OR----------
def factors(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i)
n=int(input('enter any num'))
print('factor of',n,'are',factors(n))'''


#FIBONACCHI SERIES
def fibonacchi(n):
    a,b=0,1
    for i in range(n):
        print(a)
        a,b=b,a+b
n=int(input('enter any num'))   
fibonacchi(n)     


#armstrong
