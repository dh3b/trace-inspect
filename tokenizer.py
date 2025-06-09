from sys import settrace
from pathlib import Path
from collections import defaultdict

def resolve_path(file_path) -> str:
    if not file_path:
        raise ValueError("Path cannot be empty")
        
    path_obj = Path(file_path)
    if not path_obj.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    if not path_obj.is_file():
        raise ValueError(f"Path is not a file: {file_path}")

    abs_path = str(path_obj.resolve())
    return abs_path

class ExecutionTracer:
    def __init__(self, input_path='input.py'):
        self.f_path = resolve_path(input_path)
        self.tokens = defaultdict(list)
        
    def __wrap_input(self) -> str:
        with open(self.f_path, 'r') as f:
            self.f_cont = f.read()
        return self.f_cont
    
    def __trace_code(self, frame, event, arg=None):
        depth = 0
        current_frame = frame
        while current_frame:
            depth += 1
            current_frame = current_frame.f_back
            
        if depth > 3:  # working depth of wrapped input
            code = frame.f_code
            func_name = code.co_name
            line_no = frame.f_lineno

            l_vars = frame.f_locals.copy()
            for key, val in l_vars.items():
                if not self.tokens[key] or self.tokens[key][-1] != val:
                    self.tokens[key].append(val)

            if event == 'line':
                print(f"Line {line_no} → {l_vars}")
            elif event == 'return':
                print(f"Return from {func_name}() → {l_vars} at line no. {line_no}")
            else:
                print(f"A {event} encountered in {func_name}() at line no. {line_no}")

            return self.__trace_code
        return None
    
    def tokenize(self):
        code_str = self.__wrap_input()
        compiled_code = compile(code_str, self.f_path, 'exec')
        
        settrace(self.__trace_code)
        exec(compiled_code)
        settrace(None)
        
        return self.tokens

if __name__ == '__main__':
    src_x = ExecutionTracer('input.py')
    tokens = src_x.tokenize()
    print(tokens)