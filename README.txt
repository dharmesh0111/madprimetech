*assigment 1 :Programming Assignment: Renaming All Files in a Folder Sequentially*
.The program use os module to work with file system, like checking paths, list files in folder and rename files.
.A function renameFiles(folder) is made to rename all files in the folder given by user and also ask for revers order or not.
.User need to enter folder path using input(). The input is cleaned with .strip() to remove space and .replace('\\', '/') to change backslashes to slashes for better working.
.It checks if the folder exist with os.path.exists(folder). If it not exist, it prints error message and exit.
.It also checks if the path is a folder or not using os.path.isdir(folder). If not folder, it shows message and stop.
.All files in folder are listed using os.listdir(folder). If folder empty or has only one file, it stops and print message.
.The files are sorted alphabetically using files.sort() to make renaming easier and in order.
.Non-file items like folders or system files (like desktop.ini) are skipped using os.path.isfile().
.File names are split into name and extension using rsplit('.', 1). Files without extension are ignored and a message is printed.
.Before renaming, it checks if new name like 1.txt already exist. If it exist, it skips renaming and print a message.
.Files are renamed to 1.extension, 2.extension, etc., using os.rename(). A counter is used to keep track of numbers for next file name.
.Errors during renaming are handled with try-except block:
.Prints message if permission not allowed.
.Handle file not found error if file is missing.
.Ignore folders by catching directory error.
.Print any other error if unexpected.
.During renaming, it print what is happening like file renamed, skipped, or error.
.At end, it prints "Renaming completed." after all files are done.
.The user can now choose whether to rename files in reverse order. If reverse=True, files will be renamed starting from the highest number. The user can select this option through an input prompt.
.ask user for want to preveiws folder file name using for loop


*assigment 2 :Zipping a Folder*
.This program uses os and zipfile to zip a folder and save it as a .zip file on the desktop.
.The function zipFolder(path) is made to zip the folder.
.First, it checks if the folder exists using os.path.exists(). If the folder does not exist, it prints an error and stops.
.Then, it checks if the path is a folder using os.path.isdir(). If it's not a folder, it shows an error and stops.
.The program takes the folder name from path using os.path.basename(path) and adds .zip at the end to make the zip file name.
.The zip file is saved on the desktop using Path.home() and os.path.join().
.The program prints a message to show that it's zipping the folder to the desktop.
.A try-except block is used to handle errors:
.If there is a permission issue while zipping, it shows an error.
.If a file is missing, it shows an error with the file details.
.If any other error happens, it shows that error.
.The program uses os.walk() to go through all the files and subfolders in the folder.
.Each file is added to the zip file using zipfile.ZipFile.write().
.The program includes a section that prompts the user to enter the folder path using input(). If no path is entered or the path is incorrect, an error is shown. If the path is correct, the zipFolder(path) function is called to zip the folder.
.After adding all files to the zip, it shows a message saying the folder was zipped successfully.
.If any error happens, it shows an error message.
.The part if __name__ == "__main__": runs the program when you run it as a script.
.The program asks the user for the folder path using input(). If no path is entered, it shows an error.
.If the path is correct, the function zipFolder(path) is called to zip the folder.


assigment 3: Creating a Collage from 4 Images
.First, the program imports os and PIL.Image (from the Pillow library). os is used to check if files exist, and PIL.Image is used to handle images.
.The function createCollage() is where all the work happens.
.It makes an empty list called image_paths to store the paths of the 4 images the user will give.
.The program asks the user to enter the path for each image (Image 1, Image 2, Image 3, and Image 4).
.Then, the user is asked to pick an output format like jpg, png, bmp, or others.
.If the format is not one of jpg, jpeg, png, or bmp, the program shows an error and stops.
.The program checks if the entered image paths exist using os.path.exists(). If any path does not exist, it shows an error and stops.
.The program then tries to open each image with Image.open() and checks if it’s a valid image using .verify().
.If any image is not valid, it shows an error and stops.
.After checking, the program finds the smallest width and height of all images so they can be resized to the same size.
.It resizes each image to match the smallest width and height using .resize().
.The program calculates the size of the collage. Since there are 2 rows and 2 columns, it multiplies the width and height by 2.
.It creates a new blank image for the collage using Image.new() with the calculated size.
.The program pastes each image at the correct place on the collage using .paste().
.Finally, the collage is saved as collage.<output_format>, and a success message is shown.
.The if __name__ == "__main__": part ensures that the createCollage() function runs when the script is executed.



