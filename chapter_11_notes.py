class Point:
    """ Point class represents and manipulates x, y coords """

    def __init__(self, x=0, y=0):
        """Create a new point at the origin"""
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """Compute the distance from the origin"""
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def to_string(self):
        return "({}, {})".format(self.x, self.y)

    def halfway(self, target):
        """ Return the halfway point between myself and the target"""
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx, my)


def midpoint(p1, p2):
    mx = (p1.x + p2.x) / 2
    my = (p1.y + p2.y) / 2
    return Point(mx, my)


p = Point(4, 2)
q = Point(6, 3)
r = Point()
print(p.x, p.y, q.x, q.y, r.x, r.y)
print(p.distance_from_origin())
