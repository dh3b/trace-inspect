from exec_trace import ExecutionTracer
from ast_trace import ContentTracer

def main():
    src_x = ExecutionTracer(depth_threshold=4)
    src_y = ContentTracer()
    x = src_x.tokenize()
    print(x)
    src_y.print_tree()

if __name__ == '__main__':
    main()