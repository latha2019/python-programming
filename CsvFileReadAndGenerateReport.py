# import os
# import csv
# location = r"C:\Users\ltbx\Downloads\exercises.csv"
# with open(location,'r') as f:
#     lines = f.readlines()
#     print(f"The content of CSV file '{location}':")
#     for line in lines:
#         print(line.strip())
#     print(type(lines))

""" Program to read csv file and creat report 
Name	 Course 	 TotalMarks
john 	 python 	 190
ben 	 shell 	 285
carl 	 shell 	 170
ben 	 python 	 155
john 	 shell 	 90
"""

def csv_file_read(filepath):
    data = []
    with open(location,'r') as f:
        """Read the csv file & return the data
        """
        lines = f.readlines()
        print(f"The content of CSV file '{location}':")
        for line in lines:
            print(line.strip())
        # print(type(lines))

        for line in lines:
            parts = line.strip().split(",")
            name = parts[0].strip()
            course = parts[1].strip()
            test = parts[2].strip()
            marks = int(parts[3].strip())
            data.append((name, course, marks))

    return data

def calculate_totals(data):
    result = {}
    for name, course, marks in data:
        key = (name, course)
        if key in result:
            result[key] += marks
        else:
            result[key] = marks
    return result

location = r"C:\Users\ltbx\Downloads\exercises.csv"
data = csv_file_read(location)
# print(data)
result = calculate_totals(data)
# print(result)
print("---------------Students report---------------------")
print("Name\t Course \t TotalMarks\t")
print("---------------------------------------------------")
for (name, course), marks in result.items():
    print(name,"\t",course,"\t",marks)

