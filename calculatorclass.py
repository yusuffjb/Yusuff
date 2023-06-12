import re
class Calculator:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        return x // y

    @staticmethod
    def modulo(x, y):
        return x % y


calculator = Calculator()

str = input("Enter the arithmetic expression : ")
nums = re.split(r'[-+*/%]',str)
print(nums)

num1 = float(nums[0].strip())
num2 = float(nums[1].strip())

result = None
try:

    if '+' in str:
        result = calculator.add(num1, num2)
    elif '-' in str:
        result = calculator.subtract(num1, num2)
    elif '*' in str:
        result = calculator.multiply(num1, num2)
    elif '/' in str:
        result = calculator.divide(num1, num2)
    elif '%' in str:
        result = calculator.modulo(num1, num2)
        
except Exception as e:
        print(e)

print("Result:", result)