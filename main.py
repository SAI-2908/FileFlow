import os
import shutil

FOLDER_PATH = input("Enter the folder path you want to organize: ").strip()

if not os.path.isdir(FOLDER_PATH):
    print("Error: The folder does not exist.")
    exit()

#file type mapping
FILE_TYPES ={
    'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],   
    'Audio': ['.mp3', '.wav', '.aac', '.flac'],
    'Videos': ['.mp4', '.avi', '.mov', '.mkv'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Scripts': [ '.py', '.js', '.html', '.css', '.java'],
    'Others': []
    
}
def get_category(file_extension):
    for folder, extensions in FILE_TYPES.items():
        if file_extension in extensions:
            return folder

    return 'Others'

#create folders if they don't exist
for folder in FILE_TYPES.keys():
    folder_path = os.path.join(FOLDER_PATH, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

#organise files

# Organise files

for file in os.listdir(FOLDER_PATH):

    file_path = os.path.join(FOLDER_PATH, file)

    # Skip folders
    if os.path.isdir(file_path):
        continue

    # Get file extension
    file_ext = os.path.splitext(file)[1].lower()

    # Find the correct category
    category = get_category(file_ext)

    # Create destination folder
    destination_folder = os.path.join(FOLDER_PATH, category)

    # Move the file
    destination_path = os.path.join(destination_folder, file)

    shutil.move(file_path, destination_path)

    print(f"Moved: {file} -> {category}")

print("\nFiles have been organized successfully.") 