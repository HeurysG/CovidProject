import json

def greet_user():
	"""Greet user by name."""
	filename = 'name.json'
	try: 
		with open(filename) as f_obj:
			name = json.load(f_obj)
	except FileNotFoundError:
		name = input("What is your name? ") 
		with open(filename, 'w') as f_obj:
			json.dump(name, f_obj) 
			print("We'll remember your name when you come back, " + name + "!")
	else:
		print("Welcome back, " + name + "!")
		
greet_user()


import json 

def get_stored_username():
	"""Get stored username if available."""
	
	filename = 'username1.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else: 
		return username
		
def greet_user():
	"""Greet user by name."""
	username = get_stored_username()
	if username:
		print("Welcome back, " + username + "!")
	else:
		username = input("What is your name?")
		filename = 'username1.json'
		with open(filename, 'w') as f_obj:
			json.dump(username, f_obj)
			print("We will remember you when you come back, " + username + "!")

greet_user()
print(get_stored_username())
