c=input('Enter the string:')
words = c.split()
lower=[]
upper=[]
for char in c:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)
combine = ''.join(lower + upper)
print(combine)
