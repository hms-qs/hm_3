from lib.io import *
from lib.classes import Var, Predicate, Sentence, KnowledgeBase;


inputs = input_file('./inputs/inputs1.txt');
output_file(inputs['kb'], './outputs/kb.txt');
kb = inputs['kb']

# test sentence tell
s = Sentence('A(x,y,z) | B(x,y)');
print(s.tell(Sentence('~A(Jone,Alice, Joe)')));