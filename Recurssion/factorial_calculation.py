# Write a function to compute the factorial of a number (e.g., 5! = 5 * 4 * 3 * 2 * 1).



def factorial(n):
    if n == 1:
        return 1
    return factorial(n-1) * n

print(factorial(6))