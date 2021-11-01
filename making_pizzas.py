import pizza

pizza.make_pizza( 16, 'pepperoni')
pizza.make_pizza(20, 'extra cheese' , 'pepperoni' , 'pineapple')

# to import modules(functions made in other files) you use module_name.function_name(.....) 

# you can also import like this ... from module_name import function_name
# or from module_name import function_0 , function_1 , function_2 

from pizza import make_pizza 

make_pizza(18 , 'extra sauce' )

# you can import it and give it an alias ... a different unique altername name similar to a nickname

from pizza import make_pizza as mp 

mp(22 , 'tomatoes' , 'bacon')

import pizza as p 

p.make_pizza(16 , 'pepperoni')

# using asterisk tells it to import all functions from a module .. so , 

from pizza import * 

