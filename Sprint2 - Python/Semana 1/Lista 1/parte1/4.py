for i in range(0,101):
        if i ==2:
            print(i)
        for j in range(2,i):
            if (i%j==0):
                break
            else:
                print(i)
                break
