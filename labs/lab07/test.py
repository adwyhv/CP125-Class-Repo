import csv

def append_new_students(new_file, target_file):
    new_student = open(new_file,'r',newline='')
    new_student_reader = csv.reader(new_student)
    
    final = open(target_file,'r',newline='')
    final_writer = csv.writter(final)

    next(new_student_reader)    

    result = []
    for row in new_student_reader:
     result.append((row[0],row[1]))
    
     final_writer.writerows(result)

    new_student.close()
    final.close()



    