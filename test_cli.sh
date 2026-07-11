#!/bin/bash

echo "===== NO COMMAND ====="
python3 app.py

echo -e "\n===== ADD TESTS ====="
python3 app.py add
python3 app.py add ""
python3 app.py add "   "
python3 app.py add "Learn NumPy"

echo -e "\n===== UPDATE TESTS ====="
python3 app.py update
python3 app.py update abc "Learn Pandas"
python3 app.py update -1 "Learn Pandas"
python3 app.py update 1 ""
python3 app.py update 1 "Learn Pandas"

echo -e "\n===== DELETE TESTS ====="
python3 app.py delete
python3 app.py delete abc
python3 app.py delete 999

echo -e "\n===== STATUS TESTS ====="
python3 app.py mark-in-progress 1
python3 app.py mark-done 1

echo -e "\n===== LIST TESTS ====="
python3 app.py list
python3 app.py list todo
python3 app.py list in-progress
python3 app.py list done
python3 app.py list banana

echo -e "\n===== TESTS COMPLETED ====="