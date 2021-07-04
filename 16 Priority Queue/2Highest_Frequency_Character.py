def Highest_Frequency_Character(str1):
    dict={}
    for i in range(len(str1)):
        if str1[i] in dict.keys():
            dict[str1[i]] +=1
        else:
            dict[str1[i]]=1

    Keymax = max(dict, key=dict.get)
    #Keymax = max(dict, key=lambda x: dict[x])
    v = list(dict.values())
    # taking list of car keys in v
    k = list(dict.keys())
    print(k[v.index(max(v))])
    print(dict)
    print(dict.get)
    print(Keymax)

s=input("enter string")
Highest_Frequency_Character(s)