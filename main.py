import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledText
from ttkbootstrap.tooltip import ToolTip
from agnapencrypt import encrypt,decrypt
from password import generate_password
from PIL import Image, ImageTk

def app():
    window=ttk.Window(themename='darkly')
    window.title("agnApenigma")
    window.geometry('600x550')

    window.rowconfigure((0,2),weight=10,uniform='a')
    window.rowconfigure((1,3),weight=3,uniform='a')
    window.columnconfigure((0,1,2,3),weight=1,uniform='a')

    message_frm=ttk.LabelFrame(window,bootstyle="info",text='Message')
    message_frm.grid(row=0,column=0,columnspan=4,sticky='ew',pady=5,padx=5)

    message=ScrolledText(message_frm,padding=6)
    message.pack(expand='True',fill='x')


    button_frm=ttk.Frame(window)
    button_frm.grid(row=1,column=0,columnspan=4,sticky='ew')
    button_frm.columnconfigure((0,1,2,3,4),weight=1,uniform='a')
    button_frm.rowconfigure(0,weight=1,uniform='a')



    key_frm=ttk.LabelFrame(button_frm,bootstyle="info",text='KEY')
    key_frm.grid(row=0,column=1,columnspan=3,sticky='ew')
    key_var=ttk.StringVar(value=4)
    key_enty=ttk.Entry(key_frm,textvariable=key_var)
    ToolTip(key_enty,text='key to encrypt/decrypt.')
    key_enty.pack(pady=5,padx=5,expand='True',fill='x')

    convert_btn=ttk.Button(button_frm,text="encrypt",command= lambda:[clear_output(),encr()])
    convert_btn.grid(row=0,column=0)
    ToolTip(convert_btn,text='press to encrypt the meesage')

    decrypt_btn=ttk.Button(button_frm,text="decrypt",command= lambda:[clear_output(),decr()])
    decrypt_btn.grid(row=0,column=4)
    ToolTip(decrypt_btn,text='press to decrypt the meesage')


    output_frm=ttk.LabelFrame(window,bootstyle="info",text='Output')
    output_frm.grid(row=2,column=0,columnspan=4,sticky='ew',pady=5,padx=5)
    output=ScrolledText(output_frm,padding=6)
    output.pack(expand='True',fill='x')


    def encr():
        content=message.get('1.0', tk.END).strip()
        output.insert('end',encrypt(content,key_var.get()))
        
        
    def decr():
        content=message.get('1.0', tk.END).strip()
        output.insert('end',decrypt(content,key_var.get()))

    def clear_output():
        try:
            output.delete('0.0', tk.END)
        except:
            print("nothing to clear")



    bottom_frm=ttk.Frame(window)
    bottom_frm.grid(row=3,column=0,columnspan=4,sticky='ew')
    bottom_frm.columnconfigure((0,1,2,3,4),weight=1,uniform='a')
    bottom_frm.rowconfigure(0,weight=1,uniform='a')

    generate_key_btn=ttk.Button(bottom_frm,text="generate a key of lenght of ",command=lambda: gen_password())
    generate_key_btn.grid(row=0,column=0,padx=5,columnspan=2)
    ToolTip(generate_key_btn,text='generate a key')

    password_length_var=ttk.StringVar(value=8)
    password_length_spinbox=ttk.Spinbox(bottom_frm,from_=8, to=25, increment=1,state="readonly",textvariable=password_length_var)
    password_length_spinbox.grid(row=0,column=2)

    help_image=Image.open('help.png').resize((20,20))
    help_button_photo=ImageTk.PhotoImage(help_image)

    about_btn=ttk.Button(bottom_frm,text='about',image=help_button_photo,command=lambda: open_about() )
    about_btn.grid(row=0,column=4)
    ToolTip(about_btn,text='know more about agnApenigma')

    def gen_password():
        key_var.set(generate_password(int(password_length_var.get()),True,True))

    def open_about():
        top=ttk.Toplevel()   
        top.title("about agnApenigma")
        top.geometry('405x300')
        top.resizable(False,False)

        message=ttk.ScrolledText(top,padx=10,pady=10,wrap='word')
        
        message.insert('end',"agnApenigma \n\nThis is a simple yet powerful message encrypt and decrypt program. you may able to encrypt text with any formatiing with a specific key\n\n" \
        "Key - you may specify your own key or ask agnApenigma to generate a key for you. key can content anything(alphanumeric). but you must be secure same key to decrypt the encrypted message\n\nIf you do not set specific key, agnApenigma will use its default key value 4 to encrypt and decrypt the message. messages encrypted using agnApenigma can only be decrypted using agnApenigma provided key is available\n\nYou can use Ctrl+c and Ctrl+v to copy and paste data from and to the program\n\nif you are interested to know how agnApenigma is coded, please visit\n\n https://github.com/llranga/agnApenigma \n\nwhich is a public repository and you may able to pull the source code\n\nIf you wish to contact the developer\nagnapcts@gmail.com\n\n\u00A9 agnAp\nColombo,Sri Lanka\n\nV0.1\nChristchurch NZ\n03/05/2025")
        message.pack(expand=True,fill='both')
        message.configure(state='disabled')

    window.mainloop()

if __name__=="__main__":
    app()








