from googletrans import Translator
from tkinter import *
import tkinter as tk

root = Tk()
entry = tk.Entry(root, width=40)
entry2 = tk.Entry(root, width=40)
text = Label(root, text='Language Translator')
text2 = Label(root, text='Result:')

def translate_text(text, dest_lang='en'):
    translator = Translator()
    translated = translator.translate(text, dest=dest_lang)
    return translated.text

def get_input():
    text = entry.get()
    dest_lang = entry2.get()
    translated_text = translate_text(text, dest_lang)
    text2.config(text=translated_text)

def main():  
    root.title("Translator")
    root.resizable(False, False)
    root_width = 500
    root_height = 300
    root.geometry(f"{root_width}x{root_height}")
    placeholder_text = "Enter your text here (Auto detect)"
    placeholder_dest_lang = "Enter the destination language (en,az,tr)"
    text.pack(pady=10)
    entry.insert(0, placeholder_text)
    entry.pack(pady=10)
    entry2.insert(0, placeholder_dest_lang)
    entry2.pack(pady=10)
    button = tk.Button(root, text='Translate', width=25, command=get_input)
    button.pack(pady=20)
    text2.pack()
    root.mainloop()

if __name__ == "__main__":
    main()