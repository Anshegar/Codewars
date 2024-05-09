'''

Maximum Gap

Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space.
'''

from typing import List

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        # Проверяем, что в списке есть хотя бы два элемента
        if len(nums) < 2:
            return 0
        
        # Сортируем список чисел
        nums.sort()
        
        # Инициализируем переменную для хранения максимальной разницы
        max_gap = 0
        
        # Проходим по отсортированному списку и находим максимальную разницу между соседними элементами
        for i in range(1, len(nums)):
            max_gap = max(max_gap, nums[i] - nums[i-1])
        
        # Возвращаем найденную максимальную разницу
        return max_gap