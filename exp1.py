import subprocess
import os
import tkinter as tk
from tkinter import scrolledtext

class UltimateShellGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Ultimate Shell GUI")
        self.current_directory_label = tk.Label(root, text=f"{os.getcwd()}", anchor='w')
        self.current_directory_label.pack(fill='x')
        self.entry = tk.Entry(root, width=80)
        self.entry.pack(pady=10)
        self.output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=30)
        self.output_text.pack(padx=10, pady=10)
        self.command_history = []
        self.entry.bind('<Return>', lambda event: self.execute_command())
    def execute_command(self):
        command = self.entry.get()
        self.entry.delete(0, tk.END)
        if command.lower() == 'clear':
            self.clear_output()
        elif command.lower() == 'history':
            self.print_history()
        elif command.startswith('cd '):
            self.change_directory(command[3:])
        elif command.lower() == 'exit':
            self.root.destroy()
        else:
            self.run_system_command(command)
    def run_system_command(self, command):
        try:
            result = subprocess.run(command, shell=True, text=True, capture_output=True)
            if result.returncode == 0:
                self.display_output(f">> {command}\n{result.stdout}\n")
                self.command_history.append(command)
            else:
                self.display_output(f">> {command}\nError: {result.stderr}\n")
        except Exception as e:
            self.display_output(f">> {command}\nException: {e}\n")

        self.display_output('\n')
    def change_directory(self, new_directory):
        try:
            os.chdir(new_directory)
            self.current_directory_label.config(text=f"Current Directory: {os.getcwd()}")
            self.display_output(f"Changed directory to: {os.getcwd()}\n")
            self.command_history.append("cd "+ new_directory)
        except FileNotFoundError:
            self.display_output(f"Directory not found: {new_directory}\n")
    def print_history(self):
        history_text = "Command history:\n"
        for idx, cmd in enumerate(self.command_history, start=1):
            history_text += f"{idx} {cmd}\n"
        self.display_output(history_text)
    def clear_output(self):
        self.output_text.delete(1.0, tk.END)
    def display_output(self, output):
        self.output_text.insert(tk.END, output)
        self.output_text.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = UltimateShellGUI(root)
    root.mainloop()
