from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # Сортируем входной список для группировки одинаковых элементов
        nums.sort()
        result = []
        self.backtrack(nums, [], result, set())
        return result

    def backtrack(self, nums, current, result, used):
         # Если текущая перестановка достигла нужной длины, добавляем ее в результат
        if len(current) == len(nums):
            result.append(current[:])
            return

        for i in range(len(nums)):
            # Проверяем, использовался ли индекс i или является ли он дубликатом предыдущего элемента
            if i in used or (i > 0 and nums[i] == nums[i-1] and i-1 not in used):
                continue
            used.add(i)                                 # Добавляем индекс в использованные
            current.append(nums[i])                     # Добавляем элемент в текущую перестановку
            self.backtrack(nums, current, result, used) # Рекурсивный вызов backtrack
            used.remove(i)                              # Удаляем индекс из использованных
            current.pop()                               # Удаляем элемент из текущей перестановки


s = Solution()

nums = [1,1,2]
[[1,1,2],
 [1,2,1],
 [2,1,1]]
print(s.permuteUnique(nums))

nums = [1,2,3]
[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print(s.permuteUnique(nums))

'''
47. Permutations II

Given a collection of numbers, nums, that might contain duplicates,
--- return all possible unique permutations in any order.

Уникальные перестановки: Это означает, что результатом должны быть все возможные уникальные перестановки 
--- элементов входного массива nums, без повторений.

План решение:

1) Сначала сортируем входной список nums, чтобы сгруппировать одинаковые элементы вместе.
2) Затем  используем рекурсивный метод backtrack для генерации всех уникальных перестановок.
3) В backtrack мы проверяем, достигли ли мы конца текущей перестановки. Если да, добавляем ее в результат.
4) Иначе, для каждого элемента в nums, мы проверяем, был ли он уже использован или является дубликатом 
--- предыдущего элемента, который уже был использован. Если нет, мы добавляем его в текущую перестановку, 
--- рекурсивно вызываем backtrack и затем удаляем его из перестановки.
5) Мы используем set used для отслеживания использованных индексов, чтобы избежать дубликатов.

Временная сложность этого решения - O(N * N!), где N - длина входного списка nums, поскольку мы 
--- генерируем все N! перестановок и тратим O(N) времени на каждую из них для проверки дубликатов.

'''