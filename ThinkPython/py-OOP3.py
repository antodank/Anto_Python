class Point(object):
    """Represents a point in 2-D space."""
    def print_point(p):
        """Print a Point object in human-readable format."""
        #print "(%g, %g", % (p.x, p.y)
        print("X=%d, Y=%s" % (p.x, p.y))

class Rectangle(object):
    """Represents a rectangle.
    """
    def find_center(rect):
        """Returns a Point at the center of a Rectangle."""
        p = Point()
        p.x = rect.corner.x + rect.width/2.0
        p.y = rect.corner.y + rect.height/2.0
        return p

    def grow_rectangle(rect, dwidth, dheight):
        rect.width += dwidth
        rect.height += dheight
    
def main():
    blank = Point()
    blank.x = 3
    blank.y = 4
    print('blank')
    blank.print_point()

    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0

    center = box.find_center()
    print('center')
    center.print_point()

    # print box.width
    # print box.height
    # print 'grow'
    # grow_rectangle(box, 50, 100)
    # print box.width
    # print box.height


if __name__ == '__main__':
    main()