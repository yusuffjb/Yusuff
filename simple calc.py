import re
str = input("Enter the arithmetic expression : ")
nums = re.split(r'[-+*/]',str)
num1 = float(nums[0].strip())
num2 = float(nums[1].strip())
if '+' in str:
    print(num1 + num2)
elif '-' in str:
    print(num1 - num2)
elif '*' in str:
    print(num1 * num2)
else:
    print(num1 // num2)
    

