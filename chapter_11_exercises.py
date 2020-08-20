class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __rmul__(self, other):
        return Point(other * self.x, other * self.y)

    def get_self_coordinates(self):
        return self.x, self.y

    def distance_from_point_to_point(self, target):
        return ((target.x - self.x) ** 2 + (target.y - self.y) ** 2) ** 0.5

    def reflect_x(self):
        return Point(self.x, - self.y)

    def get_midpoint_between(self, target):
        return (self.x + target.x) / 2, (self.y + target.y) / 2

    def slope_from_origin(self):
        if self.x != 0:
            return self.y / self.x
        else:
            return "No slope from origin if x = 0"

    def get_perpindicular_bisector_eq(self, target):
        midpoint = self.get_midpoint_between(target)
        slope = self.get_slope_to(target)
        if slope[0] == "slope":
            neg_reciprocal = - slope[1] ** (-1)
            return neg_reciprocal, midpoint[1] - neg_reciprocal * midpoint[0]

    def get_line_to(self, target):
        if self.x != target.x:
            slope = (self.y - target.y) / (self.x - target.x)
            return slope, slope * (-self.x) + self.y

    def get_slope_to(self, target):
        if self.x != target.x and self.y != target.y:
            return "slope", (self.y - target.y) / (self.x - target.x)
        elif self.x == target.x and self.y != target.y:
            return "vertical", self.x
        elif self.x != target.x and self.y == target.y:
            return "horizontal", self.y

    # TODO FINISH get_midpoint_of_circle
    def get_midpoint_of_circle(self, target1, target2, target3):
        # test1 = (self.get_slope_to(target1) == target2.get_slope_to(target3))
        # test2 = (self.get_slope_to(target2) == target1.get_slope_to(target3))
        # test3 = (self.get_slope_to(target3) == target2.get_slope_to(target3))
        # line1 = self.get_perpindicular_bisector_eq(target1)
        # line2 = target2.get_perpindicular_bisector_eq(target3)
        # x_val = (line1[1] - line2[1]) / (line1[0] - line2[0])
        # y_val = line1[0] * x_val + line1[1]
        # return x_val, y_val
        pass


# p1 = Point(0, 4)
# p2 = Point(3, 4)
# p3 = Point(4, 2)
# p4 = Point(3, 0)
# print(p1.get_midpoint_of_circle(p4, p2, p3))

# print(round((4 + 3) / (3 - 2.3)))
# print(p2.get_perpindicular_bisector_eq(p1))


class SMS_store:

    def __init__(self):
        self._messages = []

    def add_new_arrival(self, from_number: int, time_arrived: float, text_of_SMS: str) -> None:
        has_been_viewed = False
        self._messages.append((has_been_viewed, from_number, time_arrived, text_of_SMS))

    def message_count(self) -> int:
        if len(self._messages) > 0:
            return len(self._messages)
        return 0

    def get_unread_indexes(self) -> list:
        unread = []
        for i in range(len(self._messages)):
            if not self._messages[i][0]:
                unread.append(i)
        return unread

    def get_message(self, index):
        if len(self._messages) > index:
            self._messages[index] = (True, self._messages[index][1], self._messages[index][2], self._messages[index][3])

            return self._messages[index][1], self._messages[index][2], self._messages[index][3]

    def delete(self, index) -> None:
        if len(self._messages) > index:
            del self._messages[index]

    def clear(self):
        self._messages = []


