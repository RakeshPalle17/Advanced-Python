# Demonstrate the usage of namdtuple objects

import collections


def main():
    # TODO: create a Point namedtuple
    Point = collections.namedtuple("Point", 'x y')
    p1 = Point(x=10, y=20)
    p2 = Point(x=100, y=40)
    print(p1)
    print(p2.x, p2.y)


    # TODO: use _replace to create a new instance
    print(p2._replace(x=50))
    print(p2.x, p2.y)
    


if __name__ == "__main__":
    main()
