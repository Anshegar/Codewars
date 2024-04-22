class Solution:
    def reorganizeString(self, s: str) -> str:

        # Count the occurrences of each character
        char_count = {}
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        # Sort the characters by their frequency
        sorted_chars = sorted(char_count, key=lambda x: (-char_count[x], x))
        
        # Create the rearranged string
        result = [None] * len(s)
        index = 0
        for char in sorted_chars:
            count = char_count[char]
            for i in range(count):
                if index >= len(s):
                    index = 1
                result[index] = char
                index += 2
        
        # Check if the rearranged string has adjacent characters
        for i in range(1, len(result)):
            if result[i] == result[i-1]:
                return ""
        
        return ''.join(result)





Obj  = Solution()   
result =  Obj.reorganizeString("aabbbbcc")
print(result)
