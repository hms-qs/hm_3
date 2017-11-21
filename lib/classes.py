import copy
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
	def replace(self, pre):
		#找到那个predicate
		sen_tar_pre = None
		new_sen = Sentence();
		new_sen.predicates = copy.deepcopy(self.predicates);
		for sen_pre in self.predicates:
			if(sen_pre.name == pre.name):
				sen_tar_pre = sen_pre;
				break;
		var_list = sen_tar_pre.vars + [];
		var_target_list = pre.vars;
		i = 0
		for var in var_list:
			for new_pre in new_sen.predicates:
				for new_pre_var in new_pre.vars:
					if(new_pre_var.val == var.val):
						new_pre_var.val = var_target_list[i].val;
			i += 1
		return new_sen;

	def equal(self, pre1, pre2):
		if pre1.name == pre2.name and pre1.bo != pre2.bo:
			for k in range(len(pre1.vars)):
				if pre1.vars[k].val != pre2.vars[k].val:
					if pre1.vars[k].isCon == False and pre2.vars[k].isCon ==False:
						continue
					else:
						return False
			return True
		return False

	def tell(self, Sen):
		for i in Sen.predicates:
			for j in self.predicates:
				##找到名字相同，正负相反的predict
				if i.name == j.name and ((i.bo and not j.bo) or (j.bo and not i.bo)):
					flag = 0
					flag1 = 0
					for k in range(len(i.vars)):
						#对应都是常量有不同，不合法
						if i.vars[k].isCon and j.vars[k].isCon and i.vars[k].val != j.vars[k].val:
							flag1 = 1
							break
						#存在一个常量一个变量对应，标记可以进行resolve
						if i.vars[k].isCon or j.vars[k].isCon:
							flag = 1
					if flag1 == 1:
						continue
					if flag == 1:
						#深拷贝输入的sentence对象
						temp = copy.deepcopy(Sen)
						pro = copy.deepcopy(self)
						down = 0
						for n in range(len(i.vars)):
							if down == 1:
								break
							if i.vars[n].isCon and j.vars[n].isCon:
								continue
							if j.vars[n].isCon:
								value = i.vars[n].val
								for q in range(len(temp.predicates)):
									for w in range(len(temp.predicates[q].vars)):
										if Sen.predicates[q].vars[w].val == value:
											if temp.predicates[q].vars[w].val == value:
												temp.predicates[q].vars[w].val = j.vars[n].val
												temp.predicates[q].vars[w].isCon = j.vars[n].isCon
											elif temp.predicates[q].var[w].val == j.vars[n].isCon:
												continue
											else:
												down = 1
												break

							if i.vars[n].isCon:
								value = j.vars[n].val
								for v in range(len(pro.predicates)):
									for y in range(len(pro.predicates[v].vars)):
										if self.predicates[v].vars[y].val == value:
											if pro.predicates[v].vars[y].val == value:
												pro.predicates[v].vars[y].val = i.vars[n].val
												pro.predicates[v].vars[y].isCon = i.vars[n].isCon
											elif pro.predicates[v].var[y].val == i.vars[n].isCon:
												continue
											else:
												down = 1
												break
									#pro.predicates[l].vars[n].val = i.vars[n].val
									#pro.predicates[l].vars[n].isCon = i.vars[n].isCon
								## 将自身的predicate修改对应值加入到深拷贝
						print(pro)
						print(temp)
						st = len(temp.predicates)
						sp = len(pro.predicates)
						case = 0
						locp = -1
						loct = -1
						for p in range(sp):
							if case ==1:
								break
							for q in range(st):
								if self.equal(pro.predicates[p],temp.predicates[q]):
									locp = p
									loct = q
									case = 1
									break
						if loct == -1 or locp == -1:
							break

						temp.predicates.pop(loct)


						for i in range(sp):
							if i != locp:
								plus = copy.deepcopy(pro.predicates[i])
								for g in range(len(plus.vars)):
									if not plus.vars[g].isCon:
										plus.vars[g].val += '0'
								temp.predicates.append(plus)

						top = 0
						repeat = []
						for n in range(len(temp.predicates)):
							if top == 1:
								break
							for m in range(n+1,len(temp.predicates)):
								if top == 1:
									break
								if temp.predicates[n].name == temp.predicates[m].name:
									count = 0
									for l in range(len(temp.predicates[n].vars)):
										#相同位置上的值都是常量但是不相等，则本resolve不合法退出到最外层
										if temp.predicates[n].vars[l].isCon and temp.predicates[m].vars[l].isCon and temp.predicates[n].vars[l].val != temp.predicates[m].vars[l].val:
											top = 1
											break
										#如果所有位置常量都相,即重复，则只保留一个
										if temp.predicates[n].vars[l] == temp.predicates[m].vars[l]:
											count += 1
									if count == len(temp.predicates[n].vars):
										repeat.append(n)
						for n in repeat:
							temp.predicates.pop(n)
						 ##print(temp)
						return temp
		return 0

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

	def isequal(self, sen1, sen2):
		if len(sen2.predicates) != len(sen1.predicates):
			return False
		else:
			for i in sen1.predicates:
				flag = 0
				for j in sen2.predicates:
					if i.name == j.name and i.bo == j.bo:
						flag = 1
						for k in range(len(i.vars)):
							if i.vars[k].isCon == j.vars[k].isCon and ((i.vars[k].val == j.vars[k].val and i.vars[k].isCon == True) or (i.vars[k].isCon == False)):
								continue
							else:
								return False
						break
				if flag == 0:
					return False
			return True

	def ask(self, sen):
		generate = copy.deepcopy(self)
		new = copy.deepcopy(sen)
		new.predicates[0].bo = not new.predicates[0].bo
		generate.addSen(new)
		iteration = 0
		while True:
			##print(generate.sentences
			size = len(generate.sentences)
			for i in range(size):
				for j in range(size):
					flag = 0
					res = generate.sentences[j].tell(generate.sentences[i])
					print(i+1)
					print(j+1)
					if res == 0:
						continue
					else:
						for m in generate.sentences:
							if self.isequal(res,m):
								flag = 1
								break
						if flag == 1:
							continue
						if len(res.predicates) == 0:
							return True
						else:
							print("dasd")
							generate.addSen(res)
			print("haha")
			iteration += 1
			#print(iteration)
			#print(size)
			if len(generate.sentences) == size or iteration == 10000:
				return False





		