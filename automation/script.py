# npm install rich
from rich.console import Console, Prompt, Table
import os
import shutil
import re

console = Console()

# instantiate the console object
def list_files(directory):  #display list all files in the directory
  files = os.listdir(directory)
  print(files)
  table = Table(title=f"Files in {directory}")
  table.add_column("File Name", style="dim")
  for file in files:
      table.add_row(file)
  console.print(table)

def move_file(current_directory, file, target_directory): #move given file to target directory
  source_path = os.path.join(current_directory, file)
  target_path = os.path.join(target_directory, file)
  shutil.move(source_path, target_path)
  console.print(f"{file} as been successfully moved to {target_directory}")

def search_files(directory, pattern):
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
    file_counts = {}
    for root, _ , files in os.walk(directory):
      for file in files:
        extension = os.path.splitext(file)[1].lower()
        if extension in target_extensions:
          file_counts[extension] = file_counts.get(extension, 0) + 1
          
          return file_counts

def print_file_counts(file_counts):
  print("File counts:")
  for extension, count in file_counts.items():
    print(f'{extension}: {count}')
  


def main():
    while True:
        console.print("\n1. [orange]List[/orange] files\n2. Move file\n3. Search files\n4. Exit")
        choice = Prompt.ask("Choose a task (Enter the number)", choices=['1,'' 2', '3', '4'], default='4')

        if choice == "1":
            directory = Prompt.ask("Enter the directory to list the files")
            list_files(directory)
        elif choice == "2":
            current_directory = Prompt.ask("Enter the {current_directory} of the file")
            file = Prompt.ask("Enter {file} to move")
            target_directory = Prompt.ask(
                "Enter the {target_directory} to move the file to"
            )
        elif choice == "3":
            directory = Prompt.ask("Enter directory to search files")
            pattern = Prompt.ask("Enter the regex pattern to search for")
            search_files(directory, pattern)
        elif choice == "4":
            directory = Prompt.ask("Enter the directory path for the files you'd like to count")
            target_extensions = ("Enter comma-separated file extensions to count (e.g., .txt,.pdf)")
            file_counts = count_files(directory, target_extensions.split(","))
            print_file_counts(file_counts)
        else:
            break

if __name__ == "__main":
  main()    
