def bubble_sort(arr):
    # N个数循环N轮，因为每轮最终冒出一个数
    for j in range(len(arr)):
        # 第1轮需要N-1次比较，第2轮需要N-2次比较......
        for i in range(len(arr) - 1 - j):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return print(arr)

arr = [5,2,0,1,3,1,4]

bubble_sort(arr)

# [0, 1, 1, 2, 3, 4, 5]
