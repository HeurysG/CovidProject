import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
	rw = RandomWalk()
	rw.fill_walk()
	
	point_numbers = list(range(rw.num_points))
	
	plt.figure(dpi= 128 , figsize=(10,6))
	
	plt.plot(rw.x_values, rw.y_values , linewidth=1)
	
	
	# remove the axes.
	
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)
	
	
	plt.show()
	
	keep_running = input("Make another walk? (y/n): ")
	keep_running_nws = keep_running.strip()
	if keep_running_nws == "n":
		break
			
	

