# Lab 02 Exercise 8: Bouncing Ball Simulation
# Write your code below:

def calculate_bounce_height(current_height):
    """Calculate next bounce height (80% of current)."""
    next_height = current_height * 0.8
    return next_height
    

def is_ball_stopped(height):
    """Return True if height < 1, False otherwise."""
    if height < 1:
        return True
    else:
        return False

def simulate_bouncing_ball(start_height):
    bounce_count = 0
    distance = start_height
    current_height=start_height
    while is_ball_stopped(current_height) == False:
        bounce_height=calculate_bounce_height(current_height)
        bounce_count +=1
        distance=bounce_height*2 + distance
        current_height=calculate_bounce_height(current_height)
    return (bounce_count,distance)

# Test your code here
print("Testing Bouncing Ball Simulation...")
