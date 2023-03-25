from Levenshtein import distance


# counts the number of letters that two words have in common
def how_many_same_letters(word1, word2):
    score = 0
    for letter in word1:
        if letter in word2:
            score += 1
    return score


# creates a list of scores that represent how similar each word in list_of_str is to given_word
def create_list_of_scores(list_of_str, given_word):
    list_of_scores = []
    for word in list_of_str:
        list_of_scores.append(how_many_same_letters(word, given_word))
    return list_of_scores


# finds the maximum score in the list of scores
def find_max_value(list_of_str, given_word):
    list_of_scores = create_list_of_scores(list_of_str, given_word)
    highest_scored_word_value = max(list_of_scores)
    return highest_scored_word_value


# creates a list of indexes for the words in list_of_str that have the highest score
def create_list_of_indexes_with_highest_scores(list_of_str, given_word):
    index_list = []
    list_of_scores = create_list_of_scores(list_of_str, given_word)
    max_value = find_max_value(list_of_str, given_word)
    for index, score in enumerate(list_of_scores, start=0):
        if score == max_value:
            index_list.append(index)
    return index_list


# creates a list of the words in list_of_str that have the highest score
def list_the_highest_scored_words(list_of_str, given_word):
    indexes_with_highest_scores = create_list_of_indexes_with_highest_scores(list_of_str, given_word)
    list_of_best_matching_str = []
    for index in indexes_with_highest_scores:
        list_of_best_matching_str.append(list_of_str[index])
    return list_of_best_matching_str


# creates list of the shortest words from the list of highest scored words
def find_the_shortest(list_of_str, given_word):
    highest_scored_words = list_the_highest_scored_words(list_of_str, given_word)
    shortest_length = min(len(word) for word in highest_scored_words)
    shortest_words = [word for word in highest_scored_words if len(word) == shortest_length]
    return shortest_words

# uses the Levenshtein package to find the word in list_of_str that has the closest order of letters to given_word
def find_similar_order(list_of_str, given_word):
    distances = [distance(given_word, s) for s in list_of_str]
    min_distance = min(distances)
    closest_words = [list_of_str[i] for i, d in enumerate(distances) if d == min_distance]
    return closest_words


# identifies the first most similar word in the list to a given word
def identify_most_similar_word(list_of_str, given_word):
    to_identify = find_similar_order(list_of_str, given_word)
    return to_identify[0]


# this function finds the one closest to “zero”.
# A word is close to “zero” if it contains the same letters.
# If more than one word contains the same letters, choose the shortest one.
# If more than one is the same length, choose the one with the letters in the most similar order.
# If there is still a tie, choose the one that appeared first in the original list.
def find_closest_to_zero(list_of_str, given_word):
    shortest = find_the_shortest(list_of_str, given_word)
    closest = find_similar_order(shortest, given_word)
    most_similar = identify_most_similar_word(closest, given_word)
    return most_similar



# To do list:
# error handling (f.e. wrong input
# mom and mother - rewrite the create_list_of_scores function?

