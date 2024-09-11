def palindrome (str):
    new_str = ""
    for i in str:
        if i.isalnum():
            new_str += i.lower()
        else:
            continue
    if new_str == new_str[::-1]:
        print("yes the given string is a palindrome")

    else:
        print("the given string is not a palindrome")

str = input("Enter a string:")
palindrome(str)

def main(str):
    newstr = ""
    for i in str:
        if i.islower():
            newstr += i.upper()
        elif i.isupper():
            newstr += i.lower()
        else:
            newstr += i

    return newstr

newstr = main(str)
print(newstr)



