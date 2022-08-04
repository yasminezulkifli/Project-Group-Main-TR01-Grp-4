from pathlib import Path
import sys
import os
import csv

sys.path.append('  ')


def get_path_to_project_folder(name_of_file): #this will either be api, coh, oh, pl 
    path_to_project_folder = os.path.abspath(os.path.join(os.getcwd(), os.pardir)) 
    #getting parent directory for example: the parent directory of a path C:\folder\subfolder\myfile. txt is C:\folder\subfolder 
    print("PROJECT FOLDER (PARENT): {0}".format(path_to_project_folder)) 
    #in this case, parent folder refers to "CSV FILES"// 

    path_to_text_files = os.path.join(path_to_project_folder, "app\\csv_reports")
    print("TEXT FILES FOLDER: {0}".format(path_to_text_files))
    # finding file.txt under the subfolder 

    path_to_text_files_extension = os.path.join(path_to_text_files, name_of_file)
    print("NAME OF FILE ADDED TO PATH: {0}".format(path_to_text_files_extension))
    # finding specific files 
    
    print()

    return path_to_text_files_extension


def read_in_text_file(path_to_text_files_extension):
    with open(path_to_text_files_extension, newline='') as csvfile:
        list_of_dictionaries = list(csv.DictReader(csvfile))
        return list_of_dictionaries

# reference for "os" https://stackoverflow.com/questions/2860153/how-do-i-get-the-parent-directory-in-python