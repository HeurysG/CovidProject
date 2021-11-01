try:
	print(5/0)
except ZeroDivisionError:
	print("You can't divide by zero!")

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

"""while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q': 
		break
	second_number = input("Second number: ")
	if second_number == 'q':
		break
	answer = int(first_number)/ int(second_number)
	print(answer)"""
	
# This case cannot handle division by zero, it causes it to crash 
# So we must make a try and except block here 

while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q': 
		break
	second_number = input("Second number: ")
	if second_number == 'q':
		break
	try:
		answer = int(first_number)/ int(second_number)
	except ZeroDivisionError:
		print("You can't divide by 0!")
	else:
		print(answer)

	
title = "Alice in Wonderland"
title.split()
# split method separates a string into parts wherever 
