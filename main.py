import tkinter as tk
from tkinter import ttk, scrolledtext
from PIL import ImageTk, Image
import keyboard
import chatgptinterface as chatgpt

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"
 
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 15 bold"

def msg(chatbox,text):
    prompt = chatbox.get()
    chatbox.delete(0,'end')
    if prompt == '':
        return
    text.insert('end', '\n\nYOU --> '+prompt)
    response = chatgpt.generate_prompt(prompt)
    text.insert('end', '\nAI: '+response)
    

class ChatWindow:
    def __init__(self, master):
        self.master = master
        master.title("AI Interface")
        master.geometry('500x800')
        master.configure(bg=BG_GRAY)
        master.resizable(width=False, height=False)
        master.attributes('-topmost', 1)

        self.label = tk.Label(master, text="Talk with an AI!",pady=6,padx=10,height=1, font=FONT_BOLD,bg=BG_GRAY)
        self.label.pack(anchor = 'nw')

        self.text = tk.Text(master, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=43,height=33)
        self.text.pack()
        self.text.insert('end', 'AI: Hello, how can I assist you?')

        chatbox = tk.Entry(master, width=80,bg=TEXT_COLOR)
        chatbox.bind('<Return>', lambda event: msg(chatbox,self.text))
        chatbox.pack(anchor='w',padx=5,pady=5)



root = tk.Tk()

gui = ChatWindow(root)

root.lift()
root.mainloop()
    
    

