folder_structure = {
    "root": {
        "Documents": {
            "school": {},
            "personal": {}
        },
        "Pictures": {
            "vacation": {},
            "family": {}
        },
        "Music": {}
    }
}

def print_folders_recursive(folder, indent=0):
    for name, sub in folder.items():
        print("  " * indent + f"- {name}")
        print_folders_recursive(sub, indent + 1)

def print_folders_loop(folder):
    stack = [("root", folder["root"], 0)]
    while stack:
        name, subfolder, indent = stack.pop()
        print("  " * indent + f"- {name}")
        for sub_name in reversed(subfolder):  # reversed for visual order
            stack.append((sub_name, subfolder[sub_name], indent + 1))

print("재귀 방식 출력:")
print_folders_recursive(folder_structure)

print("\n반복문 방식 출력:")
print_folders_loop(folder_structure)
