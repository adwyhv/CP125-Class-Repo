# Lab 02 Exercise 4: Dynamic Parking Rate
# Write your code below:

def get_hourly_rate(vehicle_type, hour_24):
    if vehicle_type == "Electric":
        rate = 2.00
    elif vehicle_type =="Hybrid" :
        if hour_24 >= 22 or hour_24 <=6:
            rate = 2.00 
        else:
            rate = 5.00
    else:
        rate = 5.00
        
    return rate

# Test your code here
print("Testing Dynamic Parking Rate...")
