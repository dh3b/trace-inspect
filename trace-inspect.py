from tokenizer import ExecutionTracer

def main():
    src_x = ExecutionTracer('input.py', depth_threshold=4)
    tokens = src_x.tokenize()
    print(tokens)

if __name__ == '__main__':
    main()