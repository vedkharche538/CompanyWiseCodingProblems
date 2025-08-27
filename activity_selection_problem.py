start = [6, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]


def max_activity(start, finish):
    count = 0
    last_finish = -1
    for i in range(0, len(start)):
        if (last_finish == -1 or start[i] >= finish[last_finish]) and start[i] < finish[i]:
            last_finish = i
            count +=1
    return count


print(max_activity(start, finish))
