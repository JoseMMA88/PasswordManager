from tkinter import *
from tkinter import messagebox
import pyperclip
import random
import string
import json


FONT = ("Verdana", 10, "bold")


# Password generator
def generate_random_password():
    if len(input_3.get()) > 0:
        input_3.delete(0, END)

    random_source = string.ascii_letters + string.digits + string.punctuation
    password_list = [random.choice(random_source) for i in range(12)]

    random.shuffle(password_list)
    password = ''.join(password_list)
    pyperclip.copy(password)
    input_3.insert(0, password)


# Save Password
def save_data():

    website = input.get()
    user = input_2.get()
    password = input_3.get()
    new_data = {
        website: {
            "user": user,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Campos necesarios", message="Has dejado campos sin rellenar.\n Porfavor rellénelos.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Estos son los datos intrudcidos\n Usuario: {user}\n"
                                                      f" Contraseña: {password}\n ¿Son correctos?")

        if is_ok:
            try:
                with open("user_data.json", "r") as file:
                    # Reading old data
                    data = json.load(file)
            except FileNotFoundError:
                with open("user_data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                # Updating data with new data
                data.update(new_data)

                with open("user_data.json", "w") as file:
                    # Saving updated data
                    json.dump(data, file, indent=4)
            finally:
                print("Guardado!!")
                input.delete(0, END)
                input_3.delete(0, END)


# Search data
def search():
    try:
        website = input.get()
        with open("user_data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showwarning(title="Información no encontrada", message=f"No hay información de "
                                                                          f"{website} en el manejador de contraseñas")
    else:
        if website in data:
            user = data[website]["user"]
            password = data[website]["password"]
            messagebox.showwarning(title=website, message=f"Usuario: {user}\n Contraseña: {password}")
        else:
            messagebox.showwarning(title="Información no encontrada", message=f"No hay información de "
                                                                              f"{website} en el manejador de contraseñas")




# UI Setup
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)


# Website
label = Label(text="Web:", font=FONT)
label.grid(column=0, row=1)
input = Entry(width=32)
input.focus()
input.grid(column=1, row=1)

# Search
button_search = Button(text="Buscar", width=13, command=search)
button_search.grid(column=2, row=1)

# Email / User
label_2 = Label(text="Email/Usuario:", font=FONT)
label_2.grid(column=0, row=2)
input_2 = Entry(width=50)
input_2.insert(0, "contact@josemalagon.es")
input_2.grid(column=1, row=2, columnspan=2)

# Password
label_3 = Label(text="Contraseña:", font=FONT)
label_3.grid(column=0, row=3)
input_3 = Entry(width=32)
input_3.grid(column=1, row=3)
button = Button(text="Generar Aleatoria", command=generate_random_password)
button.grid(column=2, row=3)

# Add
button = Button(text="Añadir", width=42, command=save_data)
button.grid(column=1, row=4, columnspan=2)

window.mainloop()
