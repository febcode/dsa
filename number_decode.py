# Problem:
# A message containing letters can be encoded as numbers ('A' -> 1, 'B' -> 2, ..., 'Z' -> 26). 
# Given a string s containing only digits, return the total number of ways to decode it.
# Input: s = "226"
# Output: 3
# Explanation: It can be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

def num_decodings(s: str) -> int:
    if not s or s[0] == '0':
        return 0

    dp = [0] * (len(s) + 1)
    dp[0], dp[1] = 1, 1

    for i in range(2, len(s) + 1):
        if s[i-1] != '0':
            dp[i] += dp[i-1]
        if '10' <= s[i-2:i] <= '26':
            dp[i] += dp[i-2]

    return dp[-1]

# Example Usage
print(num_decodings("226"))  # Output: 3
