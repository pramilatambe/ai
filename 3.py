def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def job_scheduling(jobs):
    jobs.sort(key=lambda x: x[1])
    n = len(jobs)
    result = [False] * n
    slots = [False] * n
    for i in range(n):
        for j in range(min(n, jobs[i][1])-1, -1, -1):
            if not slots[j]:
                slots[j] = True
                result[jobs[i][0]] = True
                break
    return result
selection_sort([3,2,8,7,1])
job_scheduling([[3,4],[1,3],[4,4],[0,2],[1,1]])