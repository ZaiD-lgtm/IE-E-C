'''
Q2: Write a program to calculate the factorial of a
given number using a for loop.
'''
num = int(input("Enter number: "))
fac = 1
str =""
for i in range(1,num+1):
    fac *= i
    if i != num:
        str += f"{i}*"
    else:
        str += f"{i}"

print(f"factorial of num is => {str}= ",fac)
