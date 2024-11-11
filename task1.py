user_input = input("say something ")

def vowel_count(text):
    current_vowels = 0
    vowels = ["a", "e", "i", "o", "u"]
    for value in text:
        if value in vowels:
            current_vowels += 1
    print(f"the number of vowels in the string is: {current_vowels}")
    

vowel_count(user_input.lower())    
