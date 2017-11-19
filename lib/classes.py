# class Var
# val {str} 变量的值
# isCon {bool} 是否是常量
class Var:
	def __init__(self, val = ''):
		if(val == ''):
			return
		self.val = val.strip();
		if(str.isupper(val[0])):
			self.isCon = True;
		else:
			self.isCon = False;
	def __str__(self):
		return '{{"val": "{0}", "isCon": "{1}"}}'.format(self.val, self.isCon)
	__repr__ = __str__

# class Predicate
# name {str} 断言的名字
# vars {list} 变量数组
class Predicate:
	def __init__(self, pre_str = ''):
		if(pre_str == ''):
			return 
		s1 = pre_str.strip().split('(');
		s1 = [s1[0]] + s1[1].split(')');
		s1 = [s1[0]] + s1[1].split(',');
		if s1[0][0] == '~':
			bo = -1
			s1[0] = s1[0][1:]
		else:
			bo = 1
		self.init(s1[0].strip(), s1[1:], bo);
	def __str__(self):
		var_str = '';
		i = 0;
		var_len = len(self.vars);
		for item in self.vars:
			var_str =  var_str + item.__str__();
			i = i + 1;
			if(i < var_len):
				var_str = var_str + ',';
		return '{{"name": "{0}", "vars": [{1}], "bo": "{2}"}}'.format(self.name, var_str, self.bo);
	__repr__ = __str__
	def init(self, name, var_array = [], bo = 1):
		self.name = name;
		self.vars = [];
		for item in var_array:
			self.vars = self.vars + [Var(item)];
		if(bo == 1):
			self.bo = True
		else:
			self.bo = False

# class Sentence
# predicates {List} 断言数组
# tell {func} 输入一个sentence,输出fact/空集/或者没有结果
class Sentence:
	def __init__(self, sen_str = ''):
		if(sen_str == ''):
			return
		pre_str_list = sen_str.strip().split('|');
		self.predicates = [];
		for pre_str in pre_str_list:
			self.predicates = self.predicates + [Predicate(pre_str)]
	def __str__(self):
		pre_str = '';
		i = 0;
		pre_len = len(self.predicates);
		for item in self.predicates:
			pre_str = pre_str + item.__str__();
			i = i + 1;
			if(i < pre_len):
				pre_str = pre_str + ',';
		return '{{"predicates": [{0}]}}'.format(pre_str);
	__repr__ = __str__
	def tell(self, sen):
		#Todo
		print()
# class KnowledgeBase
# sentences {List} Sentence数组
# ask {func} 输入一个Predicate, 输出True/False
class KnowledgeBase:
	def __init__(self, sentences = []):
		self.sentences = sentences;
	def __str__(self):
		sen_str = '';
		i = 0;
		sen_len = len(self.sentences);
		for item in self.sentences:
			sen_str = sen_str + item.__str__();
			i = i + 1;
			if(i < sen_len):
				sen_str = sen_str + ',';
		return '{{"sentences": [{0}]}}'.format(sen_str);
	__repr__ = __str__
	def addSen(self, sen):
		self.sentences = self.sentences + [sen];
	def ask(sen):
		#Todo
		print()