# Task 1: Hello
def hello():
    return "Hello!"
hello()

# Task 2: Greet with a Formatted String
def greet(name):
    return("Hello, " + name + "!")
greet("John")

# Task 3: Calculator
def calc(num1, num2, operation="multiply"):
    try:
        operations = {
            "add": num1 + num2,
            "subtract": num1 - num2,
            "multiply": num1 * num2,
            "divide": num1 / num2 if num2 != 0 else "You can't divide by 0!",
            "modulo": num1 % num2 if num2 != 0 else "Error: Modulo by zero",
            "int_divide": num1 // num2 if num2 != 0 else "Error: Integer division by zero",
            "power": num1 ** num2
        }
    except TypeError:
        return("You can't multiply those values!")
    return operations.get(operation, "Error: Invalid operation")
    
try: 
    print("Select an operator: add, subtract, multiply, divide, modulo, int_divide and power. Else mulitply will be used as default")
    num1 = input("Enter first number: " )
    num2 = input("Enter second number: " )
    operation = input("Enter operator: " ).lower()  
    result = calc(float(num1), float(num2), operation)
    print(result)
except OSError:
    print(OSError)
except ValueError:
    print(ValueError)

# Task 4: Data Type Conversion
def data_type_conversion(data_value, data_type):
    try:
        match data_type:
            case "float":
                converted_data_value = float(data_value)
            case "str":
                converted_data_value = str(data_value)
            case "int":
                converted_data_value = int(data_value)
            case _:
                print(f"Invalid data type: {data_type}")
        print (f"The data value {data_value} converted to {data_type} type: {converted_data_value}")
        return converted_data_value
    except ValueError:
        return (f"You can't convert {data_value} into a {data_type}.")

try:
    d_value = input("Enter the value to convert: ")
    d_type = input("Enter data type (float, int, str): ")
    result = data_type_conversion(d_value, d_type)
    print(result)
except OSError:
    print(OSError)

# Task 5: Grading System, Using *args
def grade(*args):
    try:
        if not args:
            return "No grades provided."
        
        if not all(isinstance(i, (int, float)) for i in args):
            return "Invalid data was provided."
        
        total_sum = sum(args)
        total_number = len(args)
        average = total_sum/total_number
        match average:
            case _ if average>= 90:
                grade = "A"
            case _ if average<= 89 and average>=80:
                grade = "B"
            case _ if average<= 79 and average>=70:
                grade = "C"
            case _ if average<= 69 and average>=60:
                grade = "D"
            case _ if average< 60:
                grade = "F"
            case _:
                grade = "Invalid grade"
        print(f"Your grade is: {grade}")
        return grade
    except Exception:
        return "Invalid data was provided."

grade(90,95,96,89)
grade("abc",95,4)
grade(4,55,2,3,5,6,10,13)

# Task 6: Use a For Loop with a Range
def repeat(str, count):
    result = ""
    for _ in range(count):
        result = result + str
    return result 

print(repeat("hello", 5))

# Task 7: Student Scores using **kwargs
def student_scores(criteria, **kwargs):
    if criteria == "best":
        if not kwargs:
            return "No students provided."
        best_student = None
        highest_score = float('-inf')  
        for student, score in kwargs.items():
            if score > highest_score:
                highest_score = score
                best_student = student
        return best_student

    elif criteria == "mean":
        if not kwargs:
            return 0  
        return sum(kwargs.values()) / len(kwargs)

    else:
        return "Invalid criteria. Use 'best' or 'mean'."

print(student_scores("best", Sam=88, John=70, Charlie=92, Alice=95))
print(student_scores("mean", Sam=88, John=70, Charlie=92, Alice=95)) 

# Task 8: Titleize with String and List Operations
def titleize(text):
    words = text.split()
    little_words = {"a", "on", "an", "the", "of", "and", "is", "in"}
    
    for i, word in enumerate(words):
        if i == 0 or i == len(words)-1 or word.lower() not in little_words:
            words[i] = word.capitalize()
        else:
            words[i] = word.lower()
    return " ".join(words)

print(titleize("the lord of the rings and harry potter"))

# Task 9: Hangman with more String Operations
def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result
print(hangman("alphabet", "ab"))
print(hangman("california", "ai"))

# Task 10: Pig Latin, Another String Manipulation Exercise
def pig_latin(text):
    vowels = "aeiou"
    words = text.split()
    pig_latin_words = []
    
    for word in words:
        if word[0] in vowels:
            pig_latin_words.append(word + "ay")
        elif word.startswith("qu"):
            pig_latin_words.append(word[2:] + "quay")
        else:
            first_vowel_index = -1
            for i, letter in enumerate(word):
                if letter in vowels:
                    first_vowel_index = i
                    break
                if word[i:i+2] == "qu":  
                    first_vowel_index = i + 2
                    break
            if first_vowel_index == -1: 
                pig_latin_words.append(word + "ay")
            else:
                consonants = word[:first_vowel_index]
                rest = word[first_vowel_index:]
                pig_latin_words.append(rest + consonants + "ay")

    return " ".join(pig_latin_words).lower()

print(pig_latin("apple"))  
print(pig_latin("string")) 
print(pig_latin("queen"))  
print(pig_latin("the quick brown fox")) 
print(pig_latin("rhythm")) 
print(pig_latin("square")) 
print(pig_latin("Square")) 