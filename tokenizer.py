from sys import settrace

def tracer(frame, event, arg = None):
    code = frame.f_code
    func_name = code.co_name
    line_no = frame.f_lineno

    print(f"A {event} encountered in \
    {func_name}() at line number {line_no} ")

    return tracer

settrace(tracer)

# wrapper func here