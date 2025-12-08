import os

# folders to scan (adjust if needed)
# Folders:
folders = [
    "AD",
    "INDIA",
    "NIMMA",
    "ART",
    "BIRDS",
    "COLOMBIA",
    "LANDSCAPE",
    "AMAZON",
    "CATS",
    "GALAPAGOS"
]

TODO_FILE = "todo-write.txt"

todos = []

for folder in folders:
    if not os.path.isdir(folder):
        continue

    # get all JPG files
    jpgs = [f for f in os.listdir(folder) if f.lower().endswith(".jpeg")]

    for jpg in jpgs:
        base = os.path.splitext(jpg)[0]
        txt_path = os.path.join(folder, base + ".txt")

        # If TXT does not exist → create empty and add todo
        if not os.path.exists(txt_path):
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write("")  # create empty file

            todos.append(f"{folder}/{base}.txt  (missing → created)")
            continue

        # If TXT exists but is empty → add todo
        if os.path.getsize(txt_path) == 0:
            todos.append(f"{folder}/{base}.txt  (empty)")

# write todos to the main todo file
if todos:
    with open(TODO_FILE, "w", encoding="utf-8") as f:
        for item in todos:
            f.write(item + "\n")
    print(f"Written {len(todos)} todos to {TODO_FILE}")
else:
    print("All .txt files are present and non-empty. No todo file created.")
