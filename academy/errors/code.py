def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be zero!")

    return dividend / divisor


grades = [55, 60, 95, 75]
Students = [
    {"name": "bob", "grades": [95, 97]},
    {"name": "john", "grades": [99, 94]},
    {"name": "chris", "grades": [96, 96]}
]

print("Welcome to the grade program")
try:
    for student in Students:
        grades = student.get("grades")
        name = student.get("name")
        average = divide(sum(grades), len(grades))
        print(f"The average grade of {name} is {average}.")
except ZeroDivisionError as e:
    print(f"{name} dont have any grades in the list.")
else:
    print("All student average has been calculated.")
finally:
    print("Thank you!")
