import os
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

class FileSystemGUI:

    def __init__ (self, master): 
        self.master = master
        self.master.title("File System GUI")

        self.current_folder = tk.StringVar() 
        self.current_folder.set(os.getcwd())

        self.create_widgets()
    
    def create_widgets(self):
        self.folder_label = tk.Label(self.master, textvariable=self.current_folder)
        self.folder_label.pack(pady=5)

        self.frame = tk.Frame(self.master) 
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.frame)

        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.file_list = tk.Listbox(self.frame, yscrollcommand=self.scrollbar.set, selectmode=tk.SINGLE)
        self.file_list.pack(fill=tk.BOTH, expand=True) 
        self.scrollbar.config(command=self.file_list.yview) 
        self.list_files()
        self.browse_button = tk.Button(self.master, text="Browse", command=self.browse_folder)
        self.browse_button.pack(pady=5)

        self.create_file_button = tk.Button(self.master, text="Create File", command=self.create_file)
        self.create_file_button.pack(side=tk.LEFT, padx=5) 
        self.rename_button = tk.Button(self.master, text="Rename",
        command=self.rename_selected) 
        self.rename_button.pack(side=tk.LEFT, padx=5) 
        self.delete_button = tk.Button(self.master, text="Delete",
        command=self.delete_selected) 
        self.delete_button.pack(side=tk.RIGHT, padx=5)
        self.create_folder_button = tk.Button(self.master, text="Create Folder", command=self.create_folder)
        self.create_folder_button.pack(side=tk.RIGHT, padx=5) 
        self.file_list.bind("<Double-1>", self.open_folder)

    def list_files(self): 
        self.file_list.delete(0, tk.END) 
        self.file_list.insert(tk.END, "..")
        for item in os.listdir(self.current_folder.get()): 
            self.file_list.insert(tk.END, item)

    def browse_folder(self):
        folder_path = filedialog.askdirectory() 
        if folder_path:
            self.current_folder.set(folder_path) 
            self.list_files()

    def open_folder(self, event):
        selection = self.file_list.curselection() 
        if selection:
            selected_item = self.file_list.get(selection[0]) 
            if selected_item == "..":
                parent_folder = os.path.dirname(self.current_folder.get()) 
                self.current_folder.set(parent_folder)
            else:
                new_folder = os.path.join(self.current_folder.get(),
        selected_item)

                if os.path.isdir(new_folder): 
                    self.current_folder.set(new_folder)
            self.list_files()

    def create_file(self):
        file_name = simpledialog.askstring("Create File", "Enter file name:")
        if file_name:
            file_path = os.path.join(self.current_folder.get(), file_name) 
            try:
                open(file_path, 'a').close()	# Create empty file self.list_files()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to create file: {str(e)}")

    def create_folder(self):
        folder_name = simpledialog.askstring("Create Folder", "Enter folder name:")
        if folder_name:
            folder_path = os.path.join(self.current_folder.get(), folder_name)
            try:
                os.mkdir(folder_path) 
                self.list_files()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to create folder:{str(e)}")

    def delete_selected(self):
        selection = self.file_list.curselection() 
        if selection:
            selected_item = self.file_list.get(selection[0]) 
            if selected_item == "..":
                messagebox.showerror("Error", "Cannot delete parentfolder.")

            else:
                confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete '{selected_item}'?")
                if confirm: 
                    try:
                        path = os.path.join(self.current_folder.get(), selected_item)

                        if os.path.isdir(path): 
                            os.rmdir(path)
                        else:
                            os.remove(path) 
                        self.list_files()
                    except Exception as e:
                        messagebox.showerror("Error", f"Failed to delete: {str(e)}")

    def rename_selected(self):
        selection = self.file_list.curselection() 
        if selection:
            selected_item = self.file_list.get(selection[0])
            if selected_item == "..":
                messagebox.showerror("Error", "Cannot rename parentfolder.")

            else:
                new_name = simpledialog.askstring("Rename", f"Enter new name for '{selected_item}':")
                if new_name: 
                    try:
                        os.rename(os.path.join(self.current_folder.get(), selected_item), 
                        os.path.join(self.current_folder.get(), new_name))
                        self.list_files()
                    except Exception as e:
                        messagebox.showerror("Error", f"Failed to rename: {str(e)}")

def main():
    root = tk.Tk()
    app = FileSystemGUI(root) 
    root.mainloop()

if __name__	== "__main__": 
    print("hello")
    main()