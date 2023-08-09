def count_characters_and_english_vowels(input_string):

    char_count = 0
    vowel_count = 0
    

    english_vowels = "aeiouAEIOU"
    
    for char in input_string:
        if char.isalpha():
            char_count += 1
            if char in english_vowels:
                vowel_count += 1
                char_count -=1
                
    return char_count, vowel_count

input_text = input("Enter a text: ")

total_chars, total_vowels = count_characters_and_english_vowels(input_text)

print("Total characters : ", total_chars)
print("Total English vowels : ", total_vowels)