def Push(x, stack1, stack2):
    '''
    x: value to push
    stack1: list
    stack2: list
    '''
    stack1.append(x)

    # code here


def Pop(stack1, stack2):
    '''
    stack1: list
    stack2: list
    '''
    if len(stack1) == 0:
        return -1
    else:
        for i in range(len(stack1)):
            stack2.append(stack1.pop())
        k = stack2.pop()
        for j in range(len(stack2)):
            stack1.append(stack2.pop())
    return k

    # code heredef Push(x,stack1,stack2):
    #     '''
    #     x: value to push
    #     stack1: list
    #     stack2: list
    #     '''
    #     stack1.append(x)
    #
    #     #code here
    #
    # def Pop(stack1,stack2):
    #
    #     '''
    #     stack1: list
    #     stack2: list
    #     '''
    #     if len(stack1)==0:
    #         return -1
    #     else:
    #         for i in range(len(stack1)):
    #             stack2.append(stack1.pop())
    #         k=stack2.pop()
    #         for j in range(len(stack2)):
    #             stack1.append(stack2.pop())
    #     return k
    #
    #     #code here