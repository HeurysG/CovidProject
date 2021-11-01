import matplotlib.pyplot as plt

squares = [1, 4 , 9 , 16 , 25 ] 

"""plt.plot(squares)
plt.show() is my first attempt, destroy quotes to see func work"""
input_values = [1,2,3,4,5] 
plt.plot(input_values, squares, linewidth = 5)

# Set chart title and label axes. 

plt.title("Square Numbers", fontsize = 24 )
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)

# Set size of tick labels.
plt.tick_params(axis='both' , labelsize = 14)

plt.show()

# the graph starts at a x-coordinate value of 0 .. not what we want so we must input 
# the input values ourself. 

input_values = [1,2,3,4,5] 
#then we modify the plt.plot command 


x_values = [1,2,3,4,5]
y_values = [1, 4 , 9 , 16 , 25 ] 

plt.scatter(x_values, y_values , s= 100)

# set chart title and axes

plt.title("Square Numbers in Scatter Plot" , fontsize = 24 )
plt.xlabel("Value" , fontsize = 14 ) 
plt.ylabel("Square of Value", fontsize=14)

plt.show()
