from sys import settrace
from utils import resolve_path
from utils import wrap_input
from collections import defaultdict
import logging

class ExecutionTracer:
    def __init__(self, input_path='input.py', log_level=logging.INFO, depth_threshold=3):
        self.f_path = resolve_path(input_path)
        logging.basicConfig(
            level=logging.INFO,
            format='[%(levelname)s] %(message)s'
        )

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)

        self.tokens = defaultdict(list)
        self.depth_threshold = depth_threshold
    
    def __trace_code(self, frame, event, arg=None):
        depth = 0
        current_frame = frame
        while current_frame:
            depth += 1
            current_frame = current_frame.f_back
            
        if depth > self.depth_threshold:  # working depth of wrapped input
            code = frame.f_code
            func_name = code.co_name
            line_no = frame.f_lineno

            l_vars = frame.f_locals.copy()
            for key, val in l_vars.items():
                last_token = self.tokens[key][-1] if self.tokens[key] else None
                append = False

                if not last_token:
                    prefix = 'initialize'
                    append = True
                elif last_token[0] != val:
                    prefix = 'change'
                    append = True

                if append:
                    self.tokens[key].append([val, line_no, prefix])

            if event == 'line':
                self.logger.info(f"Line {line_no} → {l_vars}")
            elif event == 'return':
                self.logger.info(f"Return from {func_name}() → {l_vars} at line no. {line_no}")
            else:
                self.logger.info(f"A {event} encountered in {func_name}() at line no. {line_no}")

            return self.__trace_code
        return None
    
    def tokenize(self):
        code_str = wrap_input(self.f_path)
        compiled_code = compile(code_str, self.f_path, 'exec')
        
        settrace(self.__trace_code)
        exec(compiled_code)
        settrace(None)
        
        return self.tokens