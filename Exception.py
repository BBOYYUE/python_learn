"""定义异常"""
try:
	print(5/0)
except ZeroDivisionError:
	print("You can't divide by zero!")

first_number = input('plese input first_number:')
second_number = input('plese input second_number:')
try:
	answer = int(first_number) / int(second_number)
except ZeroDivisionError:
	print("You can't divide by zero!")
else:
	print(answer)

filename = input('plese input filename:')
try:
	with open(filename) as f_obj:
		contents = f_obj.read()
except FileNotFoundError:
	msg = "Sorry,the file " + filename + "does not exist."
	print(msg)
else:
	print(contents)

def count_words(filename):
	"""计算一个文件大致包含多少个单词"""
	try:
		"""如果文件不存在会报异常"""
		with open(filename) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		# msg = "Sorry,the file " + filename + "does not exist."
		# print(msg)
		pass
	else:
		"""split() 根据一个字符串获取单词列表"""
		words =contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) + " words.")
