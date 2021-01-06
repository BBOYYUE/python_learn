"""字符串的定义"""
print("这是一个字符串");
print("python 的字符串可以使用\'也可以使用\"")
print("python 使用+号"+"拼接字符串")
variable = "strip()可以去掉字符串末尾多余的空白 "
print(variable+'.')
print(variable.strip()+'.')
variable = "Hello"
if variable.lower() == "hello":
	print(variable)

if variable != 'hello':
	print(variable)

variable = ''
if variable:
	print('success')
else:
	print('error')


