
# Basic Math 

1. Modulo (%)

Gives the remainder after division.
For example, 7 % 3 gives 1 because 3 goes into 7 two times, with a remainder of 1.

Why it's useful:

It’s often used in algorithms where you need to loop back through an array (like rotating it or implementing circular queues).

Example: If you want to find the new index after rotating an array by k positions:

new_index = (current_index + k) % n

This helps avoid going out of bounds by “wrapping around” the array.


2. Integer Division (//)

Divides two numbers and rounds down the result.
For example, 7 // 3 results in 2 (because it rounds down the result of 2.33).


It's commonly used when you need to split a range, for example, in Binary Search.

Example: When you want to find the middle index of a range:

mid = (low + high) // 2

This ensures you avoid floating-point values and only get the integer part.


3. Prime Numbers

Numbers that are divisible only by 1 and themselves.
For example, 2, 3, 5, 7, 11 are prime numbers. But 4, 6, 8, 9, and 10 are not.


Prime numbers are frequently used in hashing algorithms, cryptography, and number theory problems.

Optimization Tip: To check if a number is prime, you don’t need to check all numbers up to n. Instead, you only need to check up to sqrt(n), which makes your algorithm faster.

Python code:

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n > 1


4. Power of 2

Numbers like 1, 2, 4, 8, 16, 32…
These are powers of 2 because they follow the formula 2^n.


Powers of 2 are common in bit manipulation and binary trees.

For example, a binary tree with height h will have 2^h - 1 nodes.

To check if a number is a power of 2 using Python Programming:

def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

This is an efficient way to check if a number is a power of 2 using bitwise operations.



5. GCD (Greatest Common Divisor)

The largest number that divides two numbers without leaving a remainder.
For example, the GCD of 36 and 60 is 12, because 12 is the largest number that divides both.

Why it's useful:

GCD helps simplify fractions (e.g., 36/60 simplifies to 3/5).

It's used in problems where you need to find common divisors, such as in task scheduling (syncing intervals).

Euclid’s Algorithm to calculate GCD:

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


6. Combinations (nCr)

How many ways can you choose r elements from n elements?
For example, choosing 2 items from a set of 3: {1, 2, 3}. The possible pairs are: (1, 2), (1, 3), (2, 3) — so 3 combinations in total.


You’ll encounter combinations in problems where you have to count pairs, triplets, or subsets, like in problems involving subsets or selecting items from a list.

Formula for combinations (nCr):
nCr = n! / (r!(n-r)!)



Key Takeaways:

- Modulo is used for wrapping values around and handling circular data.

- Integer division ensures you work with whole numbers, particularly useful in algorithms like Binary Search.

- Prime numbers are essential in hashing, cryptography, and optimization.

- Powers of 2 show up in binary operations and data structures like binary trees.

- GCD helps simplify ratios and find common factors.

- Combinations are all about counting possible ways to choose items and show up in many optimization problems.