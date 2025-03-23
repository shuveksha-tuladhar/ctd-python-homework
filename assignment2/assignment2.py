# Task 2: Read a CSV File
import traceback
import csv
import os
import custom_module
from datetime import datetime

def read_employees():
    employees_dict = {}
    rows = []
    try:
        with open('../csv/employees.csv', 'r') as file:
            reader = csv.reader(file)
            employees_dict["fields"] = next(reader)
            for row in reader:
                rows.append(row)
            employees_dict["rows"] = rows
        return employees_dict
    
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = [f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}' for trace in trace_back]
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")

employees = read_employees()
print(employees)

# Task 3: Find the Column Index
def column_index(column_header):
    return employees["fields"].index(column_header)

employee_id_column = column_index("employee_id")
print(employee_id_column)

# Task 4: Find the Employee First Name
def first_name(row_number):
    index = column_index("first_name")
    return employees["rows"][row_number][index]

print(first_name(3))

# Task 5: Find the Employee: a Function in a Function
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches=list(filter(employee_match, employees["rows"]))
    return matches

print(employee_find(5))
    
# Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):
    matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
    return matches

print(employee_find_2(6))

# Task 7: Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
    employees["rows"].sort(key = lambda row: row[column_index("last_name")])
    return employees["rows"]

print(sort_by_last_name())

# Task 8: Create a dict for an Employee
def employee_dict(fields):
    # result_dict = {}
    return {key: value for key, value in zip(employees["fields"][1:], fields[1:])}

print('task8')
sample_row = employees["rows"][0]
print(employee_dict(sample_row)) 

# Task 9: A dict of dicts, for All Employees
def all_employees_dict():
    return {employee[0]: employee_dict(employee) for employee in employees["rows"]}

print(all_employees_dict())

# Task 10: Use the os Module
def get_this_value():
    return os.getenv('THISVALUE') 

print(get_this_value())

# Task 11: Creating Your Own Module
def set_that_secret(word):
    return custom_module.set_secret(word)

set_that_secret('happy')
print(custom_module.secret)

# Task 12: Read minutes1.csv and minutes2.csv
def read_csv_file(file_path):
    result_dict = {}
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        result_dict["fields"] = next(reader)  
        result_dict["rows"] = [tuple(row) for row in reader]  
    return result_dict

def read_minutes():
    minutes1_dict = read_csv_file('../csv/minutes1.csv')
    minutes2_dict = read_csv_file('../csv/minutes2.csv')
    return minutes1_dict, minutes2_dict

minutes1, minutes2 = read_minutes()

print(minutes1)
print(minutes2)

# Task 13: Create minutes_set
def create_minutes_set():
    minutes1_set = set(minutes1["rows"])  
    minutes2_set = set(minutes2["rows"]) 
    return minutes1_set.union(minutes2_set) 

minutes_set = create_minutes_set()
print(minutes_set)

# Task 14: Convert to datetime
def create_minutes_list():
    minutes_list = list(minutes_set)
    minutes_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list))

    return minutes_list

minutes_list = create_minutes_list()
print(minutes_list)

# Task 15: Write Out Sorted List
def write_sorted_list():
    sorted_minutes = sorted(minutes_list, key=lambda x: x[1])
    converted_list = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), sorted_minutes))

    with open('./minutes.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        writer.writerows(converted_list)

    return converted_list

converted_data = write_sorted_list()
print(converted_data)