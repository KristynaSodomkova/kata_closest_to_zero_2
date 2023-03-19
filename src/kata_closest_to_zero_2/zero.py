def how_many_same_letters(word1, word2):
    count = 0
    for letter in word1:
        if letter in word2:
            count += 1
    return count
