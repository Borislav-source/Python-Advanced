def best_list_pureness(my_list, n, best_result=[], rotations=0, rotations_to_best=[]):
    if rotations == n+1:
        return
    the_sum = 0
    for el in range(len(my_list)):
        the_sum += el * my_list[el]
    if len(best_result) == 0:
        best_result.append(the_sum)
        rotations_to_best.append(rotations)
    elif the_sum > best_result[0]:
        best_result.pop()
        best_result.append(the_sum)
        rotations_to_best.pop()
        rotations_to_best.append(rotations)

    for i in range(n):
        last = my_list.pop()
        my_list.insert(0, last)
        break
    best_list_pureness(my_list, n, best_result, rotations + 1, rotations_to_best)
    return f"Best pureness {best_result[0]} after {rotations_to_best[0]} rotations"


# print(best_list_pureness([4, 3, 2, 1], 4))

import unittest

class Tests(unittest.TestCase):
    def test(self):
        test = ([1, 2, 3, 4, 5], 10)
        result = best_list_pureness(*test)
        self.assertEqual(result, "Best pureness 40 after 0 rotations")

if __name__ == "__main__":
    unittest.main()




