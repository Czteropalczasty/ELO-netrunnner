# generates copy to my obsidian

import os
import shutil


def copy_files(source_folder, destination_folder):
    # Ensure the destination folder exists
    os.makedirs(destination_folder, exist_ok=True)

    # Iterate through all files in the source folder
    for filename in os.listdir(source_folder):
        source_file = os.path.join(source_folder, filename)

        # Check if it's a file
        if os.path.isfile(source_file):
            # Copy the file to the destination folder
            shutil.copy(source_file, destination_folder)
            print(f"Copied: {source_file} to {destination_folder}")


def copy_single_file(source_file_path, destination_folder):
    # Ensure the destination folder exists
    os.makedirs(destination_folder, exist_ok=True)

    # Get the filename from the source file path
    filename = os.path.basename(source_file_path)

    # Check if the source file exists
    if os.path.isfile(source_file_path):
        # Copy the file to the destination folder
        shutil.copy(source_file_path, destination_folder)
        print(f"Copied: {source_file_path} to {destination_folder}")
    else:
        print(f"File does not exist: {source_file_path}")


def copy_all_analysis():
    # Example usage
    source_folder = 'Players_elo_graphs'
    destination_folder = '/home/ioke/personal/Obsidian_osobiste/Osobiste/Osobiste/Hobby/Netrunner/ELO Netrunner/Players_elo_graphs'
    copy_files(source_folder, destination_folder)


    # Example usage
    source_file_path = 'Analysis.md'  # Full path to the specific file to copy
    destination_folder = '/home/ioke/personal/Obsidian_osobiste/Osobiste/Osobiste/Hobby/Netrunner/ELO Netrunner/'  # Destination folder
    copy_single_file(source_file_path, destination_folder)
