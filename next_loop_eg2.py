string_list = ["Coder", "Academy", "Champion"]
result = 0

for string in string_list:
    for vowel in string:
        if vowel in "aeiouAEIOU":
            result += 1

print("The total occurance of vowels in the list is", result)