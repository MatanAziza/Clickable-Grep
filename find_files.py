#!/usr/bin/env python3

import os
import sys

if __name__=="__main__":
    args:list = []
    for arg in sys.argv:
        args.append("".join([c for c in arg if c != '\\']))
    if len(args) == 1:
        print("Missing searched argument.\nPlease run the program with what you're looking for or with argument '--help' to learn how to use it.")
        sys.exit(1)
    elif len(args) > 3:
        print("Too much arguments were provided.\nPlease run the program with what you're looking for or with argument '--help' to learn how to use it.")
        sys.exit(1)
    one_arg = len(args) == 2
    if args[1] == '--help':
        print('help')
        sys.exit(0)
    where_to_search = os.getcwd() if one_arg else args[2] # Where you want to search
    folder: str = ""
    tab = where_to_search.split('/')
    folder = tab[-2] if not tab[-1] else tab[-1]
    os.system("touch files.txt")
    os.system(f"grep -rnw --include=*.py --include=*.c '{where_to_search}/' -e '.*{args[1]}.*'| sed 's/$/ 1/' >> files.txt")
    file = open("files.txt", "r")
    list_files = file.read().split("\n") # All occurences of searched string
    file.close()
    os.system("rm files.txt")
    gen = list(set([file_path[:file_path.index(":")] for file_path in list_files[:-1]])) # List of unique path from /home
    url_list = []
    for path in gen:
        if '/home' in path:
            url_list.append(f"file://{path}")
        else:
            url_list.append(f'file://{os.getcwd()}/{path}')
    print("\n".join(url_list))
    gen = [file_path[file_path.index(folder)+len(folder):] for file_path in gen] # Path from requested folder
    if not gen:
        print("\033[0;31mL'élément cherché n'existe pas dans le dossier et sous-dossiers!\033[1;37m")
    for i, file_path in enumerate(gen):
        path = file_path[file_path.index("/")+1:]
        print(f"\033[0;32mFile n°{i+1}: \033[0m", end='')
        print(f"\033]8;;{url_list[i]}\033\\{path}\033]8;;\033\\")
