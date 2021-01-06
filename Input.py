Variable = input('请输入你的名字:')
print("Hello "+Variable)
Variable = input('请输入一个数字:')
print(int(Variable))

Variable = ""
while Variable != 'quit':
	Variable = input("请输入指令-1:")
	if Variable != 'quit':
		print(Variable)

Variable = True
while Variable:
	Message = input("请输入指令-2:")
	if Message != 'quit':
		print(Message)
	else:
		Variable = False

