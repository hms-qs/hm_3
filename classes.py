# 变量类
# type 0 代表变量， 1代表常量
# val 变量的值
class Var:
	def __init__(self, type, val = None):
		self.type = type;
		self.val = val;

# 断言类
class Predicate:
	def __init__(self, name, var_num, var_array = None):
		if(var_array != None and len(var_array) != var_num):
			raise Exception('Predicate 初始化错误: 1');
		self.name = name;
		self.var_num = var_num;
		self.var_array = var_array;
	def getVal(self):
		if(len(self.var_array > 0)):
			return False;
		for i in self.var_array:
			if(i.type == 1):
				return True;
		return False;


a = Var(1, 2);
b = Var(0);


pre1 = Predicate('A', 2);

print(pre1.getVal())