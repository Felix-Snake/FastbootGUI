import tkinter as tk
from tkinter import ttk
from PIL import ImageTk
from pyperclip import copy
from tkinter import filedialog as fd
import subprocess
from tkinter import scrolledtext as st # scrolledtext is loaded module of tkinte, and you can't use: "tk.scrolledtext.something"

"""""""""
-------------------------------------------
Tab 1 (Flash)
"""""""""
def flash_page(tab1:tk.Frame)->None:
    """
    Configurate flash page(Frame). 

    Parameters:
        tab1(tk.Frame) : A tab(tkinter Frame) for flash page.
    """
    def flashing()->None:
        """
        Use command from function_field1_t1(tkinter Entry)
        """
        command = function_field1_t1.get()
        subprocess.check_output(command, shell=True)

    def flash()->None:
        """
        Create input string for fastboot and insert it into function_field1_t1(tkinter Entry). 
        If the image file is not selected, paste "Please select the .img file" into function_field2_t1
        """
        field2 = function_field2_t1.get()
        partition = selected.get()
        function_field1_t1.delete(0, tk.END)


        if field2 == "" or "Please, choose .img file" in field2 :
            function_field2_t1.delete(0, tk.END)
            function_field2_t1.insert(0, "Please, choose .img file")

        else:
            function_field1_t1.insert(0, f"fastboot flash {partition} {field2}")



    def btn_copy()->None:
        """
        Copy to clipboard function. Using pyperclip.
        """
        copy(function_field1_t1.get())

    def get_file()->None:
        """Get image file.

        Requesting an image file via File Explorer.
        """
        file = fd.askopenfilename(
            title="Choose image for flashing",filetypes=[("img", "*.img*")]
        )
        function_field2_t1.delete(0, tk.END)

        function_field2_t1.insert(0, file)

    lbl1_t1 = tk.Label(tab1, text='Function(shell)', font=("Arial", 12))  
    lbl1_t1.place(x=300, y=0)
    function_field1_t1 = tk.Entry(tab1, width=50, font=("Arial", 10))  
    function_field1_t1.place(x=205, y=25)
    btn_copy_t1 = tk.Button(tab1, text="❏", command=btn_copy, width=2, height=1)  
    btn_copy_t1.place(x=575, y=20)

    lbl2_t1 = tk.Label(tab1, text='Path to image(.img)', font=("Arial", 12))  
    lbl2_t1.place(x=285, y=50)
    function_field2_t1 = tk.Entry(tab1, width=50, font=("Arial", 10))  
    function_field2_t1.place(x=205, y=75)
    btn_find_t1 = tk.Button(tab1, text="⌕", command=get_file, width=2, height=1)  
    btn_find_t1.place(x=575, y=75)

    selected = tk.StringVar()
    rad_butt_boot = tk.Radiobutton(tab1, text='Boot', value="boot", variable=selected, font=("Arial", 12), width=30, selectcolor='red', indicatoron=0, command=flash) 
    rad_butt_recovery = tk.Radiobutton(tab1, text='Recovery', value="recovery", variable=selected, font=("Arial", 12), width=30, selectcolor='red', indicatoron=0, command=flash)  
    rad_butt_system = tk.Radiobutton(tab1, text='System', value="system", variable=selected, font=("Arial", 12), width=30, selectcolor='red', indicatoron=0, command=flash)
    rad_butt_userdata = tk.Radiobutton(tab1, text='Userdata', value="userdata", variable=selected, font=("Arial", 12), width=30, selectcolor='red', indicatoron=0, command=flash)
    rad_butt_radio = tk.Radiobutton(tab1, text='Radio', value="radio", variable=selected, font=("Arial", 12), width=30, selectcolor='red', indicatoron=0, command=flash)
    rad_butt_cache = tk.Radiobutton(tab1, text='Cache', value="cache", variable=selected, font=("Arial", 12), width=30, selectcolor='red', indicatoron=0, command=flash)

    rad_butt_boot.place(x=5, y=180)
    rad_butt_recovery.place(x=5, y=210)
    rad_butt_system.place(x=5, y=240)
    rad_butt_userdata.place(x=5, y=270)
    rad_butt_radio.place(x=5, y=300)
    rad_butt_cache.place(x=5, y=330)

    btn_flash_t1 = tk.Button(tab1, text='Flash', command=flashing, width=20, height=5, font=("Arial", 12))  
    btn_flash_t1.place(x=455, y=250)

