# Lab 02 Exercise 1: Road Trip Budgeter
# Write your code below:

def is_budget_sufficient(one_way_km, km_per_liter, price_per_liter, budget):
    round_trip = one_way_km * 2 
    total_fuel = round_trip / km_per_liter
    total_price = total_fuel * price_per_liter
    if budget >= total_price:
        return True
    else:
        return False

    # TODO: Implement this function
    # Calculate round trip cost and checks if within budget
    pass

# Test your code here
print("Testing Road Trip Budgeter...")