class Rectangle:

    def __init__(self, posn, w, h):
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "({}, {}, {})".format(self.corner, self.width, self.height)

    def grow(self, delta_width, delta_height):
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        self.corner.x += dx
        self.corner.y += dy

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * self.width + 2 * self.height

    def flip(self):
        temp = self.width
        self.width = self.height
        self.height = temp

    def contains(self, point):
        check1 = self.corner.x <= point.x < self.width
        check2 = self.corner.y <= point.y < self.height

        if check1 and check2:
            return True
        return False

    def collides_with(self, rectangle):
        rectangle_is_inside_self_height = self.corner.y <= rectangle.corner.y <= self.corner.y + self.height
        self_inside_rectangle_height = rectangle.corner.y <= self.corner.y <= rectangle.corner.y + rectangle.height
        rectangle_is_inside_self_width = self.corner.x <= rectangle.corner.x <= self.corner.x + self.width
        self_inside_rectangle_width = rectangle.corner.x <= self.corner.x <= rectangle.corner.x + rectangle.width

        print("Is rectangle corner {} inside self {} height {} : {}"
              .format(rectangle.corner.get_self_coordinates(), self.corner.get_self_coordinates()
                      , self.height, rectangle_is_inside_self_height))
        print("Is self corner {} inside rectangle {} height {} : {}"
              .format(self.corner.get_self_coordinates(), rectangle.corner.get_self_coordinates()
                      , rectangle.height, self_inside_rectangle_height))
        print("Is rectangle corner {} inside self {} width {} : {}"
              .format(rectangle.corner.get_self_coordinates(), self.corner.get_self_coordinates(),
                      self.width, rectangle_is_inside_self_width))
        print("Is self corner {} inside rectangle {} width {} : {}"
              .format(self.corner.get_self_coordinates(), rectangle.corner.get_self_coordinates(),
                      rectangle.width, self_inside_rectangle_width))

        if rectangle_is_inside_self_width and rectangle_is_inside_self_height:
            return True
        elif self_inside_rectangle_width and self_inside_rectangle_height:
            return True
        return False


r1 = Rectangle(Point(0, 0), 2, 2)
r2 = Rectangle(Point(1, 0), 2, 5)
r3 = Rectangle(Point(2, 3), 1, 1)
r4 = Rectangle(Point(0, 2), 2, 2)


class MyTime:

    def __init__(self, hrs=0, mins=0, secs=0):

        totalsecs = hrs * 3600 + mins * 60 + secs
        self.hours = totalsecs // 3600
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60

    def __add__(self, other):
        return MyTime(0, 0, self.to_seconds() + other.to_seconds())

    def __str__(self):
        return "Hours: {}, Minutes: {}, Seconds: {}".format(self.hours, self.minutes, self.seconds)

    def __gt__(self, other):
        return self.to_seconds() > other.to_seconds()

    def increment(self, seconds):
        totalsecs = self.to_seconds() + seconds
        # if totalsecs < 0:
        #     self.hours = 0
        #     self.hours = 0
        #     self.hours = 0
        # elif totalsecs >= 0:
        self.hours = totalsecs // 3600
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def after(self, time2):
        return self.to_seconds() > time2.to_seconds()

    def between(self, t1, t2):
        if t1.to_seconds() <= self.to_seconds() < t2.to_seconds():
            return True
        elif t2.to_seconds() <= self.to_seconds() < t1.to_seconds():
            return True
        return False


time1 = MyTime(0, 0, 600)
time2 = MyTime(0, 0, 500)
time3 = MyTime(0, 0, 400)

print(time3)
time3.increment(300)
print(time3)


def add_time(t1, t2):
    secs = t1.to_seconds() + t2.to_seconds()
    return MyTime(0, 0, secs)


def multadd(x, y, z):
    return x * y + z


def front_and_back(front):
    import copy
    back = copy.copy(front)
    back.reverse()
    print(str(front) + str(back))


class Card:
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["narfs", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.ranks[self.rank] + " of " + self.suits[self.suit]

    def __eq__(self, other):
        return self.cmp(other) == 0

    def __le__(self, other):
        return self.cmp(other) <= 0

    def __ge__(self, other):
        return self.cmp(other) >= 0

    def __gt__(self, other):
        return self.cmp(other) > 0

    def __lt__(self, other):
        return self.cmp(other) < 0

    def __ne__(self, other):
        return self.cmp(other) != 0

    def cmp(self, other):
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        return 0


class Deck:

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))

    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s = s + " " * i + str(self.cards[i]) + "\n"
        return s

    def print_deck(self):
        for card in self.cards:
            print(card)

    def shuffle(self):
        import random
        rng = random.Random()
        # num_cards = len(self.cards)
        # for i in range(num_cards):
        #     j = rng.randrange(i, num_cards)
        #     (self.cards[i], self.cards[j]) = (self.cards[j], self.cards[i])
        rng.shuffle(self.cards)

    def remove(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False

    def pop(self):
        return self.cards.pop()

    def is_empty(self):
        return self.cards == []


red_deck = Deck()
blue_deck = Deck()
print(red_deck)
