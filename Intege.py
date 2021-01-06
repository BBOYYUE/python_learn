variable = 1
print(variable)
variable = variable+1
print(variable)
variable = variable**variable
print(variable)
print(variable/3)
print(variable%2)
print("整型数字可以通过str转成字符串然后和字符串拼接"+str(2))

if 1 > 2:
	print(1)
else:
	print(2)

if 1 > 2 and 2/0 > 0:
	print('error')

if 2 > 1 or 2/0 > 0:
	print('error')  

variable = 0
if variable:
	print('success')
else:
	print('error')

variable = 0
while variable < 10 :
	print(variable)
	variable +=1 
