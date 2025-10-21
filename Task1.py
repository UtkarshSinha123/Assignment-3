# Define a function to calculate factorial
def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

# Take input from the user
number = int(input("Enter a number: "))

# Call the function and display the result
print("The factorial of", number, "is", factorial(number))
