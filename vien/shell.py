#!/usr/bin/env python3
from basic import *
import os



def handle_minish(command, run_minish):
    valid_command = ["cd", "printenv", "export", "unset", "exit"]
    if command[0] == valid_command[0]:
        handle_cd(command)
    elif command[0] == valid_command[1]:
        handle_printenv(command)
    elif command[0] == valid_command[2]:
        handle_export(command)
    elif command[0] == valid_command[3]:
        handle_unset(command)
    elif command[0] == valid_command[4]:
        run_minish = handle_exit(command)
    elif command[0] not in valid_command:
        handle_other_action(command)
    return run_minish


def single_quote(string):
    return string[1:len(string)-1]


def double_quote(string):
    # "the order: \\ -> \n -> \t -> \r -> \hhh ->\xnn -> \b"
    return handle_backspace(string)

def parse_oct_hex(string):
    # \nnn   the eight-bit character whose value is the octal value nnn (one to three digits)
    # \xHH   the eight-bit character whose value is the hexadecimal value HH (one or two hex digits)
    # \cx    a control-x character (non-complete)
    for i in range(len(string) - 3):
        if string[i] == "\\":
            if string[i+1:i+4].isdigit() and int(string[i+1:i+4]) < 178:
                string = string[:i] + chr(int(string[i+1:i+4])) + string[i+4:]
            elif string[i+1] == "x" and ord(string[i+2]) >=  48 and ord(string[i+2]) <= 55 and ((string[i+3]).isdigit() or (string[i+3]).isalpha()):
                char_replace = bytes.fromhex('4C').decode('utf-8')
                string = string[:i] + char_replace + string[i+4:]
    return string


def parse_horizontaltab_newline(string):
    for i in range(len(string) - 1):
        if string[i] == "\\":
            if(string[i+1] == "t"):
                string = string[:i] + "       " + string[i+2:]
            elif(string[i+1] == "n"):
                string = string[:i] + "\x0A" + string[i+2:]
    print(string)

print(parse_horizontaltab_newline("viet\tna\nm"))


def count_len_to_delete(string, pos):
    """ $ printf "\123\b"
        $ printf "\x7A\b"
        eg: ord('a') -> 65: get ascii of param    """

    if string[pos - 4] == '\\':
        if string[pos - 3:pos].isdigit() and int(string[pos - 3:pos]) < 178:
            return 3
        elif string[pos - 3] == "x" and ord(string[pos - 2]) >=  48 and ord(string[pos - 2]) <= 55 and ((string[pos - 1]).isdigit() or (string[pos - 1]).isalpha()):
            return 3
        return 0
    elif string[pos - 3] == "\\":
        pass
        # cx control -x charactter
    elif string[pos - 2] == "\\":
        if string[pos - 1]  in ["a", "b", "e", "f", "n", "r", "t", "v", "\\", "\'"]:
            return 2
    return 0


def removeCharInString(string, start, len):
    return string[:start] + string[start + len:]


def read_env_var(string):
    """replace environ variables"""
    iter = 0
    while iter < len(string) - 1:
        if string[iter] == '$':
            temp = ''
            while iter < len(string) and string[iter] != ' ':
                temp += string[iter]
                iter += 1
            print("TEMP:", temp)
            replace = ""
            if temp[1:] in os.environ:
                replace = os.environ[temp[1:]]
            string = string.replace(temp, replace)
        iter += 1
    return string


def handle_backspace(string):
    for i in range(len(string) - 1):
        if string[i] == '\\' and string[i+1] == "b":
            lenCharDel = count_len_to_delete(string, i)
            removeCharInString(string, i - len, len)
    return string


def quoting(string):
    if string[0]== "'" and string[-1] == "''":
        string = single_quote(string)
        print("hi")
    elif string[0]== '"' and string[-1] == '"':
        string = double_quote(string)
    print(string)

if __name__ == "__main__":
    quoting('"viet nam"')
