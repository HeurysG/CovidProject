message = input("Tell me something, and I will repeat it back to you: " )
print(message)

name = input("Please enter your name: ")
print("Hello, " + name + "!") 	

prompt = "If you tell us who you are, we can personalize the messages you see." 
prompt += "\nWhat is your first name? " 

name = input(prompt) 
print("Hello, " + name + "!")


age = input("How old are you? " ) 

age = int(age)
print(age >= 18)

height = input("How tall are you, in inches? ") 
height = int(height) 

if height >= 36 : 
	print("\nYou are tall enough to ride!")
else:
	print("\nSorry, you are too short!")

# practicing dictionary stuff lol 

leaguechampions = {'vayne': {'class': 'marksman',
    'range' : 550, 
    'ms' : 330 ,
    'ad' : 79,
    'ap' : 0 },
    'nami': {'class': 'support',
    'range' : 525,
    'ms': 335,
    'ad': 49,
    'ap': 30 },
    'zed': {'class' : 'assassin',
    'range': 125, 
    'ms': 345 , 
    'ad': 80, 
    'ap': 0},
    }

for champion,stats in leaguechampions.items():
	if champion == 'vayne' and stats['range'] > 250: 
		print(champion.title() + " is a hyperscaling marksman.")
	elif champion == 'nami' :
		print(champion.title() + " is an enchanter support.")
	elif champion == 'zed' :
		print(champion.title() + " is an assassin.")
	
 # back to input and while loops
 
 
