#!/bin/bash

TASK_FILE="tasks.json"
BACKUP_FILE="tasks.json.backup"

echo "===== TASK TRACKER CLI TESTS ====="

# Backup existing task database
if [ -f "$TASK_FILE" ]; then
    cp "$TASK_FILE" "$BACKUP_FILE"
    echo "Existing tasks.json backed up."
fi

# Start with a clean database
rm -f "$TASK_FILE"

echo -e "\n===== FILE CREATION TEST ====="
python3 app.py list

echo -e "\n===== NO COMMAND ====="
python3 app.py

echo -e "\n===== UNKNOWN COMMAND ====="
python3 app.py banana

echo -e "\n===== ADD TESTS ====="
python3 app.py add
python3 app.py add ""
python3 app.py add "   "
python3 app.py add "Learn NumPy"
python3 app.py add "Build ML project"
python3 app.py add "Learn SQL"

echo -e "\n===== ADD WHITESPACE TEST ====="
python3 app.py add "   Learn Python   "

echo -e "\n===== LIST AFTER ADD ====="
python3 app.py list

echo -e "\n===== UPDATE TESTS ====="
python3 app.py update
python3 app.py update abc "Learn Pandas"
python3 app.py update 1.5 "Learn Pandas"
python3 app.py update -1 "Learn Pandas"
python3 app.py update 0 "Learn Pandas"
python3 app.py update 1 ""
python3 app.py update 1 "   "
python3 app.py update 1 "Learn Pandas"
python3 app.py update 999 "Ghost task"

echo -e "\n===== DELETE TESTS ====="
python3 app.py delete
python3 app.py delete abc
python3 app.py delete 1.5
python3 app.py delete -1
python3 app.py delete 0
python3 app.py delete 999

echo -e "\n===== STATUS TESTS ====="
python3 app.py mark-in-progress
python3 app.py mark-in-progress abc
python3 app.py mark-in-progress -1
python3 app.py mark-in-progress 999
python3 app.py mark-in-progress 1

python3 app.py mark-done
python3 app.py mark-done abc
python3 app.py mark-done -1
python3 app.py mark-done 999
python3 app.py mark-done 1

echo -e "\n===== LIST TESTS ====="
python3 app.py list
python3 app.py list todo
python3 app.py list in-progress
python3 app.py list done
python3 app.py list banana

echo -e "\n===== ID GENERATION TEST ====="
python3 app.py delete 2
python3 app.py add "Test ID generation"
python3 app.py list

echo -e "\n===== EMPTY JSON FILE TEST ====="
> "$TASK_FILE"
python3 app.py list

echo -e "\n===== MALFORMED JSON TEST ====="
echo '{"id": 1,' > "$TASK_FILE"
python3 app.py list

echo -e "\n===== INVALID JSON STRUCTURE: OBJECT ====="
echo '{"id": 1}' > "$TASK_FILE"
python3 app.py list

echo -e "\n===== INVALID JSON STRUCTURE: STRING ====="
echo '"hello"' > "$TASK_FILE"
python3 app.py list

echo -e "\n===== INVALID JSON STRUCTURE: NUMBER ====="
echo '42' > "$TASK_FILE"
python3 app.py list

echo -e "\n===== INVALID JSON STRUCTURE: NULL ====="
echo 'null' > "$TASK_FILE"
python3 app.py list

echo -e "\n===== RESTORING DATABASE ====="

if [ -f "$BACKUP_FILE" ]; then
    mv "$BACKUP_FILE" "$TASK_FILE"
    echo "Original tasks.json restored."
else
    rm -f "$TASK_FILE"
    echo "Test tasks.json removed."
fi

echo -e "\n===== TESTS COMPLETED ====="