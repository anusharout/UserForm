import os

# Specify the path to the folder where you want to create the directory
folder_path = r"C:\Users\anurout\PycharmProjects\errorDataTemplate"

# Check if the folder exists, and if not, create it
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Specify the name of the directory to be created
directory_name = "finalReport"

# Construct the full path to the new directory
new_directory_path = os.path.join(folder_path, directory_name)

# Check if the directory already exists
if os.path.exists(new_directory_path):
    print(f"The directory '{directory_name}' already exists.")
else:
    # Create the directory
    os.mkdir(new_directory_path)
    print(f"Directory '{directory_name}' created successfully in '{folder_path}'.")
