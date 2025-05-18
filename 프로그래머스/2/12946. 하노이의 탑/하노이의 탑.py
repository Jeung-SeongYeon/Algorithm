def switch_num(arr, target1, target2):
    for i in range(len(arr)):
        if arr[i] == target1:
            arr[i] = target2
        elif arr[i] == target2:
            arr[i] = target1
    return

def solution(n):
    answer = [[1,3]]
    for i in range(1,n):
        left = [arr[:] for arr in answer]
        right = [arr[:] for arr in answer]
        for j in range(len(left)):
            left_arr = left[j]
            right_arr = right[j]
            switch_num(left_arr, 2, 3)
            switch_num(right_arr, 1, 2)
                
        answer = left + [[1,3]] + right
    return answer