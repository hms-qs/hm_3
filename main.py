from lib.io import *
from lib.classes import Var, Predicate, Sentence, KnowledgeBase;


inputs = input_file('./inputs/inputs1.txt');
output_file(inputs['kb'], './outputs/kb.txt');
kb = inputs['kb']
ql = inputs['ques_list']
#print(ql)

print(kb.isequal(Sentence('~A(a,b)|~B(Cat,L)|C(David)'),Sentence('C(David)|~B(Cat,L)|~A(x,y)')))


#print(Sentence('A(Bob,x,x)|B(x,y)').tell(Sentence('~A(y,Alice,y)|C(x,y)')))
#for i in ql:
##print(kb.ask(ql))



