def tower_honoi(n,src,dst,hlp):
    if n==0:
        return
    tower_honoi(n-1,src,hlp,dst)
    print('{} [{} ->{}]'.format(n,t1,t2))
    tower_honoi(n-1,hlp,dst,src)


n=int(input("enter the number of disks"))
t1=input("first tower")
t2=input("second tower")
t3=input("third tower")
print(tower_honoi(n,t1,t2,t3))