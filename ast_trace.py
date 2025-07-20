import ast
from utils import resolve_path
from utils import wrap_input

class ContentTracer:
    def __init__(self, input_path='input.py'):
        self.f_path = resolve_path(input_path)
        self.tree = ast.parse(wrap_input(self.f_path))
    def print_tree(self, node=None, indent=0):
        if not node:
            node = self.tree

        print(" " * indent + f"{type(node).__name__} {node.__dict__}")
        for child in ast.iter_child_nodes(node):
            self.print_tree(child, indent + 1)
    def trace_vars(self):
        # Traverse and return dict of historical values of variables
        var_tokens = {}
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        var_name = target.id
                        val = ast.dump(node.value)
                        if isinstance(node.value, ast.Constant):
                            val = node.value.value
                        elif isinstance(node.value, ast.Name):
                            val = node.value.id
                        prefix = 'initialize'
                        if var_name not in var_tokens:
                            var_tokens[var_name] = []
                        else:
                            last_val = var_tokens[var_name][-1][1]
                            if val != last_val:
                                prefix = 'change'
                            else:
                                continue
                        var_tokens[var_name].append((val, node.lineno, prefix))
        return var_tokens