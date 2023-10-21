import os

def generate_file_tree(startpath):
    tree = ['.']
    prefix = {startpath: ''}

    for root, dirs, files in os.walk(startpath):
        # Ignore .git directory
        if '.git' in dirs:
            dirs.remove('.git')

        level = root.replace(startpath, '').count(os.sep)
        indent_subdir = '│   ' * (level - 1) + '├── '
        indent_file = '│   ' * level + '├── '

        if level == 0:  # Base repository
            for i, f in enumerate(sorted(files)):
                tree.append(indent_file + f)
            for d in sorted(dirs):
                tree.append(indent_subdir + d)

        elif level == 1:  # Immediate subfolders
            last_subdir = list(prefix.keys())[-1]
            tree.append(prefix[last_subdir] + os.path.basename(root))
            prefix[root] = prefix[last_subdir] + '│   '
            for d in sorted(dirs):
                tree.append(prefix[root] + '├── ' + d)

        # Since we're only interested in the base, immediate subfolders, and one more level, we can break out early.
        if level >= 2:
            break

    return '\n'.join(tree)

def update_readme_with_tree(tree):
    with open("README.md", "r") as file:
        content = file.readlines()

    begin_marker = "<!-- BEGIN FILE TREE -->\n"
    end_marker = "<!-- END FILE TREE -->\n"
    begin_index = content.index(begin_marker) + 1
    end_index = content.index(end_marker)

    # Remove old tree
    del content[begin_index:end_index]

    # Insert new tree
    content.insert(begin_index, "```text\n" + tree + "\n```\n")

    with open("README.md", "w") as file:
        file.writelines(content)

if __name__ == "__main__":
    tree = generate_file_tree('.')
    update_readme_with_tree(tree)
    print("Updated README.md with the file tree.")

