import pandas as pd


def compare_averages(filename):
    data = pd.read_csv(filename)
    student_dict = {}
    math_average = data['Math'].mean()
    science_average = data['Science'].mean()
    english_average = data['English'].mean()
    best_subject = max()
    return student_dict

result = compare_averages("data/students.csv")
print(result)
# {
#     "Math": 84.0,
#     "Science": 82.9,
#     "English": 84.4,
#     "best_subject": "English",
#     "worst_subject": "Science"
# }

