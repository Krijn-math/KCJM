import os
import json

base = "."  # directory where folder_1 … folder_9 live

for i in range(1, 10):
    folder = f"folder_{i}"
    path = os.path.join(base, folder)

    if not os.path.isdir(path):
        continue

    files = [
        f for f in os.listdir(path)
        if os.path.isfile(os.path.join(path, f))
           and not f.endswith(".json")
           and not f.startswith(".")
    ]

    index_path = os.path.join(path, "index.json")
    with open(index_path, "w") as f:
        json.dump(files, f, indent=2)

    print(f"Created {index_path} with {len(files)} entries.")
