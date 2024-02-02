# LAB - Class 19

Project: Automation

Author: Andrea Riley(Thiel)

1. Automate the creation of a folder.

- Write a Python script to create a new folder with a specified name.

2. Handle a deleted user.

- user2 is a deleted user and need to move their documents from their user folder to a temporary folder. Your script will create the temporary folder. This will effectively delete the user from the system while still maintaining a record of their documents.

3. Sort documents into appropriate folders.

- Go through a given folder and sort the documents into additional folders based on their file type.
  - Move log files into a logs folder. If a logs folder doesn’t exist, your script should create one.
  - Move email files into a mail folder. If a mail folder doesn’t exist, your script should create one.

4. Parse a log file for errors and warnings.

- From the previous task, you’ve moved a log file into the logs folder. Now, parse the log file for errors and warnings and create two separate log files in a target directory:
  - errors.log: Contains all error messages.
  - warnings.log: Contains all warning messages.

5. Create a menu-driven application.

- Give the user a list of automation tasks (1-4) and let them choose one to execute. Customize your application by incorporating an additional automation task, choose one:
  - Counting the number of specific file types in a directory. *completed 02-01-2024 11:25PM EST*
  - Renaming files based on a specific pattern.
  - Automatically backing up specific folders.

## Links and Resources

back-end server url (when applicable)
front-end application (when applicable)
Setup
.env requirements (where applicable)
i.e.

PORT - Port Number
DATABASE_URL - URL to the running Postgres instance/db

How to initialize/run your application (where applicable)
e.g. python main.py
How to use your library (where applicable)

## Tests

How do you run tests?
Any tests of note?
Describe any tests that you did not complete, skipped, etc