"""""""""
-------------------------------------------
Tab 2 (Earse)
"""""""""
def erase_page(tab2:tk.Frame)->None:
    """
    Configurate erase page(Frame). 

    Parameters:
        tab2(tk.Frame) : A tab(tkinter Frame) for erase page.
    """
    def btn_copy()->None:
        """
        Copy to clipboard function. Using pyperclip.
        """
        copy(function_field1_t2.get())

    def erase()->None:
        """
        Create input string for fastboot and insert it into function_field1_t2(tkinter Entry)
        """
        partition = selected.get()
        function_field1_t2.delete(0, tk.END)
        function_field1_t2.insert(0, f"fastboot erase {partition}")
       

    def erasing()->None:
        """
        Use command from function_field1_t2(tkinter Entry)
        """
        command = function_field1_t2.get()
        print(subprocess.check_output(command, shell=True))

    lbl1_t2 = tk.Label(tab2, text='Function(shell)', font=("Arial", 12))  
    lbl1_t2.place(x=300, y=0)
    function_field1_t2 = tk.Entry(tab2, width=50, font=("Arial", 10))  
    function_field1_t2.place(x=205, y=25)
    btn_copy_t2 = tk.Button(tab2, text="❏", command=btn_copy, width=2, height=1)  
    btn_copy_t2.place(x=575, y=20)

    selected = tk.StringVar()
    rad_butt_boot = tk.Radiobutton(tab2, text='Boot', value="boot", variable=selected, font=("Arial", 12), width=30, selectcolor='red', indicatoron=0, command=erase) 
    rad_butt_recovery = tk.Radiobutton(tab2, text='Recovery', value="recovery", variable=selected, font=("Arial", 12), width=30, selectcolor='red', indicatoron=0, command=erase)  
    rad_butt_system = tk.Radiobutton(tab2, text='System', value="system", variable=selected, font=("Arial", 12), width=30, selectcolor='red', indicatoron=0, command=erase)
    rad_butt_userdata = tk.Radiobutton(tab2, text='Userdata', value="userdata", variable=selected, font=("Arial", 12), width=30, selectcolor='red', indicatoron=0, command=erase)
    rad_butt_radio = tk.Radiobutton(tab2, text='Radio', value="radio", variable=selected, font=("Arial", 12), width=30, selectcolor='red', indicatoron=0, command=erase)
    rad_butt_cache = tk.Radiobutton(tab2, text='Cache', value="cache", variable=selected, font=("Arial", 12), width=30, selectcolor='red', indicatoron=0, command=erase)

    rad_butt_boot.place(x=5, y=180)
    rad_butt_recovery.place(x=5, y=210)
    rad_butt_system.place(x=5, y=240)
    rad_butt_userdata.place(x=5, y=270)
    rad_butt_radio.place(x=5, y=300)
    rad_butt_cache.place(x=5, y=330)

    btn_earse_t2 = tk.Button(tab2, text='Erase', command=erasing, width=20, height=5, font=("Arial", 12))  
    btn_earse_t2.place(x=455, y=250)

