#!/usr/bin/env python3
import os, subprocess
from builtin import handle_cd, handle_export, handle_unset, handle_exit
from history import handle_history, handle_exclamation_mark_history
from path_expansion import handle_tidle, handle_parameter, get_variable



def handle_rough_command(rough_commands):
    """
    1. plit program-name and argument by " " in command
    """
    command = rough_commands.split() # 2
    return command



def identify_command(command, dict_history, dic_var):
    # type_character = {''}

    # show history
    if command[0] == 'history':
        return handle_history(command, dict_history)
]    # execute history with !
    elif command[0].startswith("!"):
        return handle_exclamation_mark_history(command, dict_history)

    # work with tidle expansion
    elif command[0].startswith("~"):
        return handle_tidle(command)

    # save variable and ready to cal
    elif "=" in command[0]:
        return get_variable(command, dic_var)
    # work with paramater expansion
    elif "${" in ' '.join(command) or "$" in ' '.join(command):
        print(' '.join(command), type(' '.join(command)), command)
        return handle_parameter(command, dic_var)
        """
        many thing to handle be here and we can change the order later
        globbing
        handle_exit_status
        subshell with ()
        pipe and redirection >> << > <
        logical operators && and || ★
        quoting
        command substitution with the backquotes - ` `
        """
    else:
        return command


def handle_execute_command(command):
    # global dic_var

    # only dot "."
    if len(command) == 1 and command[0] == ".":
        print("bash: .: filename argument required\n.: usage: . filename [arguments]")

    # 2 PATH
    elif "/" in command[0] or command[0].startswith("."):
        path = handle_path(command)
        check_path(path, command)
    # 3 bultin-name or external-file or script
    else:
        if check_exists_command(command[0]) == "non_PATH":
            print("intek-sh: " + command[0] + ": No such file or directory")
        elif check_exists_command(command[0]) == "notfound":
            if command[0] != ['history'] and command != [' ']:
                print("%s: command not found" % command[0])
        elif check_exists_command(command[0]) == "buildin":
            process_commands(command)
        else:
            if(len(command) == 1):
                subprocess.run(command[0])
            else:
                for arg in command[1:]:
                    subprocess.run([command[0], arg])



def handle_path(command):
    if command[0] == ".":
        if not command[1].startswith("/") or not command[1].startswith("./"):
            path = os.getcwd() + "/" + command[1]
    else:
        path = command[0]
    return path


def check_path(path, command):
    name = command[0]
    print(name, type(name), command, type(command))
    if command[0] == ".":
        if len(command) > 1:
            name = command[1]
    if os.path.exists(path) is False:
        print("bash: " + name + ": No such file or directory")
    elif os.path.isdir(path) is True:
        print("bash: " + name + ": Is a directory")
    elif os.path.isfile(path) is True:
        if os.access(path, os.X_OK) is False:
            if command[0] == ".":
                os.chmod(path, 0o755)
                subprocess.run(path)
            else:
                print("bash: " + name + ": Permission denied")
        else:
            subprocess.run(path)
    else:
        print("bash: %s: command not found" % name)


def check_exists_command(command):
    """
    if non-exists PATH -> False
    if non-exists command -> True
    exists command -> return where command
    """
    if command in ["cd", "unset", "export", "exit"]:
        return "buildin"
    if 'PATH' not in os.environ:
        return "non_PATH"
    PATH = os.environ['PATH'].split(':')
    for path in PATH:
        if(os.path.exists(path)):
            if command in os.listdir(path):
                return path
    return "notfound"


def process_commands(command):
    processing = {'cd': handle_cd,
                  'unset': handle_unset,
                  'export': handle_export,
                  'exit': handle_exit }
    return processing[command[0]](command)
