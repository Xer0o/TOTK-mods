import os
import shutil
import sys
from tkinter import messagebox

def backup(self):
    if self.mode == "Yuzu":
        # Fetch the nand_directory value from the qt-config.ini file
        testforuserdir = os.path.join(self.nand_dir, "user", "save", "0000000000000000")
        testforuser = os.listdir(testforuserdir)
        target_folder = "0100F2C0115B6000"
        # checks each individual folder ID for each user and finds the ones with saves for TOTK. Then backups the TOTK saves!
        for root, dirs, files in os.walk(testforuserdir):
            if target_folder in dirs:
                folder_to_backup = os.path.join(root, target_folder)
        print(f"Attemping to backup {folder_to_backup}")
    # Create the 'backup' folder inside the mod manager directory if it doesn't exist
    elif self.mode == "Ryujinx":
        folder_to_backup = self.nand_dir
    script_dir = os.path.dirname(os.path.abspath(sys.executable))
    backup_folder_path = os.path.join(script_dir, "backup")
    os.makedirs(backup_folder_path, exist_ok=True)
    backup_file = "Save.rar"
    file_number = 1
    while os.path.exists(os.path.join(backup_folder_path, backup_file)):
        backup_file = f"Save_{file_number}.rar"
        file_number += 1

    # Construct the full path for the backup file inside the 'backup' folder
    backup_file_path = os.path.join(backup_folder_path, backup_file)

    try:
        # Check if the folder exists before creating the backup
        if os.path.exists(folder_to_backup):
            shutil.make_archive(backup_file_path, "zip", folder_to_backup)
            os.rename(backup_file_path + ".zip", backup_file_path)
            messagebox.showinfo("Backup", f"Backup created successfully: {backup_file}")
        else:
            messagebox.showerror("Backup Error", "Folder to backup not found.")

    except Exception as e:
        messagebox.showerror("Backup Error", f"Error creating backup: {e}")