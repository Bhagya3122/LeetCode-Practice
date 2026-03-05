'''Write a Python program that:

Takes a number input from the user

Prints the factorial of that number.'''

num=int(input("Enter a number for which you want the factorial"))
result=1
for i in range(1,num+1):
        result=i*result

print(result)
    