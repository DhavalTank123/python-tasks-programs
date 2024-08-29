import os
import json

def check_files_in_folders(json_file_path, base_directory):
    """
    Check if folders and files listed in the JSON file are present in the base directory.
    
    :param json_file_path: Path to the JSON file.
    :param base_directory: Base directory to check for folders and files.
    """
    try:
       
        with open(json_file_path, 'r') as file:
            folders_files = json.load(file)
        
    
        for folder_name, files in folders_files.items():
            folder_path = os.path.join(base_directory, folder_name)
            
            if os.path.isdir(folder_path):
                print(f"Checking folder: {folder_name}")
                
             
                for file_name in files:
                    file_path = os.path.join(folder_path, file_name)
                    
                  
                    if not os.path.isfile(file_path):
                        print(f"Missing file: {file_name} in folder: {folder_name}")
            else:
                print(f"Folder not found: {folder_name}")
               
                for file_name in files:
                    print(f"Missing file: {file_name} in folder: {folder_name}")

    except FileNotFoundError:
        print(f"JSON file not found: {json_file_path}")
    except json.JSONDecodeError:
        print("Error decoding JSON file")
    except Exception as e:
        print(f"An error occurred: {e}")

# 
json_file_path = 'folders_files.json'  
base_directory = r"/home/nikhil/Documents/All python program"  


check_files_in_folders(json_file_path, base_directory)
