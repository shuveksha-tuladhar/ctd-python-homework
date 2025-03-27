import pandas as pd

# Task 1: Introduction to Pandas - Creating and Manipulating DataFrames
task1_data = {
    'Name': ['Alice', 'Bob', 'charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

task1_data_frame = pd.DataFrame(task1_data)
print("Original data frame:")
print(task1_data_frame)

task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]
print("Data frame with salary:")
print(task1_with_salary)

task1_older = task1_with_salary.copy()
task1_older["Age"] +=1
print("Data frame with age increment:")
print(task1_older)

task1_older.to_csv("employees.csv", index=False)
print("task1_older saved to employees.csv")

# Task 2: Loading Data from CSV and JSON
task2_employees = pd.read_csv('employees.csv', delimiter=',', header=0)
print("task 2 employees:")
print(task2_employees)

json_employees = pd.read_json('additional_employees.json')
print("task 2 employees from JSON:")
print(json_employees)

more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print("Combined employees data frames:")
print(more_employees)

# Task 3: Data Inspection - Using Head, Tail, and Info Methods
first_three = more_employees.head(3)
last_two = more_employees.tail(2)
employee_shape = more_employees.shape
employee_info = more_employees.info()

print("task 3")
print(first_three)
print(last_two)
print(employee_shape)
print(employee_info)



