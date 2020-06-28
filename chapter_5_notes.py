def my_find(haystack: str, needle: str) -> int:
    for index, letter in enumerate(haystack):
        if letter == needle:
            return index
    return -1


def find2(haystack: str, needle: str, start=0, end=-1) -> int:
    for index, letter in enumerate(haystack[start:end]):
        if letter == needle:
            return index + start


layout = "{0:>4}{1:>6}{2:>6}{3:>8}{4:>13}{5:>24}"

print(layout.format("i", "i**2", "i**3", "i**5", "i**10", "i**20",))
for i in range(1, 11):
    print(layout.format(i, i ** 2, i ** 3, i ** 5, i ** 10, i ** 20))
