# https://www.youtube.com/watch?v=N1dEdieBHRY&t=257s

variable  = input("Enter any Alphabet")

#initialized
count_vowels = 0
count_consunent = 0
vowel = 'AEIOUaeiou'
for i in variable:
    if i in vowel:
        count_vowels+=1
    else:
        count_consunent+=1

print('count vowel', count_vowels)
print('Count Consunent', count_consunent)
