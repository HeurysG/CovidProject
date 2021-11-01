import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values] 

plt.scatter(x_values , y_values , c=y_values , cmap= plt.cm.Blues , edgecolor = 'none' ,  s = 40 ) 

plt.title("Square Numbers in Scatter Plot" , fontsize = 24 )
plt.xlabel("Value" , fontsize = 14 ) 
plt.ylabel("Square of Value", fontsize=14)

plt.axis([ -100 , 1100 , -100000 , 1100000]) 
plt.show()

# to save as a file, instead of plt.show() use 
# plt.savefig('any_name.png' , bbox_inches = 'tight' ) 

# the argument bbox_inches = 'tight' is used to trim extra white space from the plot
# we can omit if we want the extra white space 
