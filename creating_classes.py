class Dog(): 
	"""A simple attempt to model a dog."""
	def __init__(self, name, breed, age):
		"""Initialize name and age attributes.""" 
		self.name = name
		self.breed = breed 
		self.age = age
		
	def sit(self):
		"""Simulate a dog sitting in response to the command."""
		print(self.name.title() + " is now sitting.")
		
	def roll_over(self):
		"""Simulate a dog rolling over in response to the command."""
		print(self.name.title() + " is now rolling over.")	

my_dog = Dog('cooper' , 'golden retriever', 2)
print("My dog " + my_dog.name.title() + " is a good boi and he is " + str(my_dog.age) + " years old.")

my_dog.sit()
my_dog.roll_over()
Dog.roll_over(my_dog)

my_dog2 = Dog('scrappy', 'chihuahua' , 10)
my_dog2.sit()
my_dog2.roll_over()

print("My dog " + my_dog2.name.title() + " is a good boi and he is " + str(my_dog2.age)
      + " years old.")

# Time to modify attributes of classes 

class Car(): 
	"""A simple attempt to represent a car."""
	
	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car."""
		self.make = make 
		self.model = model 
		self.year = year
		self.odometer_reading = 0 
	
	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model 
		return long_name.title()
	
	def read_odometer(self): 
		"""Print a statement showing the car's mileage."""
		print("This car has " + str(self.odometer_reading) + " miles on it.") 
	def update_odometer(self,mileage):
		"""Set the odometer reading to the given value... Version 2 uses logic since 
		an odometer can't be rolled back """
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else: 
			print("You can't roll back an odometer!")
	def increment_odometer(self,miles):
		self.odometer_reading += miles
			    

my_new_car = Car('audi' , 'a4' , 2016 ) 
print(my_new_car.get_descriptive_name()) 
my_new_car.read_odometer()

# There are 3 ways to change the value of an attribute .. you can change the value 
#directly through an instance , set the value through a method, or increment the 
#value through a method. 

# Modifying an Attribute's value directly 

my_new_car.odometer_reading = 23 
my_new_car.read_odometer()

# to mody an attribute's value through a method you need to update the class and add
# a method to it such as this ... it updates the attribute for me and I won't have to 
# access the attribute directly, I can just pass the new value to the method which will
#update it internally
""" def update_odometer(self, mileage):
     self.odometer_reading = mileage """

my_new_car.update_odometer(39)
my_new_car.read_odometer()
my_new_car.update_odometer(37)

# Making a child class from the parent class Car 

class Battery(): 
	"""A simple attempt to model a battery for an electric car."""
	
	def __init__(self, battery_size=70):
		"""Initialize the battery's attributes."""
		self.battery_size = battery_size
	
	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print("This car has a " + str(self.battery_size) + "-kWh battery.")



class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles."""
	def __init__(self, make, model, year):
		"""Initialize attributes of the parent class
		Then initialize attributes specific to an electric car."""
		super().__init__(make,model, year)
		self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model S', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()






class Computer():
	"""Represent aspects of a computer, specific to a computer only."""
	def __init__(self, hard_drive, video_card , processor, motherboard):
		self.hard_drive = hard_drive
		self.video_card = video_card
		self.processor = processor
		self.motherboard = motherboard
		
	def size(self):
		print("The size of the hard drive is " + self.hard_drive)   
		
	def video_card_info(self):
		print("The video card is a " + self.video_card.title())
		
	def processor_info(self):
		print("This processor is a " + self.processor.title())
		
	def motherboard_info(self):
		print("This motherboard is a " + self.motherboard.title())
		
my_computer = Computer('Samsung SSD' , 'Nvidia GTX 1070' , 'Intel Core i5-4670k', 'Intel Z390 HDMI SATA')
my_computer.video_card_info()
my_computer.size()
my_computer.motherboard_info()
my_computer.processor_info()



