import string

# 1
# print("apple" > "pineapple") == False

# 2
prefixes_str = "JKLMNOPQ"
suffix = "ack"


def prefixes(prefixes_i: str, suffix_i: str) -> None:
    for letter in prefixes_i:
        if letter == "Q" or letter == "O":
            print(letter + "u" + suffix_i)
        else:
            print(letter + suffix_i)


# 3
def count_letters(word: str, letter_to_search: str) -> int:
    count = 0
    for letter in word:
        if letter == letter_to_search:
            count += 1
    return count


# 4
def count_letters2(word: str, letter_to_find: str, find_more_than_one=True) -> int or str:
    count = 0
    index_to_start_from = 0
    index_found = word.find(letter_to_find, index_to_start_from)
    if index_found != -1 and find_more_than_one:
        while True:
            index_to_start_from = index_found + 1
            index_found = word.find(letter_to_find, index_to_start_from)
            count += 1
            if index_found == -1:
                return count
    elif index_found != -1 and not find_more_than_one:
        return count + 1
    else:
        return "did not find {} in {}".format(letter_to_find, word)


# 5
the_text = """In academic writing, readers expect each paragraph to have a sentence or two that captures its main point. They’re often called “topic sentences,” though many writing instructors prefer to call them “key sentences.” There are at least two downsides of the phrase “topic sentence.” First, it makes it seem like the paramount job of that sentence is simply to announce the topic of the paragraph. Second, it makes it seem like the topic sentence must always be a single grammatical sentence. Calling it a “key sentence” reminds us that it expresses the central idea of the paragraph. And sometimes a question or a two-sentence construction functions as the key.
"""


def text_analysis(text: str, letter_to_get_stats_on: str) -> str:
    phrase_sans_punct = ""
    count_of_letter = 0
    for letter in text:
        if letter not in string.punctuation:
            phrase_sans_punct += letter
    list_of_words = phrase_sans_punct.split(" ")
    for word in list_of_words:
        if letter_to_get_stats_on in word:
            count_of_letter += 1
    return "Your text contains {} words, of which {} ({}%) contain \"{}\"".format(
        len(list_of_words), count_of_letter,
        count_of_letter / len(list_of_words) * 100,
        letter_to_get_stats_on)


# 6
layout = "{0:>4}{1:>6}{2:>6}{3:>8}{4:>13}{5:>24}"


def print_multiplication_table(layout: str, size: int) -> None:
    number_of_rows = "{:>2}:" + "{:>10}" * size
    list_of_numbers = []
    for i in range(size + 1):
        list_of_numbers.append(i + 1)
    row1 = number_of_rows.format(*list_of_numbers)
    row2 = " :" + "{:->10}".format("") * size
    print(row1)
    print(row2)
    for row in range(1, size + 1):
        for i in range(len(list_of_numbers)):
            list_of_numbers[i] = int(row * list_of_numbers[i])
        print(number_of_rows.format(row, *list_of_numbers))
        for i in range(len(list_of_numbers)):
            list_of_numbers[i] = list_of_numbers[i] / row


# 7
def reverse(string: str) -> str:
    reversed_string = ""
    for i in range(len(string) - 1, -1, -1):
        reversed_string = reversed_string + string[i]
    return reversed_string


# 8
def mirror(string: str) -> str:
    return string + reverse(string)


# 9
def remove_letter(letter: str, target: str) -> str:
    removed = ""
    for i in range(len(target)):
        if letter != target[i]:
            removed += target[i]
    return removed


# 10
def is_palindrome(word: str) -> bool:
    if len(word) == 0:
        return False
    if reverse(word.lower()) == word.lower():
        return True
    return False


# 11
def count(sub_string: str, target: str) -> int:
    count_of_appearances = 0
    index_to_start_from = target.find(sub_string)
    while True:
        if index_to_start_from == -1:
            return count_of_appearances
        if target.find(sub_string, index_to_start_from) != -1:
            index_to_start_from = target.find(sub_string, index_to_start_from + 1)
            count_of_appearances += 1


# 12
def remove_first(sub_string: str, target: str) -> str:
    resulting_string = target
    string_location = target.find(sub_string)
    if string_location == 0:
        resulting_string = target[string_location + len(sub_string):]
    elif string_location == -1:
        pass
    else:
        resulting_string = target[:string_location] + target[string_location + len(sub_string):]
    return resulting_string


# 13
def remove_all(sub_string: str, target: str) -> str:
    resulting_str = target
    while True:
        if sub_string in resulting_str:
            resulting_str = remove_first(sub_string, resulting_str)
        else:
            return resulting_str


# dot exercises
def find_url(target: str) -> str:
    start_str = "http://"
    return target[target.find(start_str) + len(start_str): target.find(" ")]


def find_crocodiles(target: str) -> str:
    return target[target.find("<") + len("<"): target.find(">")]

# 1
def test_of_tuples_as_arg_in_func(tuple) -> None:
    
# 2
# 3
