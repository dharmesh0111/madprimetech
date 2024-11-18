import os
import zipfile
from pathlib import Path
from PIL import Image

#Renaming All Files function
def renameFiles(folder):
    if not os.path.exists(folder):
        print("The folder '/path/to/folder' does not exist.")
        exit()

    if not os.path.isdir(folder):
        print("The given path is not a folder.")
        exit()

    files = os.listdir(folder)
    if len(files)<=1:
        print(f"The folder is empty. No files to rename.")
        exit() 
    files.sort()

    preview = input("Want to preview the file names??(yes/no)").strip().lower()
    if preview == 'yes':
        for file in files:
            print(file)
    
    reverse = input("Do you want to rename the files in reverse order? (yes/no): ").strip().lower()
    reverse = True if reverse == "yes" else False

    i = 1 if not reverse else len(files)

    for file in files:
        full_path = folder + "/" + file
        if not os.path.isfile(full_path) or file == "desktop.ini":
            continue

        name_parts = file.rsplit('.', 1)
        if len(name_parts) < 2:
            print(f"Skipping {file} (no extension)")
            continue

        if str(i)+'.'+name_parts[1] in files:
            print(f"{str(i)+'.'+name_parts[1]} rename already exites")
            continue

        new_name = folder + "/" + str(i) + "." + name_parts[1]
        try:
            os.rename(full_path, new_name)
            print(f"Files '{file}' renamed to '{str(i)}.{name_parts[1]}'")
        except PermissionError:
            print(f": Unable to rename file '{file}' due to permission issues.")
        except FileNotFoundError:
            print(f"Error: File not found: {file}.")
        except IsADirectoryError:
            print(f"Error: {file} is a directory, not a file.")
        except Exception as e:
            print(f"Unexpected error occurred while renaming {file}: {e}")

        i = i + 1 if not reverse else i - 1

    print("Renaming completed.")

#zip file function

def zipFolder(path):
    if not os.path.exists(path):
        print(f"Error: Folder '{path}' doesn't exist.")
        return

    if not os.path.isdir(path):
        print(f"Error: '{path}' is not a directory.")
        return

    zip_name = input("Enter the name for the output zip file (without extension): ").strip()
    if not zip_name:
        folder_name = os.path.basename(path)
        zip_name = f"{folder_name}.zip"

    if not zip_name.endswith('.zip'):
        zip_name += '.zip'

    desktop_path = str(Path.home() / "Desktop")
    zip_path = os.path.join(desktop_path, zip_name)

    print(f"Zipping folder: {path} to {zip_path}")

    try:
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for root, dirs, files in os.walk(path):
                for file in files:
                    file_path = os.path.join(root, file)
                    arc_name = os.path.relpath(file_path, path)
                    zip_file.write(file_path, arc_name)
            print(f"Folder '{os.path.basename(path)}' zipped successfully to {zip_path}")
    except PermissionError:
        print(f"Error: Permission issue with '{zip_path}'.")
    except FileNotFoundError as err:
        print(f"Error: File not found during zipping. {err}")
    except Exception as err:
        print(f"Unexpected error: {err}")

#collage function


def createCollage():
    image_paths = []
    for i in range(1, 5):
        path = input(f"Enter the path for Image {i}: ").strip()
        image_paths.append(path)

    output_format = input("Enter the output file format (jpg, png): ").strip().lower()

    if output_format not in ['jpg', 'jpeg', 'png', 'bmp']:
        print("Unsupported output format.")
        return

    images = []
    for path in image_paths:
        if not os.path.exists(path):
            print(f"Error: {path} doesn't exist.")
            return
        try:
            with Image.open(path) as img:
                img.verify()
            images.append(Image.open(path))
        except (IOError, SyntaxError):
            print(f"Error: {path} isn't a valid image.")
            return

    min_width = min(img.width for img in images)
    min_height = min(img.height for img in images)

    for i in range(4):
        images[i] = images[i].resize((min_width, min_height))

    collage_width = min_width * 2
    collage_height = min_height * 2
    collage = Image.new('RGB', (collage_width, collage_height))

    collage.paste(images[0], (0, 0))
    collage.paste(images[1], (min_width, 0))
    collage.paste(images[2], (0, min_height))
    collage.paste(images[3], (min_width, min_height))

    output_file = f"collage.{output_format}"
    collage.save(output_file)
    print(f"Collage saved as {output_file}")


print()
print("*********** MEDPRIME*******************")
print()
print('Renaming All Files in a Folder Sequentially - press 1 ')
print('Zipping a Folder - press 2 ')
print('Creating a Collage from 4 Images - press 3 ')
print()
usertask = input("Enter here:-")

if usertask == "1":
 #Renaming All Files in a Folder Sequentially
    folder = input("Please enter the path to the folder:  ").strip().replace('\\', '/')
    renameFiles(folder)

elif usertask == '2': 
    #Zipping a Folder
    if __name__ == "__main__":
        path = input("Enter folder path to zip: ").strip() 
    if not path:
        print("Error: No folder path entereded.")
    else:
        zipFolder(path)


elif usertask == '3':
    #Creating a Collage from 4 Images
    if __name__ == "__main__":
        createCollage()

else:
    print('NOt a valid input!!')






