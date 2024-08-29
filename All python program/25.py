import os

def list_files_and_directories(directory):
    """
    List all files and directories in the specified directory.
    
    :param directory: The path to the directory to search.
    :return: Two lists: one for files and one for directories.
    """
    files = []
    directories = []

    if not os.path.isdir(directory):
        print(f"The path '{directory}' is not a valid directory.")
        return files, directories

 
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            files.append(item)
        elif os.path.isdir(item_path):
            directories.append(item)

    return files, directories

directory_to_search = r"/home/nikhil/Documents/All python program" 


files, directories = list_files_and_directories(directory_to_search)

print("Files:")
for file in files:
    print(f" - {file}")

print("\nDirectories:")
for directory in directories:
    print(f" - {directory}")
