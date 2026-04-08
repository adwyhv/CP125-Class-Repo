import pandas as pd


def critical_inventory(filename):
    df = pd.read_csv(filename)

result = critical_inventory("data/inventory.csv")
print(result)
# {
#     "total_products": 50,
#     "critical_count": 7,
#     "critical_products": {"Laptop_X1", "Monitor_Pro", "Keyboard_Mech", ...}
# }
