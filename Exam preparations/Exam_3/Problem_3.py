def numbers_searching(*args, missing_value=0):
    my_list = list(args)
    my_list = sorted(my_list)
    duplicates = []
    for num in my_list:
        if my_list.count(num) > 1:
            if num not in duplicates:
                duplicates.append(num)
    for n in range(len(my_list)-1):
        if my_list[n] + 1 == my_list[n+1]:
            continue
        elif my_list[n] + 1 not in my_list:
            missing_value = my_list[n] + 1
            break
    duplicates = sorted(duplicates)
    return [missing_value, duplicates]


# print(numbers_searching(-3, -2, -1, -5, -3, -4, -7, -49, -49))
#
# print(numbers_searching(50, 50, 48, 47, 47, 46, 46, 49, 45, 49, 44, 45, 44, 44, 48, 44, 48))
#
# print(numbers_searching(1, 2, 4, 2, 5, 4))
#
# print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
#
# print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))


# import unittest
#
# class Tests(unittest.TestCase):
#     def test_zero(self):
#         expected = [46, [44, 45, 47, 48, 50]]
#         result = numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48)
#         self.assertEqual(result, expected)
#
# if __name__ == "__main__":
#     unittest.main()