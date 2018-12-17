def BubbleSort(ara):
    for i in range(0,len(ara)-1):
        for j in range(0,len(ara)-1-i):
            if (ara[j+1]<ara[j]):
                ara[j],ara[j+1] = ara[j+1],ara[j]#ShortCut Swap Technique
                '''tem = ara[j]
                ara[j] = ara[j+1]
                ara[j+1] = tem'''
    return ara

ara=[3,9,12,3,4,1]
blb = BubbleSort(ara)
print(blb)
