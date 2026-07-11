## Project URL

https://roadmap.sh/projects/task-tracker


# Task Tracker CLI

A simple command-line task management application built with Python. Tasks are stored locally in a JSON file and can be created, updated, deleted, filtered, and marked by status.

The project uses only Python's standard library and requires no external dependencies.

## Features

* Add new tasks
* Update task descriptions
* Delete tasks
* Mark tasks as `in-progress`
* Mark tasks as `done`
* List all tasks
* Filter tasks by status
* Automatic JSON storage creation
* CLI input validation
* Invalid and corrupted JSON detection

## Requirements

* Python 3

## Installation

Clone the repository:

```bash
git clone git@github.com:ZiyaisCoding/Task_Tracker.git
```

Move into the project directory:

```bash
cd Task_Tracker
```

No external dependencies need to be installed.

## Usage

Run the application using:

```bash
python3 app.py <command> [arguments]
```

### Add a Task

```bash
python3 app.py add "Learn NumPy"
```

Output:

```text
Task added successfully (ID: 1).
```

### Update a Task

```bash
python3 app.py update 1 "Learn Pandas"
```

### Delete a Task

```bash
python3 app.py delete 1
```

### Mark a Task as In Progress

```bash
python3 app.py mark-in-progress 1
```

### Mark a Task as Done

```bash
python3 app.py mark-done 1
```

### List All Tasks

```bash
python3 app.py list
```

### Filter Tasks by Status

```bash
python3 app.py list todo
python3 app.py list in-progress
python3 app.py list done
```

## Task Data Structure

Tasks are stored in `tasks.json` using the following structure:

```json
[
  {
    "id": 1,
    "description": "Learn NumPy",
    "status": "todo",
    "createdAt": "2026-07-11T18:30:00",
    "updatedAt": "2026-07-11T18:30:00"
  }
]
```

Supported task statuses are:

* `todo`
* `in-progress`
* `done`

The `tasks.json` file is automatically created when the application runs if it does not already exist.

## Testing

The project includes a shell-based CLI integration test script.

Run:

```bash
chmod +x test_cli.sh
./test_cli.sh
```

The test script checks:

* Command validation
* Task creation
* Task updates
* Task deletion
* Status updates
* Status filtering
* ID generation
* Empty JSON files
* Malformed JSON
* Invalid JSON structures
* Automatic task database restoration

## Built With

* Python
* JSON
* Bash
* Git

## Project Goal

This project was built to practice command-line application development, JSON persistence, filesystem operations, input validation, error handling, and integration testing using Python's standard library.
