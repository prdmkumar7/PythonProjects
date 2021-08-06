import tkinter as tk
from tkinter import*
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
win = Tk()
win.title("YT Downloader")
win.geometry('350x300')
win.columnconfigure(0,weight=1)

Folder_Name = ""
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()

def DownloadVideo():
    url = url_var.get()
    quality = quality_var.get()
    my_video = YouTube(url)
    if quality=='720':
        select = my_video.streams.filter(progressive=True).first()
    elif quality=='144':
        select = my_video.streams.filter(progressive=True).last()
    elif  quality=='Only Audio':
        select = my_video.streams.filter(only_audio=True).first()

    select.download(Folder_Name)
        


url_label = ttk.Label(win, text = "Enter the URL of Video:", font = ('jost',15))
url_label.grid(pady=2)
url_label.configure(foreground='Black',background='#E9C7EA')



url_var = tk.StringVar()
url_entry = ttk.Entry(win, width=50, textvariable = url_var)
url_entry.grid(pady=2)

save_label = ttk.Label(win, text = "Save the Video File", font = ("jost",12))
save_label.grid(pady=2)
save_label.configure(foreground='Black',background='#E9C7EA')


pathbtn = tk.Button(win, text="Choose Path", fg = 'Black', bg='Red',command=openLocation)
pathbtn.grid(pady=2)

quality_label = ttk.Label(win, text = "Select the Quality", font = ('jost',12))
quality_label.grid(pady=2)
quality_label.configure(foreground='Black',background='#E9C7EA')

quality_var = tk.StringVar()
quality_combobox = ttk.Combobox(win, width = 20,textvariable = quality_var, state = "readonly")
quality_combobox['values'] = ('720', '144', 'Only Audio')
quality_combobox.grid(pady=2)

downloadbtn = tk.Button(win, text = "Download", fg = 'Black', bg = 'Red', command=DownloadVideo)
downloadbtn.grid(pady=2)


# developer_name_label = ttk.Label(win, text = "")
# developer_name_label.grid()
# developer_name_label = ttk.Label(win, text = "")
# developer_name_label.grid()


developer_name_label = ttk.Label(win, text = "Developed By Praduman")
developer_name_label.grid(pady=50)
developer_name_label.configure(foreground='Black',background='#F99A4C')



win.mainloop()