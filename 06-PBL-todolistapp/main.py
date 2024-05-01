import json


def add_new_todo():
    output = input("Silahkan masukan todo anda hari ini : ")
    return output


def save_todo(json_: dict, filename="todo.json"):
    with open(filename, "w") as file:
        json.dump(json_, file)


def load_todo(filename="todo.json"):
    pass


if __name__ == "__main__":
    print("Ini adalah aplikasi todo list app")
    todos = []
    while True:
        todo = add_new_todo()
        if todo == "0":
            break
        todos.append(todo)

    save_todo(json_={"todos": todos})
