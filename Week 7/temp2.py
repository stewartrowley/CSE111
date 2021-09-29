students = ["joey", "emily", "fred", "fred" ]

user_student = input("Please enter your favorite student: ")
# students.append(user_student)
# students.insert(1, user_student)
# students_copy = students.copy()
hogwarts_students = ["hermione", "ron", "harry"]
students.extend(hogwarts_students)
# user_to_find = input("What student are you looking for? ")
# print(students.count(user_to_find))


for i, val in enumerate(students):
    
    students[i] = val.title()

# print(students)
# students.pop(3)

# print(students.index("fred"))
# students.remove("fred")
students.sort()
print(students)
students.reverse()

print(students)
  

