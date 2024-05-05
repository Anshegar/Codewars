
'''

Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

'''


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Если степень равна 0, возвращаем 1
        if n == 0:
            return 1
        
        # Если степень отрицательная, меняем основание и степень на обратные
        if n < 0:
            x = 1 / x
            n = -n
        
        # Инициализируем результат
        result = 1
        
        # Пока степень больше 0
        while n > 0:
            # Если степень нечетная, умножаем результат на основание
            if n % 2 == 1:
                result *= x
            # Возводим основание в квадрат
            x *= x
            # Уменьшаем степень вдвое
            n //= 2
        
        # Возвращаем результат
        return result