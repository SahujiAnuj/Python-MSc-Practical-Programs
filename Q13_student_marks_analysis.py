# Program 13: Student Marks Analysis using Dictionary

# ----------- STUDENT DATA -----------

students = {
    "Alice": 88,
    "Bob": 73,
    "Charlie": 95,
    "Diana": 91,
    "Eve": 67
}

print("=" * 60)
print("STUDENT MARKS ANALYSIS")
print("=" * 60)

# Display data
print("\nStudent Records:")
for name, marks in students.items():
    print(f"{name:<10} : {marks}")


# ----------- TOPPER -----------

topper = max(students, key=students.get)
print("\nTopper :", topper, "-", students[topper])


# ----------- AVERAGE -----------

average = sum(students.values()) / len(students)
print("Average Marks :", round(average, 2))


# ----------- SORTING -----------

# Ascending
asc = sorted(students.items(), key=lambda x: x[1])

# Descending
desc = sorted(students.items(), key=lambda x: x[1], reverse=True)

print("\nSorted (Ascending):")
for name, marks in asc:
    print(name, ":", marks)

print("\nSorted (Descending):")
for name, marks in desc:
    print(name, ":", marks)

print("=" * 60)
