from tkinter import *
from tkinter.filedialog import askdirectory
from PIL import Image,ImageTk
from pytube import YouTube
from threading import *
from tkinter.messagebox import askyesno

file_size = 0 # File Size

def downThread(): #Download Thread
    thread = Thread(target=downloader)
    thread.start()


def progress(chunk, file_handle, remaining): #Monitor Progress
    global download_status
    file_downloaded = file_size - remaining
    percent = (file_downloaded/file_size) * 100
    download_status.config(text= '{:00.0f} % downloaded'.format(percent))


def downloader(): #Download
    global file_size, download_status
    download_button.config(state = DISABLED)
    download_status.place(x = 230, y = 250)
    try:
        url1 = url.get()
        path = askdirectory()
        yt = YouTube(url1, on_progress_callback=progress)
        video = yt.streams.filter(progressive= True, file_extension='mp4').first()
        file_size = video.filesize
        video.download(path)
        download_status.config(text = 'Finish')
        res = askyesno("YouTube Video Downloader","Do You Want To Download Another Video?")
        if res == 1:
            url.delete(0,END)
            download_button.config(state = NORMAL)
            download_status.confg(text = '')
        else:
            root.destroy()
    except Exception as e:
        download_status.config(text = 'Failed!')
    

root = Tk()#Window
root.geometry("600x400")#SIZE OF WINDOW
root.iconbitmap(r"C:\\Users\\acer\\Downloads\\Icon.ico")

root.title("YOUTUBE VIDEO DOWNLOADER")
root['bg'] = 'white'
root.resizable(0,0)

img = Image.open(r"C:\\Users\\acer\\Downloads\\Icon.ico")
img = img.resize((80,80), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
head = Label(root, image = img)
head.config(anchor = CENTER)
head.pack()

enter_url = Label(root, text = 'Enter URL', bg = 'white')
enter_url.config(font = ('Verdana',15))
enter_url.place(x = 5, y = 120)
url = Entry(root, width = 25, border = 1, relief = SUNKEN, font = ('Verdana',15))
url.place(x = 125, y = 123)
download_button_img = Image.open(r"C:\Users\\acer\\Downloads\\dwd.png")
download_button_img = download_button_img.resize((200,150),Image.ANTIALIAS)
download_button_img = ImageTk.PhotoImage(download_button_img)

download_button = Button(root, width = 160, height = 45, bg = 'white', relief = FLAT, activebackground = 'red', command = downThread)
download_button.config(image = download_button_img)
download_button.place(x = 220, y = 170)
download_status = Label(root, text = 'Please Wait...', font = ('Verdana',15), bg = 'white')
root.mainloop()
