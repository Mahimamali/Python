# First code

PI = 3.14
radius = float(input('Input the radius of the circle: '))
area = PI * radius * radius
print("The area Of a Circle with radius",radius,"is:",area)

# Second code

filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))
