def merge_lists(file1, file2, output_file):
    list1 = open(file1, 'r')
    list2 = open(file2, 'r')
    output = open(output_file, 'w')

    names_list1 = set(list1.readlines())
    names_list2 = set(list2.readlines())
    completed_list = list(names_list1|names_list2)
    completed_list = sorted(completed_list)

    result = 0
    for name in completed_list:
        output.write(name)
        result +=1

    list1.close()
    list2.close()
    output.close()
    return result

result = merge_lists("lab08\exercise2\data\list1.txt","lab08\exercise2\data\list2.txt")
print(f"Unique name : {result}")