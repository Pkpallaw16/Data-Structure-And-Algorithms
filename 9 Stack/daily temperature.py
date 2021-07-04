def dailyTemperatures(temperatures):
    """
    :type temperatures: List[int]
    :rtype: List[int]
    """
    temp = []
    diff = [0 for i in range(len(temperatures))]
    for i in range(len(temperatures)):
        if not temp:
            temp.append(i)
        else:
            while len(temp) > 0 and temperatures[temp[-1]] < temperatures[i]:
                val = temp.pop()
                diff[val] = i - val
            temp.append(i)
    return diff
arr=[2, 5, 9, 3, 1, 12, 6, 8, 7]
print(dailyTemperatures(arr))