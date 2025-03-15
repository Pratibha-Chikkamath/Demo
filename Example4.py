def count_vowels_hex(s):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in s if char in vowels)
    return hex(count)

# Example usage
input_string = "Hello World"
print("Number of vowels in hex:", count_vowels_hex(input_string))
