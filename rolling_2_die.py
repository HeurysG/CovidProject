import pygal
from die import Die


# Create 2 D6 dice.

die_1 = Die()
die_2 = Die()

# Make some rolls and store results in a list. 

 

results = [die_1.roll() + die_2.roll() for roll_num in range(10000)]
""" 
This here is the list comprehension, the other file rolling_die.py 
generated the list a different way. """

max_value = die_1.num_sides + die_2.num_sides 

	
frequencies = [results.count(value) for value in range(2, max_value + 1)]

# Visualize results

hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 10000 times."
hist.x_labels = list(range(2,13))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6' , frequencies)
hist.render_to_file('two_d6_freq.svg')


