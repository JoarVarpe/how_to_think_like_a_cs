class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

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
        pass


r = Rectangle(Point(3, 0), 10, 5)
print(r.contains(Point(0, 0)))
print(r.contains(Point(3, 3)))
print(r.contains(Point(3, 7)))
print(r.contains(Point(3, 5)))
print(r.contains(Point(3, 4.9999)))
print(r.contains(Point(-3, -3)))


