def how_many_same_letters(word1, word2):
    count = 0
    for letter in word1:
        if letter in word2:
            count += 1
    return count


def create_list_of_counts(list_of_str, given_word):
    list_of_counts = []
    for word in list_of_str:
        list_of_counts.append(how_many_same_letters(word, given_word))
    return list_of_counts

def pick_the_highest_scored_word(list_of_str, given_word):
    list_of_scores = create_list_of_counts(list_of_str, given_word)
    highest_scored_letters_count = max(list_of_scores)
    max_index = list_of_scores.index(highest_scored_letters_count)
    return list_of_str[max_index]
