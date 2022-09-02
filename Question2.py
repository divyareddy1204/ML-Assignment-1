Dog = {}  # creating dictionary named Dog
# adding properties to the dictionary Dog
Dog.update({"color": "brown", "name": "Tannie", "breed": "pomeranian", "legs": "four", "age": 4})
print(Dog)  # printing the Dog dictionary
Student ={}  # creating dictionary named Student
# adding properties to the dictionary Student
Student.update({"first_name": "Hailey", "last_name": "Marshall", "gender": "female", "age": 29,
                "martial status": "single", "skills": ["flying", "dancing", "driving"],
                "country": "New Zealand", "address": "xxx"})
print(Student)  # printing the Student dictionary
print("length of student dictionary - ", len(Student))  # prints the length of Student dictionary

# values of skills
print("values of skills - ", Student["skills"])
# data types of skills
dt = [type(k) for k in Student["skills"]]
print("Data types - ", dt)
# Adding values to the skills
Student["skills"].append('swimming')
Student["skills"].append("running")
# printing keys
print("keys - ", list(Student.keys()))
# printing values
print("values - ", list(Student.values()))
