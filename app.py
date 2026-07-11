import json
import datetime
import sys

def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)

        if not isinstance(tasks, list):
            print("Error: tasks.json has an invalid structure.")
            sys.exit(1)

        return tasks

    except FileNotFoundError:
        initial_data = []

        with open("tasks.json", "w") as f:
            json.dump(initial_data, f, indent=2)

        print("Empty task database created.")
        return initial_data

    except json.JSONDecodeError:
        print("Error: tasks.json contains invalid JSON.")
        sys.exit(1)
def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks,f,indent = 2)

def parse_task_id(task_id):
    try:
        parsed_id = int(task_id)
        if parsed_id <= 0:
            print("Task ID must be a positive integer.")
            return None
        return parsed_id
    except ValueError:
        print("Task ID must be a positive integer.")
        return None
    
def parse_description(description):
    description = description.strip()

    if not description:
        print("Enter a valid description.")
        return None

    return description

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
        if len(sys.argv) < 3:
            print('Usage: python app.py add "description"')
            return

        description = parse_description(sys.argv[2])
        if description is None:
            return
        add_task(description)

    elif command == "update":
        if len(sys.argv) < 4:
            print('Usage: python app.py update <id> "description"')
            return
        task_id = parse_task_id(sys.argv[2])
        if task_id is None:
            return
        description = parse_description(sys.argv[3])
        if description is None:
            return
        update_task(task_id, description)

    elif command == "delete":
        if len(sys.argv) < 3:
            print('Usage: python app.py delete <id>')
            return
        task_id = parse_task_id(sys.argv[2])
        if task_id is None:
            return
        delete_task(task_id)

    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print('Usage: python app.py mark-in-progress <id>')
            return
        task_id = parse_task_id(sys.argv[2])
        if task_id is None:
            return
        update_status(task_id, "in-progress")

    elif command == "mark-done":
        if len(sys.argv) < 3:
            print('Usage: python app.py mark-done <id>')
            return
        task_id = parse_task_id(sys.argv[2])
        if task_id is None:
            return
        update_status(task_id, "done")

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