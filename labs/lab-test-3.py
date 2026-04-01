import csv
def calc_display_average():
    f = open("bmi.csv","r", newline="")
    reader = csv.reader(f)
    print("Gender, height , weight, bmi")
    total_height = 0
    count = 0
    for row in reader :
        print(row)
        total_height = total_height + float(row[1])
        count += 1
    total_average = total_height/ count 
    f.close()
def add_data(gender,height,weight, bmi):
    gender = input("Gender :")
    height = input("Height :")
    weight = input("Weight :")
    bmi = input("bmi: ")
    f = open("bmi.csv","a+", newline="" )
    
    f.close()
    print("New data added.\n")

