def countVowelConsonant(userInput):
    vowels = "aeiouAEIOU"
    countvowel = 0
    countconsonants = 0
    for char in userInput:
        if char.isalpha():
            if char in vowels:
                countvowel += 1
            else:
                countconsonants += 1
    return countvowel, countconsonants

vow, conso = countVowelConsonant("Vikram Singh Kushwaha")

print(f"Number of Vowels are - {vow}\nNumber of Consonants are - {conso}")




















































































































