class Dog():
	"""狗狗类"""

	def __init__(self,name,age):
		self.name = name
		self.age = age

	def sit(self):
		"""小狗蹲下"""
		print(self.name.title() + " is now sitting.")

	def roll_over(self):
		"""小狗打滚"""
		print(self.name.title() + " rolled over!")


class Car():
	"""汽车类"""

	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""返回整洁的描述性信息"""
		long_name = str(self.year) + " " + self.make + " " + self.model
		return long_name.title()

	def read_odometer(self):
		"""打印一条指出汽车里程的消息"""
		print("This car has " + str(self.odometer_reading) + " miles on it.")

	def update_odometer(self,mileage):
		"""修改里程数"""
		if mileage > self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("里程数不能往回调")

	def  increment_odometer(self,mileage):
		"""里程数增加"""
		if mileage > 0:
			self.odometer_reading += mileage

class ElectricCar(Car):
	"""电动汽车"""

	def __init__ (self,make,model,year):
		"""初始化父类的属性"""
		super().__init__(make,model,year)
		# self.battery_size = 70 
		"""使用一个类作为属性"""
		self.battery = Battery(70)

	def describe_battery(self):
		"""打印电池容量信息"""
		return self.battery.describe_battery()
		# print("This car has a " + str(self.battery_size) + "-kWh battery.")

class Battery():
	def __init__ (self,battery_size):
		self.battery_size = battery_size

	def describe_battery():
		print("This car has a " + str(self.battery_size) + "-kWh battery")


my_car = Car('audi','a4',2016)
print(my_car.get_descriptive_name())
my_car.read_odometer()