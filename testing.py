def two_sum(li,target):
    check_li = {}
    for i , num in enumerate(li):
        diff = target - num
        if diff in check_li:
            return (check_li[diff] , i)
        else:
            check_li[num] = i

# Example Usage
# print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]


def missing_number(li):
    n = len(li)
    total = n * (n+1) //2
    missing = total - sum(li)

    # print(missing)

# print(missing_number([1, 0, 3]))  # Output: 2
from collections import Counter
def first_unique_char(s):
    count = Counter(s)
    print(count)
    for i , char in enumerate(s):
        if count[char] == 1:
            print(s[i])
            return i
        
    return -1

# Example usage:
print(first_unique_char("lllllleetcode"))  # Output: 0
        
