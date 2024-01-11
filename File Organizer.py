#import the necessary modules

from pathlib import *  #to convert files to paths
import os              #to access and manipulate directories
import shutil          #to move files to specific locations/directories

#Declare a dictionary list of directories and their formats
#more can be added depending on the file formats available in the location
Directories = {
    "Pictures": ['.jpeg', '.jpg', '.gif', '.png'],
    'Videos': ['.wmv', '.mov', '.mp4','.mpg', '.mpeg', '.mkv'],
    'Zip_Folder': ['.iso', '.tar', '.gz', '.rz', '.7z','.dmg','.rar', '.zip'],
    'Music': ['.mp3', '.msv','.wav', '.wma'],
    'PDF_Folder': ['.pdf'],
}
#Create a new dictionary file extensions as keys and directories as values
#example: {'.jpeg':'Pictures', '.png':'Pictures','.mp4':'Videos'}
File_Format = {file_format: directory for directory, file_format_stored in Directories.items() for file_format in file_format_stored}

#Define a function to build your code
def File_Organizer():

    #change the cwd to the path of files to be organized
    os.chdir(r'path')
    
    #Try and except statement to catch possible errors
    try:
        #iterate over files in the cwd with the scandir method of os in order to extract each file format 
        #A directory is created for each file format per the dictionary list.
        #Each file is then moved to their respective directories with the shutil module
        for file in os.scandir():
            
            #convert file to file path
            path=Path(file)
            file_ext=path.suffix
    
            if file.is_dir():
                continue
            else:
                if file_ext in File_Format:
                    os.makedirs(File_Format[file_ext], exist_ok=True)
                    shutil.move(file,File_Format[file_ext])
                else:
                    os.makedirs('Others',exist_ok=True)
                    shutil.move(file,'Others')
        for dir in os.listdir():
            dir=sorted(Path(dir).iterdir(), key=os.path.getmtime)
        print('File(s) successfully organized')
    except:
        print('An error occured during operation')

File_Organizer()