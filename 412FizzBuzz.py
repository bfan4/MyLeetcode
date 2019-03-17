class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        
        for num in range(1, n+1):
            divBy3 = (num % 3 == 0)
            divBy5 = (num % 5 == 0)
            
            if divBy3 and divBy5:
                result.append("FizzBuzz")
            elif divBy3:
                result.append("Fizz")
            elif divBy5:
                result.append("Buzz")
            else:
                result.append(str(num))
        return result