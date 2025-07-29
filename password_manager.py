import tkinter as tk
from tkinter import messagebox
import json
import os
import cryptography.fernet import Fernet

DATA_FILE = "data.enc"
KEY_FILE = "key.key"

def load_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as key_file:
            return key_file.read()

    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)
        return key

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = fernet.decrypted(encrypted_data)
        return json.loads(decrypted_data.decode())
    except:
        return {}

def save_data(data):
    encrypted_data = fernet.encrypt(json.dumps(data).encode())
    with open(DATA_FILE, "wb") as file:
        file.write(enrypted_data)

def save_entry():
    website = entry_website.get()
    username = entry_username.get()
    password = entry_password.get()

    if not website or not username or not password:
        messagebox.showwarning("Fehler", "Bitte alle Felder ausfüllen")
        return

    data = load_data()
    data[website] =  {"username": username, "password": password}
    save_data(data)

    messagebox.showinfo("Gespeichert", f"Eintrag für {website} gespeichert.")
    entry_website.delete(0, tk.END)
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)

key = load_key()
fernet = Fernet(key)

root = tk.Tk()
root.title("Password Manager")

tk.Label(root, text="Website:").grid(row=0, column=0)
entry_website = tk.Entry(root, width=30)
entry_website.grid(row=0, column=1)

tk.Label(root, text="Benutnername:").grid(row=1, column=0)
entry_username = tk.Entry(root, width=30)
entry_username.grid(row=1, column=1)

tk.Label(root, text="Passwort:").grid(row=2, column=0)
entry_password = tk.Entry(root, width=30)
entry_password.grid(row=2, column=1)

tk.Button(root, text="Speichern", command=save_entry).grid(row=3, column=1, pady=10)
root.mainloop()