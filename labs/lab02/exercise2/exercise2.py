# Lab 02 Exercise 2: Camping Logistics
# Write your code below:

import math

def calculate_event_cost(participants, tent_capacity, tent_price, meal_price):
   n_tent = math.ceil(participants / tent_capacity)
   total_tent_price = n_tent * tent_price
   total_meal_price = meal_price * participants
   total_cost = total_tent_price + total_meal_price
   return total_cost

print("Testing Camping Logistics...")
