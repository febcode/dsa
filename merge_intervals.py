def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key=lambda x: x[0])  # Sort by start time
    merged = []
    
    for interval in intervals:
        # If the list is empty or there's no overlap, add the interval
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # Otherwise, merge the intervals
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged

# Example Usage
print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
# Output: [[1, 6], [8, 10], [15, 18]]
