from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
# choose file button 
def upload_Action(): 
    filename1 = filedialog.askopenfilename()
    printfilename = Label(text=filename1).grid(row=2, column=1)

def upload_Action1():
    filename2 = filedialog.askopenfilename()
    printfilename = Label(frame1, text=filename2, font=("Calibri", 12), bg="#DFF2FF").place(x=200, y=300)
    img = ImageTk.PhotoImage(Image.open(filename2).resize((256, 256), Image.ANTIALIAS))
    displayimg = Label(frame2, image=img)
    displayimg.photo = img
    displayimg.place(x=0,y=200)

window = Tk()
window.title("Face Recognition App")
window.geometry("2000x1000")
# window.columnconfigure(0, minsize=800, weight=1)
frame = Frame(relief = RAISED,
               height=100,
               bg="#DFF2FF")
frame.pack(fill=X)
greeting = Label(frame, text="Face Recognition",fg="#47B8D3",bg="#DFF2FF", font=("Calibri",30,"bold"))
greeting.place(x=600, y=50)
# greeting.grid(row=0)
# column 0  
frame1 = Frame(relief = RAISED,
               width=525,
               bg="#DFF2FF")
frame1.pack(side=LEFT,fill=Y)        
dataset = Label(frame1,text="Insert Your Dataset",bg="#DFF2FF",fg="#3E6287", font=("Calibri",16,"bold"))
dataset.place(x=100, y=150)
button = Button(frame1, text= "Choose Folder", fg="#47B8D3", command=upload_Action, font="Calibri")
button.place(x=100, y=200)
nofile1 = Label(frame1, text="No Folder Chosen", bg="#DFF2FF", font=("Calibri",12))
nofile1.place(x=210, y=200)
image = Label(frame1, text="Insert Your Image", bg="#DFF2FF",fg="#3E6287", font=("Calibri",16,"bold"))
image.place(x=100, y=250)   
button1 = Button(frame1, text= "Choose File", fg="#47B8D3", command=upload_Action1, font="Calibri")
button1.place(x=100, y=300)
nofile = Label(frame1, text="No File Chosen", bg="#DFF2FF", font=("Calibri",12))
nofile.place(x=200, y=300)
result = Label(frame1, text="Result :", bg="#DFF2FF", fg="#3E6287", font=("Calibri",16,"bold"))
result.place(x=100, y=450)
none = Label(frame1, text="  None", fg="#98FB98", bg="#DFF2FF", font=("Calibri",16)).place(x=100, y=500)
bttn_calculate = Button(frame1, text="CALCULATE", font=("Calibri",16), fg="white", bg="#47B8D3").place(x=100,y=350)

# column 1
frame2 = Frame(relief = RAISED,
               width=525,
               bg="#DFF2FF")
frame2.pack(side=LEFT,fill=Y) 
test_image = Label(frame2, text="Test image",bg="#DFF2FF",fg="#3E6287", font=("Calibri",16,"bold"))
test_image.place(x=0, y=75)
execution = Label(frame2, text="Execution Time : ",bg="#DFF2FF", fg="#3E6287", font=("Calibri",16,"bold"))
execution.place(x=0, y=500)
time = Label(frame2, text="00:00:00", fg="#98FB98", bg="#DFF2FF", font=("Calibri",16)).place(x=150, y=500)
imgholder = ImageTk.PhotoImage(Image.open("image holder.jpg").resize((256, 256), Image.ANTIALIAS))
displayimgholder = Label(frame2, image=imgholder)
displayimgholder.photo = imgholder
displayimgholder.place(x=0,y=200)
# creating frame to display the test image 
# frame1 = Frame(window, width=256, height=256).grid(row=2, column=2)
# frame2 = Frame(window, width=256, height=256).grid(row=2, column=3)

# column 2 
frame3 = Frame(relief = RAISED,
               width=525,
               bg="#DFF2FF")
frame3.pack(side=LEFT,fill=BOTH) 
closet_result = Label(frame3, text="Closest Result", bg="#DFF2FF",fg="#3E6287", font=("Calibri",16,"bold"))
closet_result.place(x=0, y=75)
imgholder1 = ImageTk.PhotoImage(Image.open("image holder.jpg").resize((256, 256), Image.ANTIALIAS))
displayimgholder1 = Label(frame3, image=imgholder1)
displayimgholder1.photo = imgholder1
displayimgholder1.place(x=0,y=200)
window.mainloop()
