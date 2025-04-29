#global 
x='awsome' #yh x bhar hai hai tuo global variable

def myfunc():
    print('pyhton is' + x)
    myfunc()


    #local
    x='atika'
    def myfunc():
        x='zahra' #yeh x under hai tuo local 
        print('my name is' + x)
        myfunc()