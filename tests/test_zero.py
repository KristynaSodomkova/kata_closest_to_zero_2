from kata_closest_to_zero_2.zero import *

list_of_str_for_test = ["post", "most", "frost", "does", "blast", "window"]
list_of_str_for_test2 = ["postal", "post", "most", "frost", "does", "blast", "window"]


def test_how_many_same_letters():
    assert how_many_same_letters("most", "post") == 3


def test_does_not_count_twice():
    assert how_many_same_letters("most", "mm") == 1


def test_create_list_of_counts():
    assert create_list_of_scores(list_of_str_for_test, "stop") == [4, 3, 3, 2, 2, 1]


def test_find_max_value():
    assert find_max_value(list_of_str_for_test, "stop")

def test_pick_the_highest_scored_words():
    assert pick_the_highest_scored_word(list_of_str_for_test, "stop") == "post"


def test_more_than_one_max_value():
    assert pick_the_highest_scored_word(list_of_str_for_test2, "stop") == "post"


#def test_find_the_shortest():
 #   assert find_the_shortest() ==