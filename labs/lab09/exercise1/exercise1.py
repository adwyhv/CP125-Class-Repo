import pandas as pd


def explore_data(filename):
    data = pd.read_csv(filename)
    total_students = len(data)
    subjects = list(data.columns[1:])
    math_average = data['Math'].mean()
    highest_math_student = data.loc[data['Math'].idxmax(), 'Name']

    dict_result = {
        'total_students': total_students,
        'subjects': subjects,
        'math_average': float(math_average),
        'highest_math_student': highest_math_student,
    }
    print(dict_result)

explore_data("lab09/data/students.csv")
