from sys import settrace

INPUT_PATH = 'input.py'

def tracer(frame, event, arg = None):
    depth = 0
    current_frame = frame
    while current_frame:
        depth += 1
        current_frame = current_frame.f_back
    if depth > 3: # working depth of wrapped input
        code = frame.f_code
        func_name = code.co_name
        line_no = frame.f_lineno

        if event == 'line':
            l_vars = frame.f_locals.copy()
            print(f"Line {line_no} → {l_vars}")
        elif event == 'return':
            l_vars = frame.f_locals.copy()
            print(f"Return from {func_name}() → {l_vars} at line no. {line_no}")
        else:
            print(f"A {event} encountered in {func_name}() at line no. {line_no}")

        return tracer
    return None

def wrap_input(f_path: str) -> str:
    with open(f_path, 'r') as f:
        f_cont = f.read()
    return f_cont

def main():
    code_str = wrap_input(INPUT_PATH)
    x = compile(code_str, INPUT_PATH, 'exec')

    settrace(tracer)
    exec(x)
    settrace(None)

if __name__ == '__main__':
    main()