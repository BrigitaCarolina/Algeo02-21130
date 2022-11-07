from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

# choose file button 
def upload_Action(): 
    filename1 = filedialog.askopenfilename()
    printfilename = Label(text=filename1).grid(row=2, column=1)

def upload_Action1():
    filename2 = filedialog.askopenfilename()
    printfilename = Label(text=filename2).grid(row=4, column=1)
    img = ImageTk.PhotoImage(Image.open(filename2).resize((256, 256), Image.ANTIALIAS))
    displayimg = Label(image=img)
    displayimg.photo = img
    displayimg.grid(row=2,column=2)

window = Tk()
window.title("Face Recognition App")
window.geometry("500x500")
# window.columnconfigure(0, minsize=800, weight=1)
greeting = Label(text="Face Recognition", justify="center",font=200)
greeting.grid(row=0, column=1)
# greeting.grid(row=0)
# column 0  
dataset = Label(text="Insert Your Dataset")
dataset.grid(row=1, column=0)
button = Button(text= "Choose File", fg="#00FFFC", command=upload_Action)
button.grid(row=2, column=0)
button1 = Button(text= "Choose File", fg="#00FFFC", command=upload_Action1)
button1.grid(row=4, column=0)
image = Label(text="Insert Your Image")
image.grid(row=3, column=0)   
nofile = Label(text="No File Chosen")
nofile.grid(row=2, column=1)
nofile1 = Label(text="No File Chosen")
nofile1.grid(row=4, column=1)
result = Label(text="Result")
result.grid(row=5, column=0)
none = Label(text="  None", fg="#98FB98").grid(row=6, column=0)

# column 1 
test_image = Label(text="Test image")
test_image.grid(row=1, column=2)
execution = Label(text="Execution time : ", padx=3)
execution.grid(row=3, column=2)
time = Label(text="00.00", fg="#98FB98").grid(row=3, column=3)

# creating frame to display the test image 
# frame1 = Frame(window, width=256, height=256).grid(row=2, column=2)
# frame2 = Frame(window, width=256, height=256).grid(row=2, column=3)

# column 2 
closet_result = Label(text="Closest Result")
closet_result.grid(row=1, column=3)
window.mainloop()
