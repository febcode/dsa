nterms = int(input("how many item"))
n1,n2 = 0,1
count = 0

if nterms<0:
    print('enter positive')
elif nterms==1:
    print(n1)
else:
    while count<nterms:
        print(n1)
        nth = n1 +n2
        n1 = n2
        n2 = nth
        count+1


"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

 

Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3."""

def fib(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 0 :
            return 0
        elif n == 1:
            return 1
        
        return self.fib(n-1) + self.fib(n-2)


def climbStairs(self, n):
        
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1 :
            return 1 
        if n == 2 :
            return 2 
        
        return self.climbStairs(n-1) + self.climbStairs(n-2) 
        