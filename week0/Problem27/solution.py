def reduce_file_path(path):
    path = path.split('/')
    final_path = []

    for part in path:
        if part == '..':
            if final_path:
                final_path.pop() 
        elif part != '.' and part != '/':
            final_path.append(part)

    return '/' + '/'.join(filter(lambda x: x != '', final_path))