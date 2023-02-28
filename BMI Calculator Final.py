# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 05:03:40 2023

@author: p
"""

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
window=Tk()
window.geometry("340x420")
window.configure(bg='#175117')
window.resizable(0,0)
window.title('BMI Calculator  مؤشر كتلة الجسم')
frame=Frame(window,width = 330, height = 80,bg='#268726')
frame.pack(side=TOP)
labelAddress=Label(window,text='(BMI) Body Mas Index',bg='#268726',fg='white',font=('century 18 bold'),justify=CENTER)
labelAddress.place(x=25,y=20)
img_icon= Image.open('health-care.png')
photo = ImageTk.PhotoImage(img_icon)
window.wm_iconphoto(False, photo)
def calculate_bmi():
    try:
        m=float(Height_input.get())/100.0 ###To convert from c to m
        kg=float(Weight_input.get())
        bmi=kg/(m**2)
        bmi=round(bmi,1) ### to give decimal digits
        bmi_index(bmi)
    except ZeroDivisionError:
        messagebox.showinfo("Result", "Please enter positive height!!")
    except ValueError:
        messagebox.showinfo("Result", "Please enter valid data!")
          
def bmi_index(bmi):
    m=float(Height_input.get())/100.0
    if bmi <18.5:
        ideal_wieght=18.5*(m**2)
        ideal_wieght=round(ideal_wieght,1)
        messagebox.showinfo('The BMI-Result',f'you are under wieght. your BMI is :{bmi}. You shold reach at least {ideal_wieght} KG to become healthy!!')
    elif  18.0<=bmi<=24.9:
        ideal_wieght=24.9*(m**2)
        ideal_wieght=round(ideal_wieght,1)
        messagebox.showinfo('The BMI-Result',f'you are healthy. your BMI is :{bmi}. Bravoo! You reach the ideal wieght {ideal_wieght} KG. Ideal and healthy wieght!!')
    elif  25.0<=bmi<=29.9:
        ideal_wieght=24.9*(m**2)
        ideal_wieght=round(ideal_wieght,1)
        messagebox.showinfo('The BMI-Result',f'you are over wieght. your BMI is :{bmi}. You shold reach at least {ideal_wieght} KG to become healthy!!')
 
    else:
        messagebox.showinfo('The BMI-Result',f'you are obese. your BMI is :{bmi}')
def Reset_Entry():
    Age_input.delete(0,'end')
    Height_input.delete(0,'end')
    Weight_input.delete(0,'end')
    


######Insert Image  ###########
image= Image.open('fmale.png')
image.thumbnail((70, 70),Image.Resampling.LANCZOS)
photo=ImageTk.PhotoImage(image)
label_image=Label(image= photo,bg='#175117')
label_image.place(x=90,y=90)

image2=Image.open('male.png')
image2.thumbnail((70,70),Image.Resampling.LANCZOS)
photo2=ImageTk.PhotoImage(image2)
labe2_image=Label(image= photo2,bg='#175117')
labe2_image.place(x=180,y=90)
###### Radiobutton ############
redvar=IntVar()
rdibtnf=Radiobutton(window,variable=redvar,value=1,bg='#175117',fg='orange')
rdibtnf.place(x=90,y=160)
femalelabel=Label(window,text='Female',font=('arial 8 bold'),bg='#175117',fg='white')
femalelabel.place(x=108,y=162)
rdibtnm=Radiobutton(window,variable=redvar,value=2,bg='#175117',fg='orange')
rdibtnm.place(x=187,y=160)
malelabel=Label(window,text='Male',font=('arial 8 bold'),bg='#175117',fg='white')
malelabel.place(x=205,y=162)
############ scale & Entry   ################
# to conect scale with entry:
    # create IntVar -----entry==textvriable----scale==variable
Age=Label(window,text='Age',bg='#175117',fg='white',font=('arial 16 bold'))
Age.place(x=25,y=200)
var1=IntVar()
sc1=Scale(window,from_=0,to=100,fg='white',highlightbackground='#175117',troughcolor='orange',orient=HORIZONTAL,length=160,bg='#175117',bd=0,sliderlength=10,variable=var1)
sc1.place(x=90,y=190)

Age_input=Entry(window,width=5,fg='#175117',font=('century 8 bold'),bd=0,textvariable=var1)
Age_input.place(x=275,y=209)

Height=Label(window,text='Height',bg='#175117',fg='white',font=('arial 12 bold'))
Height.place(x=20,y=245)
var2=IntVar()
sc2=Scale(window,from_=0.0,to=250,resolution=0.01,fg='white',highlightbackground='#175117',troughcolor='orange',orient=HORIZONTAL,length=160,bg='#175117',bd=0,sliderlength=10,variable=var2)
sc2.place(x=90,y=230)

Height_input=Entry(window,width=5,fg='#175117',font=('century 8 bold'),bd=0,textvariable=var2)
Height_input.place(x=275,y=250)

Weight=Label(window,text='Weight',bg='#175117',fg='white',font=('arial 12 bold'))
Weight.place(x=20,y=290)
var3=IntVar()
sc3=Scale(window,from_=0.0,to=250,resolution=0.01,fg='white',highlightbackground='#175117',troughcolor='orange',orient=HORIZONTAL,length=160,bg='#175117',bd=0,sliderlength=10,variable=var3)
sc3.place(x=90,y=270)

Weight_input=Entry(window,width=5,fg='#175117',font=('century 8 bold'),bd=0,textvariable=var3)
Weight_input.place(x=275,y=290)

calacBtn=Button(window,width=13,bg='#268726',text='Calculate BMI',fg='white',font=('arial 12 bold'),command=calculate_bmi)
calacBtn.place(x=40,y=330)
resetBtn=Button(window,width=13,bg='#268726',text='Reset',fg='white',font=('arial 12 bold'),command=Reset_Entry)
resetBtn.place(x=170,y=330)

window.mainloop()



