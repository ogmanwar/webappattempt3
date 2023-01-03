def get_todos(filepath ='todos.txt'):
    """"Gets past todos from text
    and writes them as a to-do"""
    with open(filepath, 'r') as loc_file:
        todo_local = loc_file.readlines()
    return todo_local


def write_todos(loctodos,filepath ='todos.txt'):
    """"Writes the updated to-do list"""
    with open(filepath, 'w') as file:
        file.writelines(loctodos)


