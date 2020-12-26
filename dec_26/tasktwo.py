
def vowel_count(s):
    count = 0
    s = s.upper()
    for i in s:
        if i in ['A', 'E', 'I', 'U', 'O']:
            count += 1
    return count

phrase = "lemon"
print(vowel_count(phrase))