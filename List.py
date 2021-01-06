"""定义一个列表"""
variable = [1,2,3]
print(variable);
"""给列表的某一项设置值"""
variable[0] = 0
print(variable);
"""给列表结尾加上一个值"""
variable.append(4)
print(variable)
variable[0] = 1
"""给列表的某个位置插入一个值"""
variable.insert(0,0)
print(variable)
"""删除列表的某一项"""
del variable[0]
print(variable)
"""弹出列表的最后一项"""
variable.pop()
print(variable)
"""删除列表的某一项"""
variable.remove(2)
print(variable)
"""弹出列表的某一项"""
variable.pop(0)
print(variable)
"""给列表排序"""
variable = [9,8,7,6,5,4,3,2,1]
variable.sort()
print(variable)
"""正序"""
variable.sort(reverse = True)
print(variable)	
print(sorted(variable))
print(variable)
variable = [9,2,7,4,5,6,3,8,1]
print(variable)
variable.reverse()
print(variable)
print(len(variable))
print(variable[-1])

for i in variable:
	print(i)

print('\r');
for i in range(0,5):
	print(i)
print('\r');
max = max(variable)
print(max)
min = min(variable)
print(min)
sum = sum(variable)
print(sum)

variable = [value**2 for value in range(0,11)]
print(variable)
print(variable[0:5])
print(variable[:5])
print(variable[-2:])

for value in variable[2:-2]:
	print(value)

variable = [value for value in range(0,5)]
print(variable)
variable_copy = variable[:]
print(variable_copy)
variable.append(5)
print(variable)
print(variable_copy)
del variable_copy[0]
print(variable)
print(variable_copy)
variable_copy = variable
print(variable)
print(variable_copy)
del variable[0]
print(variable)
print(variable_copy)

if 1 in variable:
	print(1)

variable = []
if variable:
	print('success')
else:
	print('error')

print("\r")
variable = [value for value in range(0,5)]
key = 0
while key < len(variable):
	print(key)
	if variable[key] % 2 == 1:
		key += 1 
		continue
	else:
		key += 1 


print("\r");
data = []
while variable:
	data.append(variable.pop())
	print(data)
	print(variable)

print("\r");
variable = [1,1,2,1]
count = 1
while 1 in variable:
	variable.remove(1)
	print(count)
	count += 1
	




