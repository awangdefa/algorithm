import sys

# 递归层数限制
sys.setrecursionlimit(100000000)

def quick_sort(arr):
    # 回归条件
    if len(arr) < 2:
        return arr
    # 选取基准，随便选哪个都可以，选中间的便于理解
    pivot = arr[len(arr) // 2]
    # 定义基准值左右两个数列
    left, right = [], []
    # 从原始数组中移除基准值
    arr.remove(pivot)
    for item in arr:
        # 大于基准值放右边
        if item >= pivot:
            right.append(item)
        else:
            # 小于基准值放左边
            left.append(item)
    # 使用递归
    return quick_sort(left) + [pivot] + quick_sort(right)

arr = [5, 2, 0, 1, 3, 1, 4] * 1888

print(quick_sort(arr))
