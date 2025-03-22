# Task 2: Read a CSV File
import traceback
import csv

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







