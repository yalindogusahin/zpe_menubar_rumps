from tailscale_api import api_call
from web_browser import webbrowser_open
import customtkinter
'''

'''
list_of_devices = []
list_of_devices = api_call()
x=0
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("200x100")
app.title("Tailscale Nodegrid Launcher")

def button_function(x):
    print(x)
    
    webbrowser_open("https://"+x)
    
#button = customtkinter.CTkButton(master=app, text=i, command=lambda: button_function(list_of_devices)).grid(row=x+1, column=0, padx=10, pady=10)
def button_callback():
    button_function(combobox_1.get())

combobox_1 = customtkinter.CTkComboBox(app, values=list_of_devices)
combobox_1.pack(pady=10, padx=10)
combobox_1.set("Select Nodegrid Host")


button_1 = customtkinter.CTkButton(master=app, command=button_callback, text="Open Web Browser")
button_1.pack(pady=10, padx=10)


app.mainloop()