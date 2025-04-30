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

# Task 4: Data Cleaning
dirty_data = pd.read_csv('dirty_data.csv', delimiter=',', header=0)
clean_data = dirty_data.copy()
print("Task 4 - Original Data:")
print(clean_data)

clean_data.drop_duplicates(inplace=True)
print("Data after removing duplicates:")
print(clean_data)

clean_data["Age"] = pd.to_numeric(clean_data['Age'], errors='coerce')
clean_data["Age"] = clean_data["Age"].fillna(clean_data["Age"].mean())
print("Data after converting Age and handling missing values:")
print(clean_data)

clean_data["Salary"] = clean_data["Salary"].replace("unknown", pd.NA)
clean_data["Salary"] = pd.to_numeric(clean_data["Salary"], errors="coerce")
print("Data after Salary to numeric and replace known placeholders (unknown, n/a) with NaN:")
print(clean_data)

clean_data["Salary"] = clean_data["Salary"].fillna(clean_data["Salary"].median())
print("Data after Fill Age which the mean and Salary with the median")
print(clean_data)

clean_data["Hire Date"] = pd.to_datetime(clean_data["Hire Date"], errors="coerce")
print("After converting to datetime:")
print(clean_data)

clean_data["Name"] = clean_data["Name"].str.strip().str.upper()
clean_data["Department"] = clean_data["Department"].str.strip().str.upper()
print("Data after removing whitespace and standardize Name and Department as uppercase")
print(clean_data)
