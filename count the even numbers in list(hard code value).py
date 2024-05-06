def count_evens(nums):
    count = 0
    for i in nums:
        if i % 2 == 0:
            count += 1
    return count


num = [2, 3, 6, 8, 2]
print(count_evens(num))