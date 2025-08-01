n=3
#op = 3 you can take 1 or 2 steps at a time

def climb_stair_case(n):
    if n==1:
        return 1
    if n==2:
        return 2
    
    return climb_stair_case(n-1) + climb_stair_case(n-2)


print(climb_stair_case(n))