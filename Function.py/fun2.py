#reletion between parameter and argument
# 1.positional argument
# 2.keyword argument
# 3.default argument
# 4.variable lenght positional
# def fibo(x,y,z):
#     print('value of x=',x)
#     print('value of y=',y)
#     print('value of z=',z)
#     print(x+y+z)
# p=10
# q=20
# r=30
# fibo(p,q,r)    

#default
# def fibo(x=0,y=0,z=0):
#     print('value of x=',x)
#     print('value of y=',y)
#     print('value of z=',z)
#     print(x+y+z)
# p=10
# q=20
# r=30
# fibo(p,q,r)  
# fibo() 
# fibo(p,q) 

#variable length positional argumnent
# def fibo(*args): #*kess data ko form krega
#     print(args)
#     print(type(args))

# fibo(2,4,6,8,10,20,30)    

#summm--1
# def fibo(*args):
#     sum=0
#     for i in args:
#         sum=sum+i
#     return sum
# x=fibo(2,4,6,8,10)  
# print(x)  

#summ--2
def fibo(*args):
    sum=0
    for i in args:
        for j in i:
            sum=sum+j
    return sum
p=(2,4,6,8,10)
x=fibo(p) 
print(x)  