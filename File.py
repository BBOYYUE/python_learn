"""文件操作"""
filename = 'hello.py'
with open(filename,'w') as file_object:
	file_object.write("print('I love programming')\r\n")
with open(filename,'a') as file_object:
	file_object.write("print('I love zhaoyan')")

