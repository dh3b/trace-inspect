# Trace Inspect

Trace Inspect is a Python tool for analyzing and visualizing variable changes and code execution paths in Python scripts. It provides both runtime and static analysis using two main modules:

## Features

- **ExecutionTracer** (`exec_trace.py`):
  - Dynamically traces variable changes and function calls during code execution.
  - Records when variables are initialized or changed.
  - Logs execution events including line execution and function returns.

- **ContentTracer** (`ast_trace.py`):
  - Parses Python source code using the Abstract Syntax Tree (AST).
  - Walks through assignments and reconstructs the history of variable values.
  - Identifies variables tested in conditional branches.

## Usage

1. Place your target Python script in the project directory.
2. Run `trace_inspect.py` to analyze the script:
   ```bash
   python trace_inspect.py
   ```
3. The output will display both the runtime variable trace and the static variable history.

## File Overview

- `trace_inspect.py`: Main entry point; runs both tracing modules and prints results.
- `exec_trace.py`: Runtime execution tracer.
- `ast_trace.py`: Static AST-based tracer.
- `input.py`: The Python script to be analyzed.
- `utils.py`: Utility functions for path resolution and input handling.

## Example Output

```
{'x': [(1, 3, 'initialize'), (0, 5, 'change')], 'y': [(2, 4, 'initialize')]}
{'x': [(3, 'initialize'), (5, 'change')], 'y': [(4, 'initialize')]}
```

## License

This project is licensed under the terms of the LICENSE file in the repository.
