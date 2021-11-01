prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = " " 
while message != 'quit':
	message = input(prompt)
	
	if message != 'quit':
		print(message)
		

signal = True
while signal: 
	message = input(prompt)
	
	if message == 'quit':
		signal = False
	else :
		print(message)

current_number = 0 

while current_number < 20 : 
	current_number += 1
	if current_number %2 == 0 :
		continue
	print(current_number)
	

unconfirmed_users = ['heurys', 'stanley' , 'angie'] 
confirmed_users = [] 

while unconfirmed_users: 
	current_user = unconfirmed_users.pop()
	
	print("Verifying user: " + current_user.title())
	confirmed_users.append(current_user)
print("\nAll the following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())

