def check_collision(x1, y1, w1, h1, x2, y2, w2, h2):
    # Calculate the right and bottom edges of each rectangle
    if x1 < x2+w2 and x2 < x1+w1 and y1 < y2+w2 and y2<y1+w1:
        return True
    else:
        return False
    
    