from kata_closest_to_zero_2.zero import *

list_of_str_for_test = ["post", "most", "frost", "does", "blast", "window"]


def test_how_many_same_letters():
    assert how_many_same_letters("most", "post") == 3


def test_does_not_count_twice():
    assert how_many_same_letters("most", "mm") == 1

def test_pick_the_highest_same_letters():
    assert pick_the_highest_same_letters(list_of_str_for_test, "stop") == "post"

#def test_find_the_shortest():
 #   assert find_the_shortest() ==