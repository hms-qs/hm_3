from lib.classes import Var, Predicate, Sentence, KnowledgeBase
import json


def input_file(file_str):
	file = open(file_str)
	ques_num = int(file.readline().strip())
	ques_list = []
	for i in range(0, ques_num):
		line = file.readline().strip()
		ques_list = ques_list + [line]
	sen_num = int(file.readline().strip())
	kb = KnowledgeBase();
	for i in range(0, sen_num):
		line = file.readline().strip()
		kb.addSen(Sentence(line))
	return {
		'ques_num': ques_num,
		'ques_list': ques_list,
		'kb': kb
	}

def output_file(data, file_str):
	f = open(file_str, 'w');
	f.write(data.__str__())
	f.close()