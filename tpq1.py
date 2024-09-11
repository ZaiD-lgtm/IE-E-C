'''Q1: Write a program to determine if the sum of two numbers is
divisible by 7 (using if-else) and divisible by 5 (using a ternary operator).'''

a = int(input("num1: "))
b = int(input("num2: "))

if (a+b) % 7 == 0:
    print(f"the sum of {a} and {b} is divisible by 7. ")
else:
    print(f"the sum of {a} and {b} is not divisible by 7.")

ans = f"sum of {a} and {b} is divisible by 5" if (a+b) % 5 == 0 else f"sum of {a} and {b} is not divisible by 5"
print(ans)
