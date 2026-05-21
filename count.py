def count(word, exact_letter):
    total = 0
    for letter in word:
        if letter == exact_letter:
            total = total + 1
    return total

print(count('banana', 'a'))