"""""""""
-------------------------------------------
Tab 3 (DeviceInfo)
"""""""""
def DevInfo_page(tab3:tk.Frame)->None:
    """
    Configurate device information page(Frame). 

    Parameters:
        tab3(tk.Frame) : A tab(tkinter Frame) for device information page.
    """
    def getvar()->None:
        """
        Use get command for fastboot and put all info in ScrolledText tkinter object
        """
        txt.delete(1.0, tk.END)
        lbl1_t3.config(text="")
        result = subprocess.check_output("fastboot getvar all", shell=False)
        txt.insert(tk.INSERT, result.decode('utf-8'))


    lbl1_t3 = tk.Label(tab3, text='Please insert your device', font=("Arial", 12))  
    lbl1_t3.place(x=250, y=0)
    btn_get_t3 = tk.Button(tab3, text='CheckInfo', command=getvar, width=20, height=5, font=("Arial", 12))  
    btn_get_t3.place(x=455, y=50)
    txt = st.ScrolledText(tab3, width=40, height=10)  
    txt.place(x=10, y=50) 

"""""""""
-------------------------------------------
Tab 4 (Reboot)
"""""""""
def reboot_page(tab4:tk.Frame)->None:
    """
    Configurate reboot page(Frame). 

    Parameters:
        tab4(tk.Frame) : A tab(tkinter Frame) for reboot page.
    """
    def btn_copy()->None:
        """
        Copy to clipboard function. Using pyperclip.
        """
        copy(function_field1_t4.get())

    def reboot()->None:
        """
        Create input string for fastboot and insert it into function_field1_t4(tkinter Entry)
        """
        mode = selected.get() # Get value from tkinter radiobutton

        function_field1_t4.delete(0, tk.END) # Clear Entry
        function_field1_t4.insert(0, f"fastboot reboot{mode}")

    def rebooting()->None:
        """
        Use command from function_field1_t4(tkinter Entry)
        """
        command = function_field1_t4.get()
        subprocess.check_output(command, shell=True)

    lbl1_t4 = tk.Label(tab4, text='Function(shell)', font=("Arial", 12))  
    lbl1_t4.place(x=250, y=0) 
    function_field1_t4 = tk.Entry(tab4, width=50, font=("Arial", 10))  
    function_field1_t4.place(x=205, y=25)
    btn_copy_t4 = tk.Button(tab4, text="❏", command=btn_copy, width=2, height=1)  
    btn_copy_t4.place(x=575, y=20)

    selected = tk.StringVar()
    rad_butt_standart = tk.Radiobutton(tab4, text='Normal reboot', value="", variable=selected, font=("Arial", 12), width=30, selectcolor='red', indicatoron=0, command=reboot)
    rad_butt_recovery = tk.Radiobutton(tab4, text='Recovery', value=" recovery", variable=selected, font=("Arial", 12), width=30, selectcolor='red', indicatoron=0, command=reboot) 
    
    rad_butt_standart.place(x=5, y=180)
    rad_butt_recovery.place(x=5, y=210)

    btn_reboot_t4 = tk.Button(tab4, text='Reboot', command=rebooting, width=20, height=5, font=("Arial", 12))  
    btn_reboot_t4.place(x=455, y=250)


def main()->None:
    """Main function. 

    Start FastbootGUI
    """
    window = tk.Tk()
    window.title("FastbootGUI")
    window.geometry('670x400')
    window.resizable(0, 0)
    window.iconphoto(True, ImageTk.PhotoImage(file="icon.png"))

    tab_control = ttk.Notebook(window)  

    tab1 = ttk.Frame(tab_control)  
    tab2 = ttk.Frame(tab_control)  
    tab3 = ttk.Frame(tab_control) 
    tab4 = ttk.Frame(tab_control)   

    tab_control.add(tab1, text='Flash')  
    tab_control.add(tab2, text='Earse') 
    tab_control.add(tab3, text='DeviceInfo') 
    tab_control.add(tab4, text='Reboot')  

    flash_page(tab1)
    erase_page(tab2)
    DevInfo_page(tab3)
    reboot_page(tab4)

    tab_control.pack(expand=1, fill='both') 



    window.mainloop()

if __name__ == "__main__":
    main()