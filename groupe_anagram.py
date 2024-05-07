'''
Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
 typically using all the original letters exactly once.

'''



from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        
        for word in strs:
            # Сортируем буквы в слове, чтобы получить уникальный ключ для анаграмм
            sorted_word = ''.join(sorted(word))
            # Добавляем слово в соответствующую группу анаграмм
            anagrams[sorted_word].append(word)
        
        # Возвращаем список групп анаграмм
        return list(anagrams.values())

# Примеры из условия задачи
s = Solution()
input1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
input2 = [""]
input3 = ["a"]

output1 = s.groupAnagrams(input1)
output2 = s.groupAnagrams(input2)
output3 = s.groupAnagrams(input3)

print(output1)
print(output2)
print(output3)