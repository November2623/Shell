import re, os


def handle_bracket(string):
    i = 0
    while i < (len(string) - 1):
        if string[i] == '[':
            temp = ""
            for j in range(i+1, len(string)):
                if(string[j] == ']'):
                    break
                temp += string[j]
            temp = '[' + temp + ']'
            replace = '(' + temp.lower() + '|'
            replace += temp.upper() + ')'
            string = string.replace(temp, replace)
            i += len(replace) - 1
        i += 1
    return string


def findMatching(pattern, string):
    """result[0]: list file, result[1]: list dir"""
    try:
        message_nonexist = "'{0}': No such file or directory".format(pattern)
        result = [[], []]
        if(pattern[0] != "*"):
            pattern = "^" + pattern
        pattern = handle_bracket(pattern)
        pattern = pattern.replace("*", ".*")
        pattern = pattern.replace("?", "[A-Za-z0-9]")
        for ele in string:
            matches = re.finditer(pattern, ele)
            if len(list(matches)) > 0:
                if os.path.isfile(ele):
                    result[0].append(ele)
                else:
                    result[1].append(ele)
        if(len(result[0]) ==0 and len(result[1]) == 0):
            return message_nonexist
        return result
    except:
        return message_nonexist


def handle_ls(lst):
    try:
        if type(lst) != list:
            print("ls: cannot access {0}".format(lst))
            exit()
        if len(lst[0]) > 0:
            lst[0].sort(key=lambda str: str.lower())
        if len(lst[1]) > 0:
            lst[1].sort(key=lambda str: str.lower())
        for file in lst[0]:
            print(file, end='  ')
        if len(lst[1]) > 0:
            print()
        for dir in lst[1]:
            print()
            print(dir, end=":")
            if(len(os.listdir(dir)) != 0):
                 print()
            print('  '.join(sorted(os.listdir(dir))))
    except:
        raise("Error: 'handle_ls' function")

lst = [f for f in os.listdir() if not f.startswith('.')]
lst = findMatching("../", lst)
# print(lst)
handle_ls(lst)
