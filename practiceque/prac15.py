#WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with a empty dictionary and add one by one. Use subject name as key and marks as value.
Marks={}
mark1=int(input("Enter first subject marks: "))
mark2=int(input("Enter second subject marks: "))
mark3=int(input("Enter third subject marks: "))
Marks.update({"phy": mark1})
Marks.update({"chem": mark2})
Marks.update({"maths": mark3})
print(Marks)