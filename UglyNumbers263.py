class Solution(object):
    def isUgly(self, n):
        if n <= 0:
            return False  # Negative numbers and 0 are not ugly numbers.
        
        for i in [2, 3, 5]:
            while n % i == 0:
                n //= i  # Keep dividing n by i if it is divisible.
        
        return n == 1  # If after dividing, n becomes 1, it's an ugly number.


Big O -- time complexity is o(log n)
Explaination:
Line 3-4 satisfys the prime conditions that the number (n) needs to be positive
Line 6 shows that i is going to loop 2,3,5 if n is divisible by one of those numbers
