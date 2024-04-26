'''

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
'''


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        
        # Создаем словари с количеством каждой буквы в ransomNote и magazine
        ransom_counts = Counter(ransomNote)
        magazine_counts = Counter(magazine)
        
        # Проверяем, что для каждой буквы в ransomNote количество таких букв в magazine не меньше
        for letter, count in ransom_counts.items():
            if magazine_counts[letter] < count:
                return False
        
        return True
    
s = Solution()
ransomNote = "aaaabbb"
magazine ="bbbaaa"
print(s.canConstruct(ransomNote,magazine))

ransomNote = "aaaabbb"
magazine ="bbbaaaa"
print(s.canConstruct(ransomNote,magazine))