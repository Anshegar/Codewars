'''
Minimum Number of Operations to Make Array XOR Equal to K

You are given a 0-indexed integer array nums and a positive integer k.

You can apply the following operation on the array any number of times:

Choose any element of the array and flip a bit in its binary representation. Flipping a bit means changing a 0 to 1 or vice versa.
Return the minimum number of operations required to make the bitwise XOR of all elements of the final array equal to k.

Note that you can flip leading zero bits in the binary representation of elements. For example, for the number (101)2 you can flip the fourth bit and obtain (1101)2.


Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 106
0 <= k <= 106


XOR (Exclusive OR) - это логический оператор, чей результат является истинным, 
когда только один из двух входов истинен, но не оба одновременно.
'''


from typing import List
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Шаг 1: Вычислить XOR всех элементов массива
        # --- Когда мы используем оператор XOR (^), каждый бит в xor_sum и num сравнивается, 
        # Если оба бита равны (0 и 0 или 1 и 1), результат будет 0.
        # Если биты различаются (0 и 1 или 1 и 0), результат будет 1.
        xor_sum = 0
        for num in nums:
            xor_sum ^= num
        
        # Шаг 2: Найти минимальное количество операций, если он равен k То 0 операций соответсвенно
        if xor_sum == k:
            return 0      
        # Затем мы считаем количество установленных битов (1) в двоичном представлении этого результата.
        # Это количество установленных битов и будет минимальным количеством операций, необходимых для того, чтобы XOR всех элементов был равен k.
        return bin(xor_sum ^ k).count('1')