def how_many_same_letters(word1, word2):
    score = 0
    for letter in word1:
        if letter in word2:
            score += 1
    return score


def create_list_of_scores(list_of_str, given_word):
    list_of_scores = []
    for word in list_of_str:
        list_of_scores.append(how_many_same_letters(word, given_word))
    return list_of_scores


def find_max_value(list_of_str, given_word):
    list_of_scores = create_list_of_scores(list_of_str, given_word)
    highest_scored_word_value = max(list_of_scores)
    return highest_scored_word_value


def create_list_of_indexes_with_highest_scores(list_of_str, given_word):
    index_list = []
    list_of_scores = create_list_of_scores(list_of_str, given_word)
    max_value = find_max_value(list_of_str, given_word)
    for index, score in enumerate(list_of_scores, start=0):
        if score == max_value:
            index_list.append(index)
    return(index_list)


def list_the_highest_scored_words(list_of_str, given_word):
    indexes_with_highest_scores = create_list_of_indexes_with_highest_scores(list_of_str, given_word)
    list_of_best_matching_str = []
    for index in indexes_with_highest_scores:
        list_of_best_matching_str.append(list_of_str[index])
    return list_of_best_matching_str
