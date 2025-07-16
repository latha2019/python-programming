import os
location = r"C:\Users\ltbx\Downloads\exercises.csv"
with open(location,'r') as f:
    lines = f.readlines()
    print(f"The content of CSV file '{location}':")
    for line in lines:
        print(line.strip())
    print(type(lines))