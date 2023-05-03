FILEPATH = "tasks.txt"

def get_todos(filepath_arg=FILEPATH):  # adding a default argument
    """
    Read a text file and return a list of todo items from the text file.
    default argument for filepath = "files/tasks.txt"
    """
    with open(filepath_arg, 'r') as taskfile_local:
        todos_local = taskfile_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath_arg=FILEPATH):  # put default parameters at the end
    """
    Writes a given todo list to a text file.
    default argument for filepath = "files/tasks.txt"
    """
    with open(filepath_arg, 'w') as taskfile_local:
        taskfile_local.writelines(todos_arg)


# this is run at the import functions command
if __name__ == "__main__":  # value of __name__ is __main__ only if run within
                            # functions.py. If run from command_line_interface_todo.py value is modules.functions
    print(get_todos("tasks.txt"))
