import ast
from utils import resolve_path
from utils import wrap_input

class ContentTracer:
    def __init__(self, input_path='input.py'):
        self.f_path = resolve_path(input_path)
        self.tree = ast.parse(wrap_input(self.f_path))
    def print_tree(self):
        for node in ast.walk(self.tree):
            print(node)
            print(node.__dict__)
            print("children: " + str([x for x in ast.iter_child_nodes(node)]) + "\\n")