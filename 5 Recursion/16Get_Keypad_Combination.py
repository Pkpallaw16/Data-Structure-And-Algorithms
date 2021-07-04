"""1. You are given a string str. The string str will contains numbers only, where each number stands for a key pressed on a mobile phone.
2. The following list is the key to characters map :
    0 -> .;
    1 -> abc
    2 -> def
    3 -> ghi
    4 -> jkl
    5 -> mno
    6 -> pqrs
    7 -> tu
    8 -> vwx
    9 -> yz
3. Complete the body of getKPC function - without changing signature - to get the list of all words that could be produced by the keys in str."""

codes=[".;","abc","def","ghi","jkl","mno","pqrs","tu","vwx","yz"]

def GKC(str):
    if len(str)==0:
        sq=[]
        sq.append("")
        return sq
    c=str[0]
    remstr=str[1:]
    combinations=GKC(remstr)
    keycom=[]
    for st in combinations:
        for ch in codes[int(c)]:
            keycom.append(ch + st)
    return keycom


str=input("enter string")
subseq=[]
print(GKC(str))