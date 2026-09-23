class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        result = [''] * n

        for i in range(n):
            if (i + 1) % 3 == 0 and (i + 1) % 5 == 0:
                result[i] = 'FizzBuzz'
            elif (i + 1) % 3 == 0:
                result[i] = 'Fizz'
            elif (i + 1) % 5 == 0:
                result[i] = 'Buzz'
            else:
                result[i] = str(i + 1)
        
        return result
