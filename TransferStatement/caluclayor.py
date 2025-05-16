while True:
    print('in1.Add in2.Sub in3.multi in4.div')
    n=int(input('enter any opyion'))
    x=(1,2,3,4)
    if n in x:
        if n==1:
            p=int(input("1st value"))
            q=int(input('2nd value'))
            print(p+q)
        elif n==2:
            p=int(input("1st value"))
            q=int(input('2nd value'))
            print(p-q)
        elif n==3:
            p=int(input("1st value"))
            q=int(input('2nd value'))
            print(p*q)    
        elif n==4:
            print('off')
            break
    else:
        print('please enter valid option')        