#factorial function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
        
num = int(input("Enter a number to find its factorial: "))

# Negative Check
if num < 0:
    print("Factorial is not defined for negative numbers.")

# ZERO Check
elif num == 0:
    print("The factorial of 0 is 1")

else:  
    print(f"The factorial of {num} is {factorial(num)}")        

