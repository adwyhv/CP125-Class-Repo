import pandas as pd


def promotion_candidates(filename):
    df = pd.read_csv(filename)
    # Calculate average performance
    average_performance = float(df['Performance'].mean())
    # Filter candidates with minimum years of service
    candidates_df = df[df['Years_Employed'] >= 2]
    return {
        "average_performance": average_performance,
        "min_years_required": 2,
        "candidate_count": len(candidates_df),
        "candidate_names": set(candidates_df['Name'])
    }

result = promotion_candidates("labs\lab09\data\employees.csv")
print(result)
# {
#     "average_performance": 78.5,
#     "min_years_required": 2,
#     "candidate_count": 12,
#     "candidate_names": {"John Smith", "Sarah Lee", "Michael Chen", ...}
# }