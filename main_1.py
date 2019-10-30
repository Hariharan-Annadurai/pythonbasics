print('My routine begins from',repr(__name__))

print('My program begins')

def demo(str1):
    print('Beginning Demo')
    str2=str.split(str1)
    print('End Demo')
    return str2

def man():
    str1='Hello everyone'
    print(str1)
    str2=demo(str1)
    print(str2)

if __name__ == '__main__':
    man()
