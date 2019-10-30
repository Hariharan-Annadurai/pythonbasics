def primeno(n):

    for i in  range(2, n+1):
        if (n==2):
            print('prime')
            #break
        elif(n % i ==0):
            print('not prime')
            #return n
        else:
            print('prime')
    #if(n):
        #print('not prime')
    #else:
        #print('prime')

primeno(10)

