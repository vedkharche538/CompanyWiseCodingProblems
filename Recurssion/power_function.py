# Write a recursive function to calculate x raised to the power of n (e.g., 2^3 = 8).
def power(x, n):
    if n == 1:
        return x
    return x * power(x, n-1)

print(power(2,8))