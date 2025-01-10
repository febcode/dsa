phone_book = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
}
print(phone_book["Alice"])  # O(1)


def word_count(text):
    counts = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts
print(word_count("apple banana apple"))
# {'apple': 2, 'banana': 1}

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
print(two_sum([ 11,21, 15,4,5], 9))  # [0, 1]
