pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
	pets.remove('cat')
print(pets)


responses = {} 

# set a flag to indicate that polling is active
polling_active = True

while polling_active:
	#prompt for the person's name and response
	name = input("\nWhat is your name? ") 
	response = input("Which mountain would you like to climb someday? ")
	#store the response in a dictionary
	responses[name] = response 
	# Find out if anyone else is going to take the poll. 
	repeat = input("Would you like to let another person respond? (yes/no) ")
	if repeat == 'no':
		polling_active = False
# Polling is complete. Show the results.

print("\n--- Poll Results ---")
for name,response in responses.items():
	print(name + " would like to climb " + response + "." )



favorite_brands = {} 

polling_active = True 
while polling_active: 
	name = input("\nWhat is your name?") 
	brand = input("\nWhat is your favorite shoe brand?") 
	
	favorite_brands[name] = brand
	repeat = input("Would you like to let another persond respond? (yes/no) ")
	
	if repeat == 'no' : 
		polling_active = False
# Polling is complete now :D 

print("\n --- Poll Results --- ") 
if name,brand in responses.items() : 
	print(name.title() + " prefers the shoe brand of " + brand.title() + ".") 
	
