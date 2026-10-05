# File Organizer

A simple Python utility that automatically organizes files into folders based on their file extensions.

## Features

- Allows the user to choose the folder to organize
- Automatically creates category folders
- Organizes files based on their extensions
- Supports images, documents, audio, videos, archives and scripts
- Places unrecognized file types into an 'Others' folder
- Displays the files being moved in the terminal

## Tech Stack

- Python
- OS module
- Shutil module

## How It Works

The program first asks the user for the path of the folder they want to organize.

It then checks each file's extension and matches it with a predefined category.

For example:

- `.jpg` → Images
- `.pdf` → Documents
- `.mp3` → Audio
- `.mp4` → Videos
- `.zip` → Archives
- `.py` → Scripts
- Unknown extensions → Others

The required folders are created automatically if they don't already exist.

## How to Run

Make sure Python is installed.

Run the following command in the terminal:

    python main.py

The program will ask you to enter the path of the folder you want to organize.

## What I Learned

- Working with files and directories in Python
- Using dictionaries and lists to categorize data
- Writing reusable functions
- Using `os` for filesystem operations
- Using `shutil` to move files
- Handling file extensions
- Basic error handling and user input

## Future Improvements

- Add a graphical user interface
- Add more file categories
- Add duplicate-file handling
- Add a preview mode before moving files