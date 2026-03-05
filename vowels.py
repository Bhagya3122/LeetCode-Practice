'''Write a Python program that:
Takes a string input from the user
Counts how many vowels are present in the string
Prints the total count'''

user_input = input("Enter the text you want to check the vowels for")
vowel_list=["a","e","i","o","u","A","E","I","O","U"]
a=0
for i in range(len(user_input)):
     if user_input[i] in vowel_list:
          a=a+1

print(a)