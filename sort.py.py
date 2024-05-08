def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
######################################################################
def job_scheduling(jobs):
    jobs.sort(key=lambda x: x[1])
    print(jobs)
    n = len(jobs)
    result = [False] * n
    slots = [False] * n
    for i in range(n):
        for j in range(min(n, jobs[i][1])-1, -1, -1):
            if not slots[j]:
                slots[j] = True
                result[i] = True
                break
    return result

jobs = [[1, 4], [2, 3], [3, 4], [4, 2], [5, 1]]
print(job_scheduling(jobs))
