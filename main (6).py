def sort_students(students):
  students.sort(key=lambda x: x.cgpa, reverse=True)


# Define a Student class
class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


# Example usage
students = [
    Student("praveen", "A911", 3.8),
    Student("priya", "A082", 3.9),
    Student("kalai", "A063", 3.7)
]

sort_students(students)

# Print the sorted list of students
for student in students:
  print(student.name, student.roll_number, student.cgpa)
