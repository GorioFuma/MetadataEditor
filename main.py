from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from exif import Image as ImageExif
from warnings import filterwarnings
from tkinter import messagebox

filterwarnings("ignore")
backgroundcolor="#ffcc00"
bluecolor="#00C8FF"
gray="#CCCCCC"

root=Tk()
root.iconbitmap("images/logo.ico")
root.config(bg=backgroundcolor)
root.title("Metadata Editor")
root.geometry("1000x670")

blue=ImageTk.PhotoImage(Image.open("images/blue.png"))
bluelabel=Label(root, image=blue, bd=0, bg=backgroundcolor)
bluelabel.place(x=540, y=0)

def savefunc(event=None):
    global vermake
    print(varmake.get())
    myimage.make=varmake.get()
    myimage.model=varmodel.get()
    myimage.datetime=vardatetime.get()
    myimage.software=varsoftware.get()
    try:
        if varpixelx.get()=="/":
            myimage.pixel_x_dimension=0
        else:
            myimage.pixel_x_dimension=int(varpixelx.get())
    except:
        pass
    try:
        if varpixely.get()=="/":
            myimage.pixel_y_dimension=0
        else:
            myimage.pixel_y_dimension=int(varpixely.get())
    except:
        pass
    myimage.gps_latitude_ref=varlatref.get()
    
    #latitude
    try:
        if varlatitude.get()=="/":
            myimage.gps_latitude=(0, 0, 0)
        else:
            varlat=varlatitude.get().replace("(", "")
            varlat=varlat.replace(")", "")
            varlat=varlat.replace(",", "")
            latlist=varlat.split(" ")
            print(latlist)
            myimage.gps_latitude=(latlist[0], latlist[1], latlist[2])
    except:
        pass
    myimage.gps_longitude_ref=varlongref.get()
    
    #longitude
    try:
        if varlongitude.get()=="/":
            myimage.gps_longitude=(0, 0, 0)
        else:
            varlong=varlongitude.get().replace("(", "")
            varlong=varlong.replace(")", "")
            varlong=varlong.replace(",", "")
            longlist=varlong.split(" ")
            print(longlist)
            myimage.gps_longitude=(longlist[0], longlist[1], longlist[2])
    except:
        pass
    
    fileimage=open(filename, "wb")
    fileimage.write(myimage.get_file())
    fileimage.close()
    
def clear():
    vardatetime.set("/")
    varlatitude.set("/")
    varlatref.set("/")
    varlongitude.set("/")
    varlongref.set("/")
    varmake.set("/")
    varmodel.set("/")
    varpixelx.set("/")
    varpixely.set("/")
    varsoftware.set("/")

def deleteexif():
    ask=messagebox.askquestion("Metadata Editor", "Do you want to delete all exif data?")
    if ask=="yes":
        clear()
        savefunc()
    
def readdata(path):
    global myimage, varmake
    myimage=ImageExif(path)
    val=myimage.has_exif
    print(val)
    if val==True:
        try:
            print(myimage.make)
            varmake.set(myimage.make)
        except:
            pass
        try:
            print(myimage.model)
            varmodel.set(myimage.model)
        except:
            pass
        try:
            print(myimage.datetime)
            vardatetime.set(myimage.datetime)
        except:
            pass
        try:
            print(myimage.software)
            varsoftware.set(myimage.software)
        except:
            pass
        try:
            print(myimage.pixel_x_dimension)
            varpixelx.set(myimage.pixel_x_dimension)
        except:
            pass
        try:
            print(myimage.pixel_y_dimension)
            varpixely.set(myimage.pixel_y_dimension)
        except:
            pass
        try:
            print(myimage.gps_latitude_ref)
            varlatref.set(myimage.gps_latitude_ref)
        except:
            pass
        try:
            print(myimage.gps_latitude)
            varlatitude.set(myimage.gps_latitude)
        except:
            pass
        try:
            print(myimage.gps_longitude_ref)
            varlongref.set(myimage.gps_longitude_ref)
        except:
            pass
        try:
            print(myimage.gps_longitude)
            varlongitude.set(myimage.gps_longitude)
        except:
            pass
        
def read():
    filename = filedialog.askopenfilename(title='')
    return filename

def openimage(event=None):
    global filename, imagelabel1
    filename=read()
    if filename!="":
        try:
            imagelabel1.pack_forget()
        except:
            pass
        imagelabel.pack_forget()
        image1=ImageTk.PhotoImage(Image.open(filename).resize((400, 354)))
        clear()
        readdata(filename)
        imagelabel1=Label(root, image=image1, bg=bluecolor, bd=0)
        imagelabel1.image=image1
        imagelabel1.pack(side=TOP, anchor=NE, padx=28, pady=28)
        imagelabel1.bind("<Button-1>", openimage)
    
    
image=ImageTk.PhotoImage(Image.open("images/image.png"))
imagelabel=Label(root, image=image, bg=bluecolor)
imagelabel.pack(side=TOP, anchor=NE, padx=28, pady=28)
imagelabel.bind("<Button-1>", openimage)

