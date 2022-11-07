from tkinter import *
root = Tk()
root.geometry("650x500")
root.title("Face Recognition")
root.configure(background="#282829")

Label(root,text="Masukkan direktori file foto : ", font="baloo 10", bg="#282829", fg="white").grid(row=0,column=0,sticky=W,padx=3,pady=10)
namaFile = Entry(root)
namaFile.grid(row=0,column=1,sticky=W, ipady=3)
err_namaFile = Label(root, bg="#282829", fg="white")
err_namaFile.grid(row=1,column=1,sticky=W)
# browse = PhotoImage(file="foto/browse.png")
Button(root,text='Browse File', border=0, bg="#282829", activebackground="#282829").grid(row=0,column=2,sticky=W,padx=3)

Label(root,text="Masukkan banyak foto : ", font="baloo 10", bg="#282829", fg="white" ).grid(row=2,column=0,sticky=W,padx=3,pady=10)
banyakFoto = Entry(root)
banyakFoto.grid(row=2,column=1,sticky=W,ipady=3)
err_banyakFoto = Label(root, bg="#282829", fg="white")
err_banyakFoto.grid(row=3,column=1,sticky=W)

# pilihan = IntVar()
# pilihan.set(-1)
# err_pilihan = Label(root, bg="#282829", fg="white")
# err_pilihan.grid(row=4,column=0,sticky=W)
# cosineON = PhotoImage(file="foto/cosineON.png")
# cosineOFF = PhotoImage(file="foto/cosineOFF.png")
# euclidianON = PhotoImage(file="foto/euclidianON.png")
# euclidianOFF = PhotoImage(file="foto/euclidianOFF.png")

Radiobutton(
    root,
    text="Cosine Similarity",
    # variable=pilihan,
    value=0,
    indicatoron=False,
    # image=cosineOFF,
    # selectimage=cosineON,
    border=0,
    selectcolor="#282829",
    activebackground="#282829",
    highlightbackground="#282829",
    bg="#282829").grid(row=5,column=0,sticky=W)

Radiobutton(
    root, 
    text="Euclidean Distance",
    # variable=pilihan,
    value=1,
    indicatoron=False,
    # image=euclidianOFF,
    # selectimage=euclidianON,
    bd=0,
    selectcolor="#282829",
    activebackground="#282829",
    highlightbackground="#282829",
    bg="#282829").grid(row=5,column=1,sticky=W)

# compare_img = PhotoImage(file="foto/compare.png")
Button(
    root,
    text="Compare",
    # command=compare,
    # image=compare_img,
    border=0,
    activebackground="#282829",
    bg="#282829").grid(row=10,column=0,sticky=W,padx=3,pady=5)
result=Label(root, justify=LEFT, bg="#282829", fg="white")
result.grid(row=11,column=0,sticky=W)

root.mainloop()