from lib.io import *
from lib.classes import Var, Predicate, Sentence, KnowledgeBase;


inputs = input_file('./inputs/inputs1.txt');
output_file(inputs['kb'], './outputs/kb.txt');
kb = inputs['kb']
s = Sentence('~D(x,y) | ~Q(y) | C(x,y)');
print(s.tell(Sentence('Q(Joe)')))

# test sentence tell
'''
s = Sentence('~B(x,y) | ~C(x,y) | A(x)');
print(s.tell(Sentence('B(John,Alice)')));


s = Sentence('~B(x,y) | ~C(x,y) | A(x)');
print(s.tell(Sentence('B(John,Alice)')));