def firstUniqChar(s):
    char_count = {}

    # Count the occurrences of each character in the string
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Find the first character with count 1 and return its index
    for i in range(len(s)):
        if char_count[s[i]] == 1:
            return i

    # If no non-repeating character is found, return -1
    return -1

# Example usage
s = "leetcode"
result = firstUniqChar(s)
print(result)
