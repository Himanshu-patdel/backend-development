def counting_sort(arr):
    # Find the maximum value in the array
    max_val = max(arr)
    
    # Create a count array with a size of max_val + 1
    count = [0] * (max_val + 1)
    
    # Count occurrences of each number
    for num in arr:
        count[num] += 1
    
    # Build the output array
    output = []
    for value, freq in enumerate(count):
        output.extend([value] * freq)
    
    return output

# Example usage
arr = [3, 2, 4, 2, 2, 223, 4, 5, 4, 4]
sorted_arr = counting_sort(arr)
print(sorted_arr)



from typing import List

class Solution:
    def duplicates(self, n: int, arr: List[int]) -> List[int]:
        seen = set()  # To track seen elements
        duplicates = set()  # To track duplicates

        for num in arr:
            if num in seen:
                duplicates.add(num)  # If already seen, add to duplicates
            else:
                seen.add(num)  # Otherwise, add to seen

        if not duplicates:  # If no duplicates found
            return [-1]
        
        return sorted(duplicates)  # Return sorted list of duplicates
