def Highest_Frequency_Character(str1):
    n=len(str1)
    freq={}
    for ch in str1:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    max=-1
    max_freq=None
    for key in freq.keys():
        if freq[key]>max:
            max=freq[key]
            max_freq=key
    print(max_freq)

Highest_Frequency_Character("zmszeqxllzvheqwrofgcuntypejcxovtaqbnqyqlmrwitc")


