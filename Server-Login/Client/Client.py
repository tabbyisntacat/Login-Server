import socket
import customtkinter


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("Localhost",9999))

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

root.geometry("500x350")


def login():
    client.send(entry1.get().encode())
    client.send(entry2.get().encode())
    print(client.recv(1024).decode())




frame = customtkinter.CTkFrame(master = root)
frame.pack(pady=20,padx=60,fill="both",expand=True)

label = customtkinter.CTkLabel(master=frame,text = "Login")
label.pack(pady=12,padx=10)

entry1 =customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12,padx=10)

entry2 =customtkinter.CTkEntry(master=frame, placeholder_text="Password",show=".")
entry2.pack(pady=12,padx=10)


button = customtkinter.CTkButton(master=frame,text="Login",command=login)
button.pack(pady=12,padx=10)
root.mainloop()