back=ImageTk.PhotoImage(Image.open("images/back.png"))
backlabel=Label(root, image=back, bd=0)
backlabel.place(x=50, y=50)

#save
save=ImageTk.PhotoImage(Image.open("images/save.png"))
savebutton=Button(root, image=save, activebackground=backgroundcolor, bg=backgroundcolor, bd=0, command=savefunc)
savebutton.place(x=635, y=445)

#delete
delete=ImageTk.PhotoImage(Image.open("images/delete.png"))
deletebutton=Button(root, image=delete, activebackground=backgroundcolor, bg=backgroundcolor, bd=0, command=deleteexif)
deletebutton.place(x=635, y=545)


#make
varmake=StringVar()
Label(root, text="Make: ", font=("Calibri",22, "bold"), bg=gray).place(x=60, y=60)
Label(root, text="_________________", font=("Calibri",22, "bold"), bg=gray).place(x=175, y=60)
make=Entry(root, textvariable=varmake, bd=0, bg=gray, justify=CENTER, font=("Calibri",15, "bold")).place(x=200, y=65)

#model
varmodel=StringVar()
Label(root, text="Model: ", font=("Calibri",22, "bold"), bg=gray).place(x=60, y=115)
Label(root, text="_________________", font=("Calibri",22, "bold"), bg=gray).place(x=175, y=115)
model=Entry(root, textvariable=varmodel, bd=0, bg=gray, justify=CENTER, font=("Calibri",15, "bold")).place(x=200, y=115)

#datetime
vardatetime=StringVar()
Label(root, text="Datetime: ", font=("Calibri",20, "bold"), bg=gray).place(x=60, y=170)
Label(root, text="_________________", font=("Calibri",22, "bold"), bg=gray).place(x=175, y=170)
datetime=Entry(root, textvariable=vardatetime, bd=0, bg=gray, justify=CENTER, font=("Calibri",15, "bold")).place(x=200, y=170)

#software
varsoftware=StringVar()
Label(root, text="Software: ", font=("Calibri",20, "bold"), bg=gray).place(x=60, y=225)
Label(root, text="_________________", font=("Calibri",22, "bold"), bg=gray).place(x=175, y=225)
software=Entry(root, textvariable=varsoftware, bd=0, bg=gray, justify=CENTER, font=("Calibri",15, "bold")).place(x=200, y=225)

#pixelx
varpixelx=StringVar()
Label(root, text="Pixel X: ", font=("Calibri",20, "bold"), bg=gray).place(x=60, y=280)
Label(root, text="_________________", font=("Calibri",22, "bold"), bg=gray).place(x=175, y=280)
pixelx=Entry(root, textvariable=varpixelx, bd=0, bg=gray, justify=CENTER, font=("Calibri",15, "bold")).place(x=200, y=280)

#pixely
varpixely=StringVar()
Label(root, text="Pixel Y: ", font=("Calibri",20, "bold"), bg=gray).place(x=60, y=335)
Label(root, text="_________________", font=("Calibri",22, "bold"), bg=gray).place(x=175, y=335)
pixely=Entry(root, textvariable=varpixely, bd=0, bg=gray, justify=CENTER, font=("Calibri",15, "bold")).place(x=200, y=335)

#latref
varlatref=StringVar()
Label(root, text="Lat. ref: ", font=("Calibri",20, "bold"), bg=gray).place(x=60, y=390)
Label(root, text="_________________", font=("Calibri",22, "bold"), bg=gray).place(x=175, y=390)
latref=Entry(root, textvariable=varlatref, bd=0, bg=gray, justify=CENTER, font=("Calibri",15, "bold")).place(x=200, y=390)

#lat
varlatitude=StringVar()
Label(root, text="Latitude: ", font=("Calibri",20, "bold"), bg=gray).place(x=60, y=445)
Label(root, text="_________________", font=("Calibri",22, "bold"), bg=gray).place(x=175, y=445)
lat=Entry(root, textvariable=varlatitude, bd=0, bg=gray, justify=CENTER, font=("Calibri",15, "bold")).place(x=200, y=445)

#longref
varlongref=StringVar()
Label(root, text="Long. ref: ", font=("Calibri",20, "bold"), bg=gray).place(x=60, y=500)
Label(root, text="_________________", font=("Calibri",22, "bold"), bg=gray).place(x=175, y=500)
longref=Entry(root, textvariable=varlongref, bd=0, bg=gray, justify=CENTER, font=("Calibri",15, "bold")).place(x=200, y=500)

#long
varlongitude=StringVar()
Label(root, text="Longitude: ", font=("Calibri",20, "bold"), bg=gray).place(x=60, y=555)
Label(root, text="_________________", font=("Calibri",22, "bold"), bg=gray).place(x=175, y=555)
long=Entry(root, textvariable=varlongitude, bd=0, bg=gray, justify=CENTER, font=("Calibri",15, "bold")).place(x=200, y=555)

clear()

root.mainloop()