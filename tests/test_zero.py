from kata_closest_to_zero_2.zero import *

list_of_str_for_test = ["post", "most", "frost", "does", "blast", "window"]
list_of_str_for_test2 = ["postal", "post", "most", "frost", "does", "blast", "window"]
list_of_str_for_test3 = ["sotp", "postal", "post", "stpo", "most", "does"]
list_of_str_for_test4 = ['dog', 'god', 'doggo', 'ogd', 'cat', 'act', 'tac', 'tca',
    'abcd', 'dcba', 'bacd', 'bcda', 'cdba', 'dcab', 'cba', 'zyxw', 'wzyx',
    'yxwz', 'xwzy', 'zwxy', 'zywx', 'wxyz', 'wxzy', 'ywxz', 'yzwx', 'zwxy']


def test_how_many_same_letters():
    assert how_many_same_letters("most", "post") == 3


def test_does_not_count_twice():
    assert how_many_same_letters("most", "mm") == 1
    assert how_many_same_letters("mom", "mother") == 2


def test_create_list_of_counts():
    assert create_list_of_scores(list_of_str_for_test, "stop") == [4, 3, 3, 2, 2, 1]


def test_find_max_value():
    assert find_max_value(list_of_str_for_test, "stop")


def test_create_list_of_indexes_with_highest_scores():
    assert create_list_of_indexes_with_highest_scores(list_of_str_for_test2, "stop") == [0,1]


def test_list_the_highest_scored_words():
    assert list_the_highest_scored_words(list_of_str_for_test2, "stop") == ["postal", "post"]


def test_find_the_shortest():
    assert find_the_shortest(list_of_str_for_test4, "abce") == ["cba"]


def test_similar_order():
    assert find_similar_order(list_of_str_for_test3, "stop") == ["sotp", "stpo"]


def test_pick_the_first():
    assert identify_most_similar_word(list_of_str_for_test3, "stop") == "sotp"


def test_find_closest_to_zero():
    assert find_closest_to_zero(list_of_str_for_test4, "abce") == "cba"

