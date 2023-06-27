def moveZeroes(nums):
    # Initialize a pointer to keep track of the position to place non-zero elements
    pointer = 0

    # Iterate through the array
    for i in range(len(nums)):
        # If the current element is non-zero, move it to the current pointer position
        if nums[i] != 0:
            nums[pointer] = nums[i]
            pointer += 1

    # Fill the remaining positions from the pointer position to the end with 0's
    while pointer < len(nums):
        nums[pointer] = 0
        pointer += 1

    return nums

# Example usage
nums = [0, 1, 0, 3, 12]
result = moveZeroes(nums)
print(result)
