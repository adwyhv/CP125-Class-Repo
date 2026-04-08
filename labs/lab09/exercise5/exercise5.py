import pandas as pd


def high_performers(filename):
    df = pd.read_csv(filename)
    high_performers_df = df[df['Science'] > 80]
    return {
        "count": len(high_performers_df),
        "names": set(high_performers_df['Name'])
    }

result = high_performers("labs\\lab09\\data\\students.csv")
print(result)
# {
#     "count": 8,
#     "names": {"Ali", "Sara", "Hassan", "Fatima", "Omar", "Layla", "Yusuf", "Amira"}
# }