class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        arr = []
        for i in range(1, n+1):
            if(i % 3 == 0 and i % 5 == 0):
                arr.append("FizzBuzz")
                continue
            elif(i % 3 == 0):
                arr.append("Fizz")
                continue
            elif(i % 5 == 0):
                arr.append("Buzz")
                continue
            else:
                arr.append(str(i))
        return arr
