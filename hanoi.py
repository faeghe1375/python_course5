while(1):
    i=int(input("enter number of disk"))
    def hanoi(disk=1, start='a', temp='b', finish='c' ):
        if disk==1:
            print(start + " go to" + finish)
        else:
            hanoi(disk-1,start,finish,temp)
            print(start + " go to"+ finish)
            hanoi(disk-1 ,temp,start,finish)
    hanoi(i, 'a' , 'b' , 'c')             