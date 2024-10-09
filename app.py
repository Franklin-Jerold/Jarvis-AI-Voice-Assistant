import tkinter as tk
from tkinter import ttk
import jarvis
import sys

class VoiceAssistantGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Jarvis Voice Assistant")
        self.root.geometry("900x500")

        # Add header label
        self.header_label = ttk.Label(root, text="Jarvis Voice Assistant", font=("Helvetica", 20, "bold"))
        self.header_label.pack(pady=10)

        # Add input entry
        

        # Add output text area with scrollbar
        self.output_text = tk.Text(root, height=20, width=100)
        self.scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.output_text.yview)
        self.output_text.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill="y")
        self.output_text.pack(pady=5)

        # Redirect stdout to the Text widget
        sys.stdout = self

        # Add speak button
        
        self.speak_button = ttk.Button(root, text="Speak", command=self.execute_jarvis_main)
        self.speak_button.pack(pady=10)

        self.input_label = ttk.Label(root, text="🎙")
        self.input_label.pack()

        self.input_label = ttk.Label(root, text="Developed by Franklin",font=("Helvetica", 10, "bold"))
        self.input_label.pack()

    def execute_jarvis_main(self):
        self.output_text.delete('1.0', tk.END)  # Clear the output text
        jarvis.main()

    def write(self, text):
        # Write the text to the Text widget
        self.output_text.insert(tk.END, text)
        self.output_text.see(tk.END)  # Scroll to the bottom
        self.output_text.update_idletasks()  # Update the Tkinter GUI to reflect changes immediately

def main():
    root = tk.Tk()
    app = VoiceAssistantGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
