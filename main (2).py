def find_positive_numbers(numbers):
    positive_numbers = []
    for num in numbers:
        if num > 0:
            positive_numbers.append(num)
    return positive_numbers

list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]

positive_list1 = find_positive_numbers(list1)
print("Input: list1 =", list1, "Output:", ', '.join(map(str, positive_list1)))

positive_list2 = find_positive_numbers(list2)
print("Input: list2 =", list2, "Output:", positive_list2)
