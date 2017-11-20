def tell(self, Sen):
	for i in Sen.predicates:
		for j in self.predicates:
			##找到名字相同，正负相反的predict
			if i.name = j.name and i.bo + j.bo == 1:
				for k in range(len(i.vars)):
					flag = 0
					#对应都是常量有不同，不合法
					if i.vars[k].isCon and j.vars[k].isCon and i.vars[k].name != j.vars[k].name:
						break
					#存在一个常量一个变量对应，标记可以进行resolve
					if i.vars[k].isCon or j.vars[k].isCon:
						flag = 1
				if flag == 1:
					#深拷贝输入的sentence对象
					temp = copy.deepcopy(Sen)
					for n in range(len(i.vars)):
						#对于predicate的同一位置的vars[n],
						#如果这一位在可以resolve的predicate的vars中都是常量，本位置在其他的predica中不变
						if i.vars[n].isCon and j.vars[n].isCon:
							continue
						#else 遍历拷贝后sentence的所有predicate
						for m in range(len(temp.predicates)):
							#如果当前predicate是找到的可以resolve的predicate，跳过
							if temp.predicates[m].name == i.name or n >= len(temp.predicates[m].vars):
								continue
							#如果对应的自身predicate的本位制是常量，
							#则将深拷贝的输入sentence对应predicate的相同位置也变为常量，同时isCon变为True
							if j.vars[n].isCon:
								temp.predicates[m].vars[n].name = j.vars[n].name
								temp.predicates[m].vars[n].isCon = j.vars[n].isCon

						for l in range(len(self.predicates)):
							if self.predicates[l].name == j.name or n >= len(self.predicates[l].vars):
								continue
							if i.vars[n].isCon:
								pro = copy.deepcopy(self.predicates[l])
								pro.vars[n].name = i.vars[n].name
								pro.vars[n].isCon = i.vars[n].isCon
							## 将自身的predicate修改对应值加入到深拷贝中
							temp.predicates.append(pro)
					#删除值name与i一样（resolve）的predicate
					temp.predicates.remove(lambda x: x.name == i.name,temp.predicates)
				#寻找合并以后的sentence中相同predicate
					top = 0
					repeat = []
					for n in range(len(temp.predicates)):
						if top == 1:
							break
						for m in range(n,len(temp.predicates)):
							if top == 1:
								break
							if temp.predicates[n].name == temp.predicates[m].name:
								count = 0
								for l in range(len(temp.predicates[n].vars)):
									#相同位置上的值都是常量但是不相等，则本resolve不合法退出到最外层
									if temp.predicates[n].vars[l].isCon and temp.predicates[m].vars[l].isCon and temp.predicates[n].vars[l].name != temp.predicates[m].vars[l].name:
										top = 1
										break
									#如果所有位置常量都相,即重复，则只保留一个
									if temp.predicates[n].vars[l] == temp.predicates[m].vars[l]:
										count += 1
								if count == len(temp.predicates[n].vars):
									repeat.append(n)
					for n in repeat:
						temp.predicates.pop(n)
	return temp 


















