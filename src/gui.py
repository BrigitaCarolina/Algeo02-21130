from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from extractor import *
from eigen import *
from eigenface import *
import cv2
import os 
from webcam import *
# choose file button 

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        images.append(os.path.join(folder,filename))
        print(images[0])
    return images

def upload_Action(): 
    global filename1
    filename1 = filedialog.askdirectory()
    printfilename = Label(frame1, text=filename1[:30] + "...", font=("Calibri", 12), bg="#DFF2FF").place(x=240, y=210)

def upload_Action1():
    global filename2
    filename2 = filedialog.askdirectory()
    images = load_images_from_folder(filename2)
    # filename2 = filedialog.askopenfilename(title="Select File", filetypes=(("jpeg files", "*.jpg"),("all files", "*.*")))
    printfilename1 = Label(frame1, text=filename2[:30] + "...", font=("Calibri", 12), bg="#DFF2FF").place(x=220, y=310)
    img = ImageTk.PhotoImage(Image.open(images[0]).resize((256, 256), Image.ANTIALIAS))
    displayimg = Label(frame2, image=img)
    displayimg.photo = img
    displayimg.place(x=0,y=150)

def calculate():
    # dir = os.chdir(os.path.pardir)
    print(os.getcwd())
    outputPath = os.path.join(os.getcwd() + "/ALGEO02-21130/test/output/output.jpg")
    #outputPath = os.path.join(os.getcwd() + "/test/output/output.jpg")
    print(outputPath)
    image_arr = extractImages(filename1)
    test_face = extractImages(filename2)
    eigenface, execution_time, flag = Eigenfaces(image_arr, test_face)
    cv2.imwrite(outputPath,np.int_(eigenface))
    if flag: 
        img = ImageTk.PhotoImage(Image.open(outputPath).resize((256, 256), Image.ANTIALIAS))
        displayimg = Label(frame3, image=img)
        displayimg.photo = img
        displayimg.place(x=0,y=150)
        displayTime = Label(frame2, text=str(execution_time), fg="#98FB98", bg="#DFF2FF", font=("Calibri",16)).place(x=150, y=500)
    else:
        #anonymouspath = os.path.join(os.getcwd() + "/img/anonymous.jpg")
        anonymouspath = os.path.join(os.getcwd() + "/ALGEO02-21130/img/anonymous.jpg")
        img = ImageTk.PhotoImage(Image.open(anonymouspath).resize((256, 256), Image.ANTIALIAS))
        displayimg = Label(frame3, image=img)
        displayimg.photo = img
        displayimg.place(x=0,y=150)   
        fail = Label(frame1, text="  Couldn't find matching image!", fg="#98FB98", bg="#DFF2FF", font=("Calibri",16, "bold")).place(x=100, y=500)


def clear():
    parrent_path = os.path.dirname(os.getcwd())
    #imageholderpath = os.path.join(os.getcwd()+ "/img/image holder.jpg")
    imageholderpath = os.path.join(os.getcwd()+ "/ALGEO02-21130/img/image holder.jpg")
    print(imageholderpath) 
    imgholder = ImageTk.PhotoImage(Image.open(imageholderpath).resize((256, 256), Image.ANTIALIAS))
    displayimgholder = Label(frame2, image=imgholder)
    displayimgholder.photo = imgholder
    displayimgholder.place(x=0,y=150)
    imgholder1 = ImageTk.PhotoImage(Image.open(imageholderpath).resize((256, 256), Image.ANTIALIAS))
    displayimgholder1 = Label(frame3, image=imgholder1)
    displayimgholder1.photo = imgholder1
    displayimgholder1.place(x=0,y=150)
    blank = Label(frame1, text=("L" * 50), fg="#DFF2FF" , bg="#DFF2FF", font=("Calibri",12))
    blank.place(x=240, y=210)
    blank1 = Label(frame1, text=("L" * 50), fg="#DFF2FF" , bg="#DFF2FF", font=("Calibri",12))
    blank1.place(x=220, y=310)
    blank1 = Label(frame2, text=("L" * 50), fg="#DFF2FF" , bg="#DFF2FF", font=("Calibri",12))
    blank1.place(x=150, y=500)
    nofile1 = Label(frame1, text="No Folder Chosen", bg="#DFF2FF", font=("Calibri",12))
    nofile1.place(x=240, y=210)
    nofile = Label(frame1, text="No File Chosen", bg="#DFF2FF", font=("Calibri",12))
    nofile.place(x=220, y=310)
    executionTime = Label(frame2, text="00:00:00", fg="#98FB98", bg="#DFF2FF", font=("Calibri",16)).place(x=150, y=500)
    blank2 = Label(frame1, text=("L" * 50), fg="#DFF2FF" , bg="#DFF2FF", font=("Calibri",12))
    blank2.place(x=100, y=500)
    none = Label(frame1, text="  None", fg="#98FB98", bg="#DFF2FF", font=("Calibri",16)).place(x=100, y=500)
