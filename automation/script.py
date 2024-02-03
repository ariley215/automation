# npm install rich
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

import os
import shutil
import re

console = Console()

# instantiate the console object
def list_files(directory):
    """Lists all files in a given directory."""
    
    files = os.listdir(directory)
    print(files)
    table = Table(title=f"Files in {directory}")
    table.add_column("File Name", style="dim")
    for file in files:
        table.add_row(file)
    console.print(table)

def move_file(current_directory, file, target_directory):
    """Moves a file from a source to a target directory."""
   
    source_path = os.path.join(current_directory, file)
    target_path = os.path.join(target_directory, file)
    try:
      shutil.move(source_path, target_path)
      console.print(f"{file} as been successfully moved to {target_directory}")
    except OSError as e:
      console.print(f'Error moving {file}: {e}')

def search_files(directory, pattern):
  """Searches files in a directory based on a regular expression pattern."""

  try:
    files = os.listdir(directory)
    matches = [file for file in files if re.search(pattern, files)]
    table = Table(title=f"Files matching {directory} matching {pattern}")
    table.add_column("Matching file name")
    for match in matches:
      table.add_row(match)
    console.print(table)
  except:
    FileNotFoundError
    console.print("[bold red]Directory not found[/bold red]")

def count_files(directory, target_extensions):
  """Counts files of specific extensions within a directory."""
  
  file_counts = {}
  for root, _ , files in os.walk(directory):
      for file in files:
        full_path = os.path.join(root, file)
        extension = os.path.splitext(full_path)[1].lower()
        if extension in target_extensions:
          file_counts[extension] = file_counts.get(extension, 0) + 1
  return file_counts

def print_file_counts(file_counts):
  """Prints a table of file counts by extension."""
  
  print("File counts:")
  for extension, count in file_counts.items():
      print(f'{extension}: {count}')

def create_folder(folder_name):
    """Creates a new folder."""
    
    try:
      os.makedirs(folder_name)
      print(f'Folder {folder_name} sucessfully created!')
    except OSError as e:
      print(f'Error creating folder {e}')

def handle_deleted_user(user_folder):
    """Moves a deleted user's documents to a temporary folder."""
    
    temp_folder = "deleted_user_docs"
    os.makedirs(temp_folder, exist_ok=True)
    for filename in os.listdir(user_folder):
        shutil.move(os.path.join(user_folder, filename),temp_folder)
    console.print(f'User documents moved to {temp_folder}')    

def sort_documents(directory):
    """Sorts documents into folders based on their extension."""
    for root, _ , files in os.walk(directory):
        for file in files:
            extension = os.path.splitext(file)[1].lower()
            target_folder = os.path.join(root, extension.replace(".", ""))
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(os.path.join(root, file), os.path.join(target_folder, file))

def parse_log_file(log_file, target_directory):
    """Parses a log file for errors and warnings, creating separate files."""

    errors = []
    warnings = []
    with open(log_file, "r") as file:
        for line in file:
            if "ERROR" in line:
                errors.append(line)
            elif "WARNING" in line:
                warnings.append(line) 
    with open(os.path.join(target_directory, "errors.log"), "w") as error_file:
        error_file.writelines(errors)
    with open(os.path.join(target_directory, "warnings.log"), "w") as warning_file:
        warning_file.writelines(warnings)

def move_specific_files(file_type, directory, target_folder):
    for root, _, files in os.walk(directory):
      for file in files:
        extension = os.path.splitext(file)[1].lower()
        if extension == file_type:
          source_path = os.path.join(root, file)
          target_path = os.path.join(target_folder, file)
          try:
              os.makedirs(target_folder, exist_ok=True)
              shutil.move(source_path, target_path)
          except Exception as e:
            console.print(f'Error moving {file}: {e}')

def main():
    print("Inside main() function")
    while True:
        console.print("\n1. [orange]List[/orange] files\n2. Move file\n3. Search files\n4. Exit")
        choice = Prompt.ask("Choose a task (Enter the number)", choices=['1', '2', '3', '4'], default='4')

        if choice == "1":
            directory = Prompt.ask("Enter the directory to list the files")
            list_files(directory)
        elif choice == "2":
            current_directory = Prompt.ask("Enter the {current_directory} of the file")
            file = Prompt.ask("Enter {file} to move")
            target_directory = Prompt.ask("Enter the {target_directory} to move the file to")
            move_file(current_directory, file, target_directory)
        elif choice == "3":
            directory = Prompt.ask("Enter directory to search files")
            pattern = Prompt.ask("Enter the regex pattern to search for")
            search_files(directory, pattern)
        elif choice == "4":
            directory = Prompt.ask("Enter the directory path for the files you'd like to count")
            target_extensions = Prompt.ask("Enter comma-separated file extensions to count (e.g., .txt,.pdf)")
            file_counts = count_files(directory, target_extensions.split(","))
            print_file_counts(file_counts)
        else:
            break

def management_menu():
    print("Inside management_menu() function")
    while True:
        console.print('\n**Management Menu**')
        console.print('1. Create Folder')
        console.print('2. Manage user documents')
        console.print('3. Move specific file types')
        console.print('4. Parse log file for errors and warnings')      
        console.print('5. Exit')
        choice = Prompt.ask("Choose a task (Enter the number)", choices = ['1', '2', '3', '4', '5'], default='5')
        
        if choice == '1':
          folder_name = Prompt.ask('Enter the name of the new folder:')
          create_folder(folder_name)
        elif choice == '2':
          action = Prompt.ask('Choose and action', choices=['Sort documents', 'Move deleted user'])
          if action == 'Sort documents':
              directory = Prompt.ask('Enter directory to sort documents')
              sort_documents(directory)
          elif action == 'Move deleted user documents':
              user_folder = Prompt.ask('Enter the path to the deleted user"s folder:')
              handle_deleted_user(user_folder)
        elif choice == '3':
            file_type = Prompt.ask('Enter the file type (e.g., .log, .txt)')
            target_folder = Prompt.ask('Enter the target folder to move files to')
            directory = Prompt.ask('Enter the directory to search the files')
            move_specific_files(file_type, directory, target_folder)
        elif choice == '4':
            log_file = Prompt.ask('Enter the path to the log pile to parse') 
            target_directory = Prompt.ask('Enter the target directory for the parsed logs:')
            parse_log_file(log_file, target_directory)
        elif choice == '5':
            break                 


if __name__ == "__main":
  
  main()  
  management_menu()  
