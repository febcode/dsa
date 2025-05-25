# Dynamic Programming

Dynamic Programming (DP) is just a smart way to solve problems where the same thing gets calculated again and again.

Instead of solving the same subproblem multiple times, you store the result the first time and reuse it when needed. That’s it.

Real-World Example

Suppose you're walking up a staircase, and you can take either 1 or 2 steps at a time. You want to know how many different ways you can reach the top.

Let’s say it's 5 steps.

Now, to reach step 5:

You could come from step 4 (1 step before)

Or from step 3 (2 steps before)


So:
ways(5) = ways(4) + ways(3)

And to get ways(4), you'd again do:
ways(4) = ways(3) + ways(2)

See what’s happening? You're solving the same smaller steps again and again.

Instead, store the result for each step once and use it later.

ways = [1, 1]  # ways[0] = 1, ways[1] = 1
for i in range(2, n+1):
    ways.append(ways[i-1] + ways[i-2])

Now you’re doing less work and reaching the answer faster.

A Common DP Interview Problem – Fibonacci Numbers

Fibonacci series: 0, 1, 1, 2, 3, 5, 8, ...

Each number is the sum of the previous two.

Naive solution (recursion):

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

Looks simple, but super slow — because it repeats the same calculation over and over.

DP solution:

def fib(n):
    dp = [0, 1]
    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]

Now it’s much faster. You only calculate each number once.


So, What’s the Pattern in DP Problems?

If a problem:

1. Can be split into smaller problems

2. Repeats the same subproblems

3. You can store and reuse answers


Then it’s likely a DP problem.
