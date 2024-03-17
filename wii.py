import os

def remove_comments(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    new_lines = []
    in_comment = False

    for line in lines:
        start_comment = line.find("/*")
        end_comment = line.find("*/")
        
        if start_comment != -1:
            in_comment = True
            if end_comment != -1:
                line = line[:start_comment] + line[end_comment+2:]
            else:
                line = line[:start_comment]
        elif end_comment != -1:
            in_comment = False
            line = line[end_comment+2:]
        elif in_comment:
            continue

        new_lines.append(line)

    with open(file_path, 'w') as file:
        file.writelines(new_lines)

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".css"):  # CSS files
                file_path = os.path.join(root, file)
                remove_comments(file_path)

if __name__ == "__main__":
    directory_path = input("Enter the path to the directory: ")
    process_directory(directory_path)
    print("Comments removed successfully.")
