# This is my first python proram
#print
print("I like durian")
print("Its really good")


# variables
full_name = "khairina"
age = 22
gpa =3.37
is_student = True

print(f"Hello {full_name}" )
print(f"You are {age} years old")
print(f"Your GPA is {gpa}")
print(f"Are you a student? {is_student}")

if is_student:
    print("You are a student")
else:
    print("You are not a student")


#arithmetic operations
friends = 3

friends += 2
friends -= 3

print(friends)

#Typecasting
name = "khairina"
age = 22
gpa = 3.37
is_student = True

print(type(is_student))

#convert from float to int
gpa = int(gpa)
print(gpa) 

age = float(age)
print(age)

age = str(age)
print(age) 
print(type(age))

name = bool (name)
print(name)

