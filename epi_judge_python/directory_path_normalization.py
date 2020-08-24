from test_framework import generic_test


def shortest_equivalent_path(path: str) -> str:
    # TODO - you fill in here.
    stack = []
    root = False
    if path[0] == '/':
        root = True

    for name in path.split('/'):
        if not name or name == '.':
            continue
        if name == '..':
            if root and len(stack)==0:
                continue
            elif not root and (len(stack) == 0 or stack[-1] == '..'):
                stack.append('..')
            else:
                stack.pop()
        else:
            stack.append(name)
    
    if root:
        result = "/"
        result += "/".join(stack)
        return result
    return "/".join(stack)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
