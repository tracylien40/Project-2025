 def find_median(numbers):
   sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    if n % 2 == 0:
         If the number of elements is even, take the average of the middle two elements
       mid1 = sorted_numbers[n // 2 - 1]
        mid2 = sorted_numbers[n // 2]
       median = (mid1 + mid2) / 2
    else:
         If the number of elements is odd, take the middle element
        median = sorted_numbers[n // 2]

    return median

Example usage:
numbers = [5, 2, 8, 1, 7, 3]
result = find_median(numbers)
print("Median:", result)



