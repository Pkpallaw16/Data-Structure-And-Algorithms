def Validate_stack_sequence(pushed,poped):
    i=0
    while len(poped)>0:
        while pushed[i]<poped[0]:
            i+=1
        if pushed[i]>poped[0]:
            print("false")
            return
        if pushed[i]==poped[0]:
            pushed.pop(i),poped.pop(0)
            i-=1
    print("true")
def fun():
    pushed= [1,2,3,4,5]
    poped=[4,3,5,1,2]
    Validate_stack_sequence(pushed,poped)
fun()