  

students = (
    ("James", 20, 85),
    ("Summet", 21, 90),
    ("Modi", 22, 9),
)
def average_grade(records):
    if not records:
        return 0
    total_grade = sum(record[2] for record in records)  
    number_of_students = len(records)  
    return total_grade / number_of_students 
print("Average Grade:", average_grade(students))