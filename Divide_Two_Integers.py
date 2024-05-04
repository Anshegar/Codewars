'''
Divide Two Integers

Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

'''








class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Определение минимального и максимального значения для 32-битных целых чисел
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Обработка частных случаев:
        # Если делимое равно 0, возвращаем 0
        if dividend == 0:
            return 0
        # Если делитель равен 1, возвращаем минимум из делимого и максимального значения
        if divisor == 1:
            return min(max(INT_MIN, dividend), INT_MAX)
        # Если делитель равен -1, возвращаем минимум из отрицательного максимального значения и отрицательного делимого
        if divisor == -1:
            return min(max(-INT_MAX, -dividend), INT_MAX)
        
        # Определение знака результата
        sign = (dividend > 0) == (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)
        
        # Инициализация результата
        result = 0
        
        # Выполнение деления без использования умножения и деления
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= temp << 1:
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            result += multiple
        
        # Применение знака к результату
        if not sign:
            result = -result
        
        # Обработка ограничений на диапазон целых чисел:
        # Если результат больше максимального значения, возвращаем максимальное значение
        # Если результат меньше минимального значения, возвращаем минимальное значение
        return min(max(INT_MIN, result), INT_MAX)