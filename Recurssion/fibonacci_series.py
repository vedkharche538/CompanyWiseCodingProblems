# Create a function to find the nth Fibonacci number (e.g., Fib(5) = 5, where each number is the sum of the two before it).
"""_summary_
Base condition will required 2 number
0,1
0,1,0+1,1+1,2+1,...

suppose n=2
need to compute compute fib(1) + fib(0)
n=3
fib(2) + fib(1)
"""

def fib(n):
    if n==1:
        return 1
    if n==0:
        return 0
    return fib(n-1) + fib(n-2)

print(fib(3))