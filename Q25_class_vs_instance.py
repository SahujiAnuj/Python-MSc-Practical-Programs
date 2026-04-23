# Program 25: Class Variables vs Instance Variables

class Student:
    # --- Class Variables (Shared by all students) ---
    school_name = "Python High School"
    total_students = 0

    def __init__(self, name, roll_no):
        # --- Instance Variables (Unique to each student) ---
        self.name = name
        self.roll_no = roll_no
        
        # Increment shared counter whenever a new student is created
        Student.total_students += 1

    def show_details(self):
        print(f"Name: {self.name} | Roll: {self.roll_no} | School: {Student.school_name}")

# --- Main Program ---

# Creating instances
s1 = Student("Alice", 101)
s2 = Student("Bob", 102)

print(f"Total Students: {Student.total_students}\n")

# Proving school_name is shared
print("Original school for all:")
s1.show_details()
s2.show_details()

# Modifying the Class Variable (Changes it for everyone)
Student.school_name = "Global Tech Institute"

print("\nAfter changing Student.school_name:")
s1.show_details()
s2.show_details()

# Modifying through an instance (Shadowing - Only affects that object)
s1.school_name = "Private Academy"

print("\nAfter s1.school_name = 'Private Academy':")
print(f"s1 school: {s1.school_name}") # Unique to s1 now
print(f"s2 school: {s2.school_name}") # Still uses the Class variable
