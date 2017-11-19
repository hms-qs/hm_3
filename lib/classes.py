# 变量类
# val 变量的值
# isCon 是否是常量
class Var:
	def __init__(self, val = ''):
		self.val = val;
		if(str.isupper(val[0])):
			self.isCon = True;
		else:
			self.isCon = False;
	def __str__(self):
		return 'Var: {{val:{0}, isCon: {1}}}'.format(self.val, self.isCon)
	__repr__ = __str__

# 断言类
class Predicate:
	def __init__(self, pre_str):
		s1 = pre_str.split('(');
		s1 = [s1[0]] + s1[1].split(')');
		s1 = [s1[0]] + s1[1].split(',');
		if s1[0][0] == '~':
			bo = -1
			s1[0] = s1[0][1:]
		else:
			bo = 1
		self.init(s1[0].strip(), s1[1:]);
	def __str__(self):
		var_str = '';
		for item in self.vars:
			var_str =  var_str + item.__str__() + ', ';
		return 'Predicate: {{name:{0}, vars: [{1}]}}'.format(self.name, var_str);
	def init(self, name, var_array = [], bo = 1):
		self.name = name;
		self.vars = [];
		for item in var_array:
			self.vars = self.vars + [Var(item)];
		if(bo == -1):
			self.bo = True
		else:
			self.bo = False
	def tel(pre):
		print('lal');

class Sentence:
	def __init__(self, sen_str):
		pre_str_list = sen_str.split('|');
		self.predicates = [];
		for pre_str in pre_str_list:
			self.predicates = self.predicates + [Predicate(pre_str)]
	def __str__(self):
		pre_str = '';
		for item in self.predicates:
			pre_str = pre_str + item.__str__() + ', ';
		return 'Sentence: {{predicates: [{0}]}}'.format(pre_str);

class KnowledgeBase:
	def __init__(self, sentences = []):
		self.sentences = sentences;
	def addSen(sen):
		self.sentences = self.sentences + [sen];
	def tell(sen):
		print('lal');

