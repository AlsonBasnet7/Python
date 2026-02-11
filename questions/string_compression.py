def compress_string(s):
    if not s:
        return ""

    compressed = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            compressed += s[i-1] + str(count)
            count = 1

    # Add the last character and its count
    compressed += s[-1] + str(count)
    
    return compressed

# Example usage
string_input = "aaabbc"
result = compress_string(string_input)
print(result)  # Output: a3b2c1
