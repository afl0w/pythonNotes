#user input for the lengths of three sides of a triangle.
print("Enter the lengths of the three triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

#if else statement 
if x == y == z:
	print("This is a Equilateral triangle")
else:
	print("This is not a Equilateral triangle")