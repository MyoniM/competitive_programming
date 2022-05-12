def countingValleys(steps, path):
    value = {
        "U": 1,
        "D": -1        
    }
    step_sum, count = 0,0
    for i in path:
        change_value = value[i]
        if step_sum == 0 and change_value == -1: count+=1
        step_sum+=change_value
    return count
