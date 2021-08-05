#
# function findMaxVal(numbers) {
#     var maxNum = numbers[0];
#     for (var i = 0; i < numbers.length; i++) {
#       if (numbers[i] > maxNum) {
#         maxNum = numbers[i];
#       }
#     }
#     return maxNum;
# }
# Program.assertEqual(
#     findMaxVal([-13, -4, -24, -7]),
#     -4);
# Program.assertEqual(
#     findMaxVal([13, 4, 24, 7]),
#     24);
# Program.assertEqual(
#     findMaxVal([13, -4, 24, -7]),
#     24);
# Program.assertEqual(
#     findMaxVal([5/2, -2.22, Math.PI, 99]),
#     99);
import math


def find_max_val(numbers):
    max_num = numbers[0]
    for i in range(0, len(numbers)):
        if numbers[i] > max_num:
            max_num = numbers[i]
    return max_num


"""
assert (condition), 'message to display when AssertionError raised'
AssertionError 
    - only raised while the condition is evaluated False
    - if the condition evaluated True then nothing happen
"""
assert -4 == find_max_val([-13, -4, -24, -7]), 'Max value should be -4'
assert 24 == find_max_val([13, 4, 24, 7]), 'Max value should be 24'
assert 24 == find_max_val([13, -4, 24, -7]), 'Max value should be 24'
assert 99 == find_max_val([5 / 2, -2.22, math.pi, 99]), 'Max value should be 99'

assert 929 == find_max_val([5 / 2, -2.22, math.pi, 99]), 'Max value should be 99'
