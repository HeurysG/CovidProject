digits = (3, 4, 'two') 

print(digits.index('two'))


s = 'lmao,wtf,u,dumb,brother'

y= 'raining {arg1} and {arg2}'.format(arg1=input('What would u like it to rain?')
, arg2=input('What else?')) 

print(y)


num = [ 2 , 4 , 6 , 8 , 10 ]

def min_max(nums):
	return min(nums) , max(nums)
	
min_num, max_num = min_max(num)
print(min_max(num))
