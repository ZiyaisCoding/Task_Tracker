import json
import datetime
import sys

def load_tasks():
    try:
        with open("tasks.json","r") as f:
            return json.load(f)
    except FileNotFoundError:
        initial_data = []
        with open("tasks.json", "w") as f:
            json.dump(initial_data, f, indent=2)
        print("Empty task database created.")
        return initial_data
    

def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks,f,indent = 2)

def add_task(description):
    tasks = load_tasks()
    if not tasks:
        new_id = 1
    else:
        new_id = max(task["id"] for task in tasks) + 1
    now = datetime.datetime.now().replace(microsecond=0).isoformat()
    task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_id}).")

def update_task(task_id,description):
    tasks = load_tasks()
    if not tasks:
        print("There is no task.")
        return

    for task in tasks:
        if task["id"] == task_id:
            task["description"] = description
            task["updatedAt"] = datetime.datetime.now().replace(microsecond=0).isoformat()
            save_tasks(tasks)
            print("Task updated successfully.")
            break
    else:
        print("Task not found.")

def delete_task(task_id):
    tasks = load_tasks()

    if not tasks:
        print("There is no task.")
        return

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print("Task deleted successfully.")
            break
    else:
        print("Task not found.")


def show(status="all"):
    tasks = load_tasks()
    found = False
    if not tasks:
        print("There is no task.")
        return
    for task in tasks:
        if status == "all" or task["status"] == status:
            print(
                f"Task ID: {task['id']}, "
                f"Task: {task['description']}, "
                f"Status: {task['status']}"
            )
            found = True
    if not found:
        print(f"No {status} tasks found.")

def update_status(task_id,status):
    tasks = load_tasks()
    if not tasks:
        print("There is no task.")
        return

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = datetime.datetime.now().replace(microsecond=0).isoformat()
            save_tasks(tasks)
            print("Task status updated successfully.")
            break
    else:
        print("Task not found.")

def main():
    if len(sys.argv)<2:
        print('No command provided')
        return
    
    command = sys.argv[1]

    if command == "add":
        description = sys.argv[2]
        add_task(description)

    elif command == "update":
        task_id = int(sys.argv[2])
        description = sys.argv[3]
        update_task(task_id, description)

    elif command == "delete":
        task_id = int(sys.argv[2])
        delete_task(task_id)

    elif command == "mark-in-progress":
        task_id = int(sys.argv[2])
        update_status(task_id,"in-progress")

    elif command == "mark-done":
        task_id = int(sys.argv[2])
        update_status(task_id,"done")

    elif command == "list":
        if len(sys.argv) == 2:
            show()
        else:
            task = sys.argv[2]

            if task == "done":
                show("done")
            elif task == "todo":
                show("todo")
            elif task == "in-progress":
                show("in-progress")
            else:
                print(f"Unknown status: {task}")

    else:
        print(f"Unknown command: {command}")







if __name__ == "__main__":
    main()