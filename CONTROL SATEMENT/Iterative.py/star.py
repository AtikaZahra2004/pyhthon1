#1-----------
'''n=int(input('enter any num'))
i=1
while i<=n:
    print('*'*n)
    i=i+1


n=int(input('enter any num'))
i=1
while i<=n:
    print('*'*i)
    i=i+1'''



n=int(input('enter any num'))
i=1
while i<=n:
    print(''*(n-i)+'*'*i)
    i=i+1    

'''n=int(input('enter any num'))
i=0
while i<n:
    print(' '*i+'*'*(n-i))
    i=i+1  


n=int(input('enter any num'))
i=0
while i<n:
    print(' '*i+'* '*(n-i))
    i=i+1  '''

'''n=int(input('enter any num'))            ####
while n>0:                                  ###  
    print('*'*n)                            ##
    n=n-1    '''                            #


'''n=int(input('enter any number'))
i=0                                           ###          
while i<n:                                    ##   
    print('*'*(n-i)+''*i)                     #
    i=i+1                                     ## 
i=i-2                                         ### 
while i>=0:
    print('*'*(n-i)+''*i)
    i=i-1    '''


n=int(input('enter any number'))
i=0                                                     
while i<n:                                       
    print(' '*i+' *'*(n-i))                    
    i=i+1                                      
i=i-2                                         
while i>=0:
    print(' '*i+' *'*(n-i))                     
    i=i-1    