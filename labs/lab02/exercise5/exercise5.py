def is_valid_triangle(side1,side2,side3):
    if side1 + side2> side3:
        return True
    elif side1+ side3 >  side2:
        return True
    elif side2 + side3 > side2:
        return True
    else:
        return False
    