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