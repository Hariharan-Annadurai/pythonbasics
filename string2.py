c=input('Enter the sentence:')
def string_2(inputString):
    characters = 0
    digits = 0
    specialno = 0
    for char in inputString:
        if char.islower() or char.isupper():
            characters += 1
        elif char.isnumeric():
            digits += 1
        else:
            specialno += 1

    print("Character = ", characters, "numbers = ", digits, "Special_character = ", specialno)

print(string_2(c))