import pickle
import shelve


class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Marks:", self.marks)


student1 = Student("Rahul", 101, 85)

with open("student.pkl", "wb") as file:
    pickle.dump(student1, file)

print("Object saved using pickle.")

with open("student.pkl", "rb") as file:
    restored_student = pickle.load(file)

print("\nRestored Object using pickle:")
restored_student.display()


with shelve.open("student_db") as db:
    db["student1"] = student1

print("\nObject saved using shelve.")

with shelve.open("student_db") as db:
    restored = db["student1"]

print("\nRestored Object using shelve:")
restored.display()