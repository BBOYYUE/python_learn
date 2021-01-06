"""定义函数"""
def sayHello():
	"""say hello world """
	print("Hello World")

sayHello()

"""带参数的函数"""
def sayHello(name):
	print("Hello "+name)

sayHello('崔跃')

"""不按顺序,按参数名称传参"""
def sayHello(name,massage):
	print(massage + " " + name)

sayHello(massage="hello",name="cuiyue")

"""不按顺序,按参数名称传参"""
def sayHello(name='zhaoyan',massage=''):
	print(massage + " " + name)

sayHello(massage="hello")

"""第一参数按顺序,其余两个按参数名称"""
def sayHello(name='zhaoyan',massage='',robot=''):
	print(robot + "'say:" + massage + " " + name)

sayHello('cuiyue',robot="zhaoyan",massage="hello")

"""传入列表"""
def sayHello(name):
	name.append('zhaoyan')
	for value in name:
		print("Hello "+value)

	return name

name = ['cuiyue']
print(sayHello(name))

"""传入列表的复制"""
"""python的函数总是传引用"""
def sayHello(name):
	name.append('zhaoyan')
	for value in name:
		print("Hello "+value)

	return name

name = ['cuiyue']
print(sayHello(name[:]))
print(name)

"""将传入的多个参数打包成列表"""
def sayHello(*name):
	for value in name:
		print("Hello "+value)

sayHello('zhaoyan','cuiyue')

"""多余的参数被打包成了列表"""
def sayHello(message,*name):
	for value in name:
		print(message + " " + value)

sayHello('hello','zhaoyan','cuiyue')

"""实参** 将字典展开作为了多个参数.形参** 将多个参数打包成字典"""
def sayHello(**values):
	print(values)
	for key,val in values.items():
		print(key + ":" + val)

args = {'a':'a','b':'b'}
sayHello(**args)
sayHello(c='c')

"""实参** 将列表展开作为了多个参数.形参** 将多个参数打包成列表"""
def sayHello(*names):
	print(names)
	for name in names:
		print("hello "+name)

args = ['a','b','c']
sayHello(*args)
sayHello('d')

"""将有三个值的列表或字典展开成为三个参数"""
def sayHello(a,b,c):
	print(a)
	print(b)
	print(c)

args = ['a','b','c']
sayHello(*args)
print('\r')
args = {'a':'a','b':'b','c':'c'}
sayHello(**args)

"""定义一个淘气的函数,在任意函数前面@它 @它的函数就会执行两次"""
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def return_greeting(name):
    print("Creating greeting")
return_greeting('cuiyue')

@do_twice
def return_say_hello(*names):
	for name in names:
		print('Hello '+name)

args = ['a','b','c']
return_say_hello(*args)

