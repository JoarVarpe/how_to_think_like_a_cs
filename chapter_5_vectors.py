# 5
def add_vectors(list1: list, list2: list) -> list:
    result_list = []
    if len(list1) == len(list2):
        result_list = [0] * len(list1)
        for i in range(len(list1)):
            result_list[i] = list1[i] + list2[i]
    return result_list


# 6
def scalar_mult(scalar: int, vector: list) -> list:
    for i in range(len(vector)):
        vector[i] *= scalar
    return vector


# 7
def dot_product(vector1: list, vector2: list) -> int or None:
    return_value = 0
    if len(vector1) != len(vector2):
        return
    else:
        for i in range(len(vector1)):
            return_value += vector1[i] * vector2[i]
        return return_value


# 8
def cross_product(vector1: list, vector2: list) -> list or None:
    if (len(vector1) == len(vector2)) and len(vector1) == 3:
        return [vector1[1] * vector2[2] - vector1[2] * vector2[1],
                - vector1[0] * vector2[2] + vector1[2] * vector2[0],
                vector1[0] * vector2[1] - vector1[1] * vector2[0]]
    return


# 9 they are equal
# song = "The rain in Spain..."
# print(" ".join(song.split()))

# 10
song = "I love spom! Spom is my favorite food. Spom, spom, yum!"


def replace(s: str, old: str, new: str) -> str:
    list_of_words = s.split(old)
    return new.join(list_of_words)


