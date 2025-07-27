import os
from clang.cindex import Index, CursorKind

CPP_SOURCES_DIR = os.path.join(os.path.dirname(__file__), 'cpp_sources')
COMPILER_ARGS = ['-x', 'c++', '-w']

def find_global_vars(cpp_file_path):
    index = Index.create()

    tu = index.parse(cpp_file_path, COMPILER_ARGS)
    root_cursor = tu.cursor

    global_vars = []
    def traverse_ast(node):
        if node.kind == CursorKind.VAR_DECL:
            if node.semantic_parent and node.semantic_parent.kind == CursorKind.TRANSLATION_UNIT:
                global_vars.append(node.spelling)

        for child in node.get_children():
            traverse_ast(child)


    traverse_ast(root_cursor)
    return sorted(set(global_vars))


def main():
    all_files = os.listdir(CPP_SOURCES_DIR)

    cpp_files = sorted([f for f in all_files if f.endswith('.cpp')])

    for filename in cpp_files:
        full_path = os.path.join(CPP_SOURCES_DIR, filename)
        global_variables = find_global_vars(full_path)

        vars_string = " ".join(global_variables)
        with open('output.txt', 'a') as f:
            print(f"{filename} {vars_string}", file=f)


if __name__ == "__main__":
    main()