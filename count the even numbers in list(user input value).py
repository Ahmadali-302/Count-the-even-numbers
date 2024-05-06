def count_even():
    nums = int(input("please enter the range of numbers that you want to enter: "))
    num_list = []
    for i in range(nums):
        num = int(input("Enter the number: "))
        num_list.append(num)
    count = 0
    for j in num_list:
        if j % 2 == 0:
            count += 1
    return count


print(count_even())