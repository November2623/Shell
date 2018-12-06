#!/usr/bin/env python3
import os
#https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
"""
PATH expansion:
tidle => $HOME
paramater => ${  } => PATH and $ => valuable
"""


def handle_tidle(command):
    """
    handle tidle in 4 basic case:
    ~. ~-, ~+, ~{+,-}[number, string]

    """
    path = os.environ["HOME"]

    if command[0] == "~":
        return path
    elif command[0] == "~+":
        return os.environ["PWD"]
    elif command[0] == "~-":
        if "OLDPWD" in os.environ.keys():
            return os.environ["OLDPWD"]
        else:
            return command
    elif command[0].startswith("~+") is True or command[0].startswith("~-") is True:
        if command[0][2:].isdigit() is False:
            print("%s: command not found" % command[0])
            return [' ']
        else:
            """
            implement pushd later => saved
            implement popd later => delete
            implement dirs later => show
            don't need to implement????????
            """
            # bash: dirs: directory stack empty
            return command# or result
    elif "/" in command[0] and command[0].startswith("~") is True:
        return [path + str(command[0][1:])]
    else:
        return str(command[0])


def count_character_in_sub_command(sub_command, character):
    """
    Count any character you want
    """
    count = 0
    for char in sub_command:
        if char == character:
            count += 1
    return count


def get_sub_cmd_paramater(argument):
    """
    Find ${....} in command and return index starts-end
    """
    start = argument.index('${')
    end = argument.index('}')
    return [start+2, end]


def get_sub_cmd_dollar_charecter(argument):
    """
    Find $var in command and return index starts-end
    """
    start = argument.index('$')
    end = len(argument)
    return [start+1, end]


def get_variable(command, dic_var):
    for cmd in command:
        if "=" not in cmd and len(command > 1):
            print("%s: command not found" %cmd)
            return [' ']
    for cmd in command:
        key = cmd.split("=")[0]
        value = cmd.split("=")[1]
        dic_var.update({key: value})
        print(dic_var)
    return [' ']


def get_sub_cmd_brace(argument):
    """
    Find {.....} in command and return index starts-end
    """
    if "{" in argment and "}" in argument:
        start = argument.index('{')
        end = argument.index('}')
        return [start+1, end]
    return [0, len(argument)]


def handle_parameter(command, dic_var):
    """
    _parameter expansions with 2 basic cases
          + $PARAMETER
          + ${PARAMETER}
    """
    parse_variable = []
    cmd = command[0].split('$')

    for key in cmd:
        if key.startswith("{") is True and key.endswith("}") is True:
            key = key[1:-1]
        if key in dic_var.keys():
            parse_variable.append(dic_var[key])
            
    return ["".join(parse_variable)]

