for num in range (1,10):
    if num>1:
        for i in range(2,num):
            if num%i == 0:
                print(num)
        else:
            print(num)