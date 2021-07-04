#bc ->[--,-c,b-,bc]
#abc ->[---,--c,-b-,-bc,a--,a-c,ab-,abc]
def subsequence_string(str):
    if len(str)==0:
        sq=[]
        sq.append("")
        return sq
    c=str[0]
    rstr=str[1:]
    rres=subsequence_string(rstr)
    subseq=[]
    for st in rres:
        subseq.append(""+st)
    for st in rres:
        subseq.append(c+st)
    return subseq


str=input("enter string")
print(subsequence_string(str))