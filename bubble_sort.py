c=[19,11,16,29,70]

for i in range(len(c)):
    swapped = False
    j=0
    while j<len(c)-1:
        if c[j]>c[j+1]:
            c[j],c[j+1]=c[j+1],c[j]
        swapped = True
        j=j+1
    if swapped == False:
        break
print(c)


