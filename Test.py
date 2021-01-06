import unittest 
from name_function import get_formatted_name
class NamesTestCase( unittest. TestCase): 
	"""测试 name_ function. py""" 
	def test_first_last_name(self): 
		"""能够 正确地 处理 像 Janis Joplin 这样 的 姓名 吗？""" 
		formatted_name = get_formatted_name('janis','joplin') 
		self.assertEqual(formatted_name,'Janis Joplin')
		"""可用的断言有很多"""
		"""assertEqual(a,b) 核实a == b"""
		"""assertNotEqual(a,b) 核实a != b"""
		"""assertTrue(x) 核实x为True"""
		"""assertFalse(x) 核实x为False"""
		"""assertIn(item,list) 核实item在list中"""
		"""assertNotIn(item,list) 核实item不在list中"""

"""运行测试"""
unittest.main()

