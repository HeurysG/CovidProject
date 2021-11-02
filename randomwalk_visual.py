import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Making a random walk and plotting the points :D

"""rw = RandomWalk()
rw.fill_walk()

plt.scatter(rw.x_values , rw.y_values , s=5 )"""


# Keep making new walks, as long as the program is active.

while True: 
	rw = RandomWalk(5000)
	rw.fill_walk()
	point_numbers = list(range(rw.num_points))
	plt.figure(dpi= 128 , figsize=(10,6))
	plt.scatter(rw.x_values, rw.y_values , c=point_numbers, cmap=plt.cm.Blues, edgecolor = 'none', s=5)
	
	# Emphasize first and last points
	plt.scatter(0, 0 , c='green', edgecolors= 'none', s = 15 )
	plt.scatter(rw.x_values[-1] , rw.y_values[-1] , c= 'red' , edgecolors = 'none', s=15)
	
	# remove the axes.
	
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)
	
	
	plt.show()
	
	keep_running = input("Make another walk? (y/n): ")
	keep_running_nws = keep_running.strip()
	if keep_running_nws == "n":
		break
		
	
