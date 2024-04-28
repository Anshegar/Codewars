'''
Number of Steps to Reduce a Number to Zero
Given an integer num, return the number of steps to reduce it to zero.

In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
'''


class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        
        while num > 0:
            if num % 2 == 0:
                # Если число четное, делим его на 2
                num //= 2
            else:
                # Если число нечетное, вычитаем 1
                num -= 1
            
            # Увеличиваем счетчик шагов
            steps += 1
        
        return steps
    
s = Solution()
n= 10
print(s.numberOfSteps(n))
n= 111
print(s.numberOfSteps(n))