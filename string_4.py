c=input('Enter the sentence:')
def longest(c):
    return max(c, key=len)
def smallest(c):
    return min(c, key=len)

s=(c.split())
print(s)
print(longest(s))
print(smallest(s))