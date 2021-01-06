"""字典的定义"""
Variable = {"Me":"崔跃","MyLove":"赵琰"}
print(Variable['Me'])

"""遍历字典"""
for key ,val in Variable.items():
	print(key+'=>'+val)

"""获取字典的键"""
for key in Variable.keys():
	print(key)

"""获取字典的值"""
for val in Variable.values():
	print(val)

"""字典总是无序的,可以在遍历之前先给键排序"""
Variable = {"a":"A","b":"B","c":"C"}
for key in sorted(Variable.keys()):
	print(Variable[key])

"""将字典的键和值保存到列表"""
VariableList = []
for key,val in Variable.items():
	VariableList.append(key.lower())
	VariableList.append(val.lower())

print(VariableList)

"""集合类似于列表,但是其中的值不能重复"""
"""将列表转为集合"""
Variable = set(VariableList)
print(Variable)
"""将字典转为集合"""
Variable = {"a":"A","b":"B","c":"C","c":"C"}
Variable = set(Variable)
print(Variable)

