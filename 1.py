numbers = [1,3,5,2,1,3,4,5,6]
def secondLargest_numbers(numbers):
    unique_numbers =list(set(numbers))
    if len(unique_numbers)<2:
        return None
    else:
        unique_numbers.sort(reverse=True)
        return unique_numbers[1]
print(secondLargest_numbers(numbers))