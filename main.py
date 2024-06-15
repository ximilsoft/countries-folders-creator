import json
import os

def create_folder(folder_name):
    """
    Creates a folder inside 'all' if it does not already exist.

    Parameters:
    folder_name (str): The name of the folder to create inside 'all'.
    """
    full_path = os.path.join("all", folder_name)
    
    try:
        if not os.path.exists(full_path):
            os.makedirs(full_path)
        else:
            print(f"Folder already exists: {full_path}")
    except OSError as e:
        print(f"Error creating directory {full_path}: {e}")

def create_text(folder_name, file_name):
    """
    Creates an empty text file with the same name as the folder inside the folder.

    Parameters:
    folder_name (str): The name of the folder where the text file will be created.
    file_name (str): The name of the text file to create (without extension).
    """
    file_path = os.path.join("all", folder_name, f"{file_name}.txt")
    try:
        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                pass
        else:
            print(f"File already exists: {file_path}")
    except OSError as e:
        print(f"Error creating file {file_path}: {e}")

def create(folder_name, file_name):
    """
    Creates a folder and an associated text file inside 'all' if they do not already exist.

    Parameters:
    folder_name (str): The name of the folder to create inside 'all'.
    file_name (str): The name of the text file to create (without extension).
    """
    try:
        create_folder(folder_name)
        create_text(folder_name, file_name)
    except Exception as e:
        print(f"Error creating {folder_name}/{file_name}: {e}")

def get_data_from_json(file_path):
    """
    Reads a JSON file and returns its content.

    Parameters:
    file_path (str): The path to the JSON file.

    Returns:
    dict: The data from the JSON file.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError as e:
        print(f"Error: The file {file_path} does not exist.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON file {file_path}: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error reading {file_path}: {e}")

# Run the script to create folders and corresponding text files based on data from 'countries.json'.
data = get_data_from_json('countries.json')
if data:
    for key, value in data.items():
        key = key.lower()
        create(key, value)