# main screen 
window = Tk()
window.title("Face Recognition App")
window.geometry("2000x1010")
frame = Frame(relief = RAISED,
               height=100,
               bg="#DFF2FF")
frame.pack(fill=X)
greeting = Label(frame, text="Face Recognition",fg="#47B8D3",bg="#DFF2FF", font=("Calibri",30,"bold"))
greeting.place(x=600, y=50)

# column 0  
parrent_path = os.path.dirname(os.getcwd())
os.chdir(parrent_path)
imageholderpath = os.path.join(os.getcwd() + "/ALGEO02-21130/img/image holder.jpg")
#imageholderpath = os.path.join(os.getcwd() + "/img/image holder.jpg")
frame1 = Frame(relief = RAISED,
               width=525,
               bg="#DFF2FF")
frame1.pack(side=LEFT,fill=Y)        
dataset = Label(frame1,text="Insert Your Dataset",bg="#DFF2FF",fg="#3E6287", font=("Calibri",16,"bold"))
dataset.place(x=100, y=150)
button = Button(frame1, text= "Choose Folder", fg="#47B8D3", command=upload_Action, font="Calibri")
button.place(x=100, y=200)
nofile1 = Label(frame1, text="No Folder Chosen", bg="#DFF2FF", font=("Calibri",12))
nofile1.place(x=240, y=210)
image = Label(frame1, text="Insert Your Image", bg="#DFF2FF",fg="#3E6287", font=("Calibri",16,"bold"))
image.place(x=100, y=250)   
button1 = Button(frame1, text= "Choose File", fg="#47B8D3", command=upload_Action1, font="Calibri")
button1.place(x=100, y=300)
nofile = Label(frame1, text="No File Chosen", bg="#DFF2FF", font=("Calibri",12))
nofile.place(x=220, y=310)
result = Label(frame1, text="Result :", bg="#DFF2FF", fg="#3E6287", font=("Calibri",16,"bold"))
result.place(x=100, y=450)
none = Label(frame1, text="  None", fg="#98FB98", bg="#DFF2FF", font=("Calibri",16)).place(x=100, y=500)
bttn_calculate = Button(frame1, text="CALCULATE", font=("Calibri",16), fg="white", bg="#47B8D3", command=calculate).place(x=100,y=350)

# column 1
frame2 = Frame(relief = RAISED,
               width=525,
               bg="#DFF2FF")
frame2.pack(side=LEFT,fill=Y) 
test_image = Label(frame2, text="Test image",bg="#DFF2FF",fg="#3E6287", font=("Calibri",16,"bold"))
test_image.place(x=0, y=75)
execution = Label(frame2, text="Execution Time : ",bg="#DFF2FF", fg="#3E6287", font=("Calibri",16,"bold"))
execution.place(x=0, y=500)
executionTime = Label(frame2, text="00:00:00", fg="#98FB98", bg="#DFF2FF", font=("Calibri",16)).place(x=150, y=500)
imgholder = ImageTk.PhotoImage(Image.open(imageholderpath).resize((256, 256), Image.ANTIALIAS))
displayimgholder = Label(frame2, image=imgholder)
displayimgholder.photo = imgholder
displayimgholder.place(x=0,y=150)
bttn_capture = Button(frame2, text="Use Webcam", font=("Calibri",16), fg="white", bg="#47B8D3", command=videowebcam).place(x=0,y=450)
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
imgholder1 = ImageTk.PhotoImage(Image.open(imageholderpath).resize((256, 256), Image.ANTIALIAS))
displayimgholder1 = Label(frame3, image=imgholder1)
displayimgholder1.photo = imgholder1
displayimgholder1.place(x=0,y=150)
bttn_clear = Button(frame3, text="Clear Result", font=("Calibri",16), fg="white", bg="#47B8D3", command=clear).place(x=0,y=450)
window.mainloop()
