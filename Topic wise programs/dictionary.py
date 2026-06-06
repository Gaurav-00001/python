student={
    "name" : "Gaurav", "subjects" :{ "Phy": 94, "chem" : 75, "math": 80}
}
print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))
student.update({"age" : 20 })

print(student)
