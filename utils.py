from pathlib import Path

def resolve_path(f_path) -> str:
    if not f_path:
        raise ValueError("Path cannot be empty")
        
    path_obj = Path(f_path)
    if not path_obj.exists():
        raise FileNotFoundError(f"File not found: {f_path}")
    if not path_obj.is_file():
        raise ValueError(f"Path is not a file: {f_path}")

    abs_path = str(path_obj.resolve())
    return abs_path

def wrap_input(f_path) -> str:
    with open(f_path, 'r') as f:
        f_cont = f.read()
    return f_cont