from random import *
from turtle import *
import colorsys
from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
import turtle
from math import *
from hashlib import *
import psutil
import platform
from datetime import datetime
import time
import qrcode
import image
import multiprocessing
from tkinter import filedialog as fd
# ------------------------         -------------------------        ----------------------------            ------------------          ----------------
win = Tk()
win.geometry('1000x600+170+50')
win.config(background="#F8D004")
win.resizable()
win.title("Bouzid's First Desktop Application")
# ------------------------------------------------------------------------------------------------------------------------------------------------------
menubar = Menu(win)
f = Menu(menubar,tearoff=0)
f.add_command(label='Copy')
f.add_command(label='New File')
f.add_command(label='Save')
f.add_command(label='Save As')
f.add_separator()
f.add_command(label='Exit',command=win.quit)
menubar.add_cascade(label='File',menu=f)
win.config(menu=menubar)
nb = ttk.Notebook(win)
f0 = Frame(nb,width='1000',height='600',background='orange')
nb.add(f0,text='Turtle & Art')
# --------------
f1 = Frame(nb,width='800',height='600',background='#246EE9',highlightbackground="red")
nb.add(f1,text='Calculator')
f2 = Frame(nb,width='1000',height='600',background='chocolate2')
nb.add(f2,text='hash & cyptography')
f3 = Frame(nb,width='800',height='600',background='green')
nb.add(f3,text='youtube downoader')
f4 = Frame(nb,width='800',height='600',background='#246EE9')
nb.add(f4,text='QR maker')
f5 = Frame(nb,width='800',height='600',background='gray')
nb.add(f5,text='text editor')
f6 = Frame(nb,width='800',height='600',background='white')
nb.add(f6,text='about')
f7 = Frame(nb,width='800',height='600',background='gray')
nb.add(f7,text='hardware info')
nb.pack()

# ----------------------------------------------------------------------------------------------------------------
# the calculator frame :
fc = Frame(f1,width=380,height=540,bg='white')
fc.place(x=20,y=20)
# ---------------
# the first entry box :

e1 = Label(f1,width=37,height=6,fg='black',bg='#F8D004',font=90)
e1.place(x=42,y=40)
e1.config()

# the label of answer:
lb1 = Label(f1,text='RESULT',width=37,height=4,fg='white',bg='#246EE9',font=("arial",12),border=0)
lb1.place(x=42,y=170)
#
v =StringVar() 
writing_space = Entry(f2,bg="white",text='enter',font=("arial",30),width=27,border=0,textvariable=v).place(x=30,y=30)
# Qr code Frame
qr_text_label = Label(f4,bg="#246EE9",text='enter text to make it Qrcode :',fg="white",font=("arial",12,"bold")).place(x=10,y=30)
qr_text =StringVar()
qr_text_window = Entry(f4,width=60,bg='white',fg='black',font=("arial",16,"bold"),textvariable=qr_text).place(x=240,y=30)
qr_name =StringVar()
qr_name_label = Label(f4,bg="#246EE9",text='enter your Qrcode name :',fg="white",font=("arial",13,"bold")).place(x=10,y=80)
qr_name_window = Entry(f4,width=60,bg='white',fg='black',font=("arial",16,"bold"),textvariable=qr_name).place(x=240,y=80)
button_creator = Button(f4,text='create Qrcode image',height=2,width=20,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center',font=("arial",12,"bold"),command=lambda:create_Qr_code()).place(x=760,y=120)
# -----------------------------------------
list_of_bgcolors = ttk.Menubutton(f4,text="color of Qrcode")
list_of_bgcolors.place(x=240,y=120)
s2 = Menu(list_of_bgcolors,tearoff=0,bg="yellow")
list_of_bgcolors['menu']=s2
def menubutton_spec(a):
    global qr_bgcolor
    list_of_bgcolors.config(text=a)
    qr_bgcolor=a
qr_bgcolor = "white"
s2.add_radiobutton(label='white',background="white",command=lambda:menubutton_spec("white"))
s2.add_radiobutton(label='khaki1',background="khaki1",command=lambda:menubutton_spec("khaki1"))
s2.add_radiobutton(label='yellow',background="yellow",command=lambda:menubutton_spec("yellow"))
s2.add_radiobutton(label='green yellow',background="green yellow",command=lambda:menubutton_spec("green yellow"))
s2.add_radiobutton(label='SpringGreen2',background="SpringGreen2",command=lambda:menubutton_spec("SpringGreen2"))
s2.add_radiobutton(label='green3',background="green3",command=lambda:menubutton_spec("green3"))
s2.add_radiobutton(label='green4',background="green4",command=lambda:menubutton_spec("green4"))
s2.add_radiobutton(label='cyan',background="#30BFBF",command=lambda:menubutton_spec("SteelBlue1"))
s2.add_radiobutton(label='blue',background="blue",command=lambda:menubutton_spec("blue"))
s2.add_radiobutton(label='cyan',background="cyan",command=lambda:menubutton_spec("cyan"))
s2.add_radiobutton(label='aquamarine3',background="aquamarine3",command=lambda:menubutton_spec("aquamarine3"))
s2.add_radiobutton(label='grey',background="grey",command=lambda:menubutton_spec("grey"))
s2.add_radiobutton(label='brown',background="brown",command=lambda:menubutton_spec("brown"))
s2.add_radiobutton(label='goldenrod3',background="goldenrod3",command=lambda:menubutton_spec("goldenrod3"))
s2.add_radiobutton(label='orange',background="orange",command=lambda:menubutton_spec("orange"))
s2.add_radiobutton(label='red',background="red",command=lambda:menubutton_spec("red"))
s2.add_radiobutton(label='hotpink',background="hotpink",command=lambda:menubutton_spec("hotpink"))
s2.add_radiobutton(label='magenta2',background="magenta2",command=lambda:menubutton_spec("magenta2"))
s2.add_radiobutton(label='purple3',background="purple3",command=lambda:menubutton_spec("purple3"))

# 
list_of_colors = ttk.Menubutton(f4,text="color of background")
list_of_colors.place(x=40,y=120)
s = Menu(list_of_colors,tearoff=0,bg="yellow")
list_of_colors['menu']=s
def menubutton2_spec(a):
    global qr_color
    list_of_colors.config(text=a)
    qr_color=a
qr_color = "black"
s.add_radiobutton(label='white',background="white",command=lambda:menubutton2_spec("white"))
s.add_radiobutton(label='khaki1',background="khaki1",command=lambda:menubutton2_spec("khaki1"))
s.add_radiobutton(label='yellow',background="yellow",command=lambda:menubutton2_spec("yellow"))
s.add_radiobutton(label='green yellow',background="green yellow",command=lambda:menubutton2_spec("green yellow"))
s.add_radiobutton(label='SpringGreen2',background="SpringGreen2",command=lambda:menubutton2_spec("SpringGreen2"))
s.add_radiobutton(label='green3',background="green3",command=lambda:menubutton2_spec("green3"))
s.add_radiobutton(label='green4',background="green4",command=lambda:menubutton2_spec("green4"))
s.add_radiobutton(label='cyan',background="#30BFBF",command=lambda:menubutton2_spec("SteelBlue1"))
s.add_radiobutton(label='blue',background="blue",command=lambda:menubutton2_spec("blue"))
s.add_radiobutton(label='cyan',background="cyan",command=lambda:menubutton2_spec("cyan"))
s.add_radiobutton(label='aquamarine3',background="aquamarine3",command=lambda:menubutton2_spec("aquamarine3"))
s.add_radiobutton(label='grey',background="grey",command=lambda:menubutton2_spec("grey"))
s.add_radiobutton(label='brown',background="brown",command=lambda:menubutton2_spec("brown"))
s.add_radiobutton(label='goldenrod3',background="goldenrod3",command=lambda:menubutton2_spec("goldenrod3"))
s.add_radiobutton(label='orange',background="orange",command=lambda:menubutton2_spec("orange"))
s.add_radiobutton(label='red',background="red",command=lambda:menubutton2_spec("red"))
s.add_radiobutton(label='hotpink',background="hotpink",command=lambda:menubutton2_spec("hotpink"))
s.add_radiobutton(label='magenta2',background="magenta2",command=lambda:menubutton2_spec("magenta2"))
s.add_radiobutton(label='purple3',background="purple3",command=lambda:menubutton2_spec("purple3"))

def create_Qr_code ():
    global qr_text
    global qr_bgcolor
    global qr_color
    qr_text = qr_text.get()
    global qr_name
    qr_name = qr_name.get()
    qr = qrcode.QRCode(
        version=12,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=8
    )
    qr.add_data(f"{qr_text}")
    qr.make(fit=True)
    img = qr.make_image(fill_color=qr_color,back_color=qr_bgcolor)  
    img.save(f"C:\\Users\\Dtech\\Desktop\\{qr_name}.jpg") 
    win.update()
    qr_bgcolor ="black"
    qr_color ="white"
# writing buttons functions :
equation=""
def show(value):
    global equation
    if (len(equation)%34==0 and len(equation)!=0) :
        l = equation+"\t"+value
        e1.config(text=l)
        equation+=value
    else:
        equation+=value
        e1.config(text=equation)
    pass
def clear():
    global equation
    equation=""
    e1.config(text=equation)
    lb1.config(text="")
def dels():
    global equation
    equation=equation[:-1:]
    e1.config(text=equation)
def calculate():
    global equation
    k = equation
    k = k.replace("x","*")
    k=k.replace("^","**")
    result=""
    if (equation!=""):
        try:
            result=eval(k)
        except:
            result ="SYNTAX ERROR"
            equation=""
    lb1.config(text=result)
def exp_2():
    lb1.config(text=exp(float(eval(equation))))
def sin_2():
     lb1.config(text=sin(radians(float(eval(equation)))))
def cos_2():
     lb1.config(text=cos(radians(float(eval(equation)))))
def sqrt_2():
     lb1.config(text=sqrt(float(eval(equation))))
def ln_2():
     lb1.config(text=log2(float(eval(equation))))
def log_2():
     lb1.config(text=log10(float(eval(equation))))
def tan_2():
     lb1.config(text=tan(radians(float(eval(equation)))))
def fact_2():
     lb1.config(text=factorial(int(eval(equation))))  
def save():
    global v
    return v.get()
def clear_s():
    text = save() 
    encrypted_text = ""
    hash_space.config(text=encrypted_text)
def sha_1():
    text = save() 
    encrypted_text = sha1(text.encode()).hexdigest()
    hash_space.config(text=encrypted_text)
def sha_224():
    text = save() 
    encrypted_text = sha224(text.encode()).hexdigest()
    hash_space.config(text=encrypted_text)
def sha_256():
    text = save() 
    encrypted_text = sha256(text.encode()).hexdigest()
    hash_space.config(text=encrypted_text)
def sha_384():
    text = save() 
    encrypted_text = sha384(text.encode()).hexdigest()
    hash_space.config(text=encrypted_text)
def sha_512():
    text = save() 
    encrypted_text = sha512(text.encode()).hexdigest()
    hash_space.config(text=encrypted_text)
def MD_5():
    text = save() 
    encrypted_text = md5(text.encode()).hexdigest()
    hash_space.config(text=encrypted_text)
def save_2():
    global k
    return k.get()
def run_my_code():
    global code_result1
    text = save_2() 
    code_in_string = compile(text,'sumstring','exec')
    code_in_object = exec(code_in_string)
    # code_result.
# def copy(text):
#     cmd='echo'+text.strip()+'|pbcopy'
#     return check_call(cmd,shell=True)
# -------------------------------------------------------
# first buttons line
btn1 = Button(f1,text='+',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center',font=("arial",8,"bold"),command=lambda:show("+")).place(x=40,y=270)
btn2 = Button(f1,text='-',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center',font=("arial",8,"bold"),command=lambda:show("-")).place(x=110,y=270)
btn3 = Button(f1,text='1',height=2,width=8,fg='black',bg='#3EB489',border=0,activebackground='red',anchor='center',font=("arial",8,"bold"),command=lambda:show("1")).place(x=180,y=270)
btn4 = Button(f1,text='2',height=2,width=8,fg='black',bg='#3EB489',border=0,activebackground='red',anchor='center',font=("arial",8,"bold"),command=lambda:show("2")).place(x=250,y=270)
btn5 = Button(f1,text='3',height=2,width=8,fg='black',bg='#3EB489',border=0,activebackground='red',anchor='center',font=("arial",8,"bold"),command=lambda:show("3")).place(x=320,y=270)
# second buttons line
btn6 = Button(f1,text='x',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center',font=("arial",8,"bold"),command=lambda:show("x")).place(x=40,y=315)
btn7 = Button(f1,text='/',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center',font=("arial",8,"bold"),command=lambda:show("/")).place(x=110,y=315)
btn8 = Button(f1,text='4',height=2,width=8,fg='black',bg='#3EB489',border=0,activebackground='red',anchor='center',font=("arial",8,"bold"),command=lambda:show("4")).place(x=180,y=315)
btn9 = Button(f1,text='5',height=2,width=8,fg='black',bg='#3EB489',border=0,activebackground='red',anchor='center',font=("arial",8,"bold"),command=lambda:show("5")).place(x=250,y=315)
btn10 = Button(f1,text='6',height=2,width=8,fg='black',bg='#3EB489',border=0,activebackground='red',anchor='center',font=("arial",8,"bold"),command=lambda:show("6")).place(x=320,y=315)
# third buttons line
btn11 = Button(f1,text='(',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center',font=("arial",8,"bold"),command=lambda:show("(")).place(x=40,y=360)
btn12 = Button(f1,text=')',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center',font=("arial",8,"bold"),command=lambda:show(")")).place(x=110,y=360)
btn13 = Button(f1,text='7',height=2,width=8,fg='black',bg='#3EB489',border=0,activebackground='red',anchor='center',font=("arial",8,"bold"),command=lambda:show("7")).place(x=180,y=360)
btn14 = Button(f1,text='8',height=2,width=8,fg='black',bg='#3EB489',border=0,activebackground='red',anchor='center',font=("arial",8,"bold"),command=lambda:show("8")).place(x=250,y=360)
btn18 = Button(f1,text='9',height=2,width=8,fg='black',bg='#3EB489',border=0,activebackground='red',anchor='center',font=("arial",8,"bold"),command=lambda:show("9")).place(x=320,y=360)
# fourth buttons line
btn16 = Button(f1,text='!',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center',font=("arial",8,"bold"),command=lambda:fact_2()).place(x=40,y=405)
btn17 = Button(f1,text='sqrt',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center',font=("arial",8,"bold"),command=lambda:sqrt_2()).place(x=110,y=405)
btn18 = Button(f1,text='0',height=2,width=8,fg='black',bg='#3EB489',border=0,activebackground='red',anchor='center',font=("arial",8,"bold"),command=lambda:show("0")).place(x=180,y=405)
btn19 = Button(f1,text='.',height=2,width=8,fg='black',bg='#3EB489',border=0,activebackground='red',anchor='center',font=("arial",8,"bold"),command=lambda:show(".")).place(x=250,y=405)
btn20 = Button(f1,text='=',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center',font=("arial",8,"bold"),command=lambda:calculate()).place(x=320,y=405)
# fifth buttons line
btn21 = Button(f1,text='^',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center',font=("arial",8,"bold"),command=lambda:show("^")).place(x=40,y=450)
btn22 = Button(f1,text='log',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center',font=("arial",8,"bold"),command=lambda:log_2()).place(x=110,y=450)
btn23 = Button(f1,text='ln',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center',font=("arial",8,"bold"),command=lambda:ln_2()).place(x=180,y=450)
btn24 = Button(f1,text='exp',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center',font=("arial",8,"bold"),command=lambda:exp_2()).place(x=250,y=450)
btn25 = Button(f1,text='c',height=2,width=8,fg='black',bg='#3697f5',border=0,activebackground='red',anchor='center',font=("arial",8,"bold"),command=lambda:clear()).place(x=320,y=450)
# six(th) buttons line
btn26 = Button(f1,text='%',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center',font=("arial",8,"bold"),command=lambda:show("%")).place(x=40,y=495)
btn27 = Button(f1,text='tan',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center',font=("arial",8,"bold"),command=lambda:tan_2()).place(x=110,y=495)
btn28 = Button(f1,text='cos',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center',font=("arial",8,"bold"),command=lambda:cos_2()).place(x=180,y=495)
btn29 = Button(f1,text='sin',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center',font=("arial",8,"bold"),command=lambda:sin_2()).place(x=250,y=495) 
btn30 = Button(f1,text='DEL',height=2,width=8,fg='black',bg='#3697f5',border=0,activebackground='red',anchor='center',font=("arial",8,"bold"),command=lambda:dels()).place(x=320,y=495)
# -----------------------------
# sc = Scrollbar(f6,orient=HORIZONTAL).pack(side=BOTTOM,fill=X)
l = Label(f6,fg="black",bg='#F8D004',anchor=None,font=("arial",22,"bold"),width=100,height=10,text="welcome to my desktop application , i'm bouzid almost 19 years old ,\nthis text was written in 17/04/2022 to present my little program .         \nthis app was written using python language and tkinter library         \nand take a little help , i will continue my dream as software                \ndevelopper , and that's it !!                                                                      ").place(x=-400,y=20)
# frame of hashing : ----------------------------------------------------------------------------------------------------------------------------------
hash_space = Label(f2,width=130,height=2,bg="white",fg='black',font=("arial",9,"bold"))
hash_space.place(x=30,y=190)
hash_space.config()

# ------------

# -------
btnc1 =  Button(f2,text='CLEAR',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='#3697f5',activeforeground="white",anchor='center',font=("arial",12,"bold"),command=lambda:clear_s()).place(x=650,y=30)
btnc2 =  Button(f2,text='Sha1\n40 bytes',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='#3697f5',activeforeground="white",anchor='center',font=("arial",12,"bold"),command=lambda:sha_1()).place(x=30,y=110)
btnc3 =  Button(f2,text='Sha224\n224 bytes',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='#3697f5',activeforeground="white",anchor='center',font=("arial",12,"bold"),command=lambda:sha_224()).place(x=131,y=110)
btnc4 =  Button(f2,text='Sha256\n256 bytes',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='#3697f5',activeforeground="white",anchor='center',font=("arial",12,"bold"),command=lambda:sha_256()).place(x=233,y=110)
btnc5 =  Button(f2,text='Sha384\n384 bytes',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='#3697f5',activeforeground="white",anchor='center',font=("arial",12,"bold"),command=lambda:sha_384()).place(x=335,y=110)
btnc6 =  Button(f2,text='Sha512\n512 bytes',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='#3697f5',activeforeground="white",anchor='center',font=("arial",12,"bold"),command=lambda:sha_512()).place(x=436,y=110)
btnc7 =  Button(f2,text='Md5\n32 bytes',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='#3697f5',activeforeground="white",anchor='center',font=("arial",12,"bold"),command=lambda:MD_5()).place(x=537,y=110)
btnc8 =  Button(f2,text='Copy',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='#3697f5',activeforeground="white",anchor='center',font=("arial",12,"bold"),command=lambda:print()).place(x=860,y=110)
btnc8 =  Button(f2,text='Run',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='#3697f5',activeforeground="white",anchor='center',font=("arial",12,"bold"),command=lambda:run_my_code()).place(x=860,y=110)

# code_result1= Label(f2,height=6,width=30,bg="white",fg='black',font=("arial",9,"bold"))
# code_result1.place(x=200,y=400)
# code_result1.config()
# 
# turtle arts coands commands functions :
def turtle_1():
    try :
        turtle.clear()
    except :
        pass
    turtle.bgcolor("black")
    turtle.title("bouzid")
    turtle.shape(name="triangle")
    t=Turtle()
    list_of_colors = ["red","yellow","green","blue"]
    for i in range(160):
        t.color("black",list_of_colors[i%4])
        t.left(125)
        t.begin_fill()
        t.circle(20)
        t.end_fill()
        t.speed(0)
        t.forward(5*i)
    turtle.done()
def turtle_2():
    try :
        turtle.clear()
    except :
        pass
    turtle.bgcolor("black")
    t=Turtle()
    for l in range(35):
        t.speed(0)
        t.color("yellow","yellow")
        t.begin_fill()
        t.color("yellow")
        t.right(90)
        t.forward(20+20*l)
        for j in range(7):
            t.color("yellow")
            t.right(90)
            t.forward(20)
        t.forward(20)
        t.rt(0)
        t.forward(20)
        t.rt(90)
        t.end_fill()
    turtle.done()
def turtle_3():
    try :
        turtle.clear()
    except :
        pass
    t=Turtle()
    turtle.bgcolor("black")
    t.speed(0)
    t.color("yellow")
    t.goto(-10,0)
    for i in range(1100):
        if i>300 and i<500 :
            t.color("orange")
        elif i>499 and i<650:
            t.color("red")
        elif i>649 and i<800:
            t.color("green")
        elif i>799:
            t.color("blue")
        t.forward(0.1*i)
        t.right(60+90*i)
    turtle.done()
def turtle_4():
    try :
        turtle.clear()
    except :
        pass
    t=Turtle()
    turtle.bgcolor("black")
    t.width(3)
    t.speed(0)
    # t.tracer(10)
    h=0
    n=50
    for i in range(150):
        c=colorsys.hsv_to_rgb(h,1,0.8)
        h+=1/n
        t.pencolor(c)
        t.circle(i,90)
        t.fd(i)
        t.rt(270)
        t.circle(i,270)
        t.fd(i)
        t.rt(180)    
    turtle.done()
def turtle_5():
    try :
        turtle.clear()
    except :
        pass
    t=Turtle()
    turtle.bgcolor("black")
    t.speed(0)
    for i in range(200):
        fg = colorsys.hsv_to_rgb(uniform(0,1),uniform(0,1),uniform(0,1))
        t.circle(50)
        t.begin_fill()
        t.color(fg,fg)
        t.end_fill()
        t.fd(0)
    done()
# line one :
filename = StringVar()
art1 = Button(f0,text='Art1\n4 colors',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center',command=lambda:turtle_1()).place(x=25,y=270)
art2 = Button(f0,text='Art2\nwait to see',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center',command=lambda:turtle_2()).place(x=105,y=270)
art3 = Button(f0,text='Art3\nfolded paper',height=2,width=9,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center',command=lambda:turtle_3()).place(x=182,y=270)
art4 = Button(f0,text='Art4\nWonderful',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center',command=lambda:turtle_4()).place(x=265,y=270)
art5 = Button(f0,text='@art5',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center',command=lambda:turtle_5()).place(x=345,y=270)
art6 = Button(f0,text='choose file',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center',command= lambda:open_file()).place(x=425,y=270)
def open_file():
    global filename
    filename = fd.askopenfilename()
    print("the file is "+filename+"   !")
art7 = Button(f0,text='@art7',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center').place(x=505,y=270)
art8 = Button(f0,text='@art8',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center').place(x=585,y=270)
art9 = Button(f0,text='@art9',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center').place(x=665,y=270)
art10 = Button(f0,text='@art10',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center').place(x=745,y=270)
art11 = Button(f0,text='@art11',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center').place(x=825,y=270)
art12 = Button(f0,text='@art12',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center').place(x=905,y=270)
# second line :
art13 = Button(f0,text='@art13',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center').place(x=25,y=325)
art14 = Button(f0,text='@art14',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center').place(x=105,y=325)
art15 = Button(f0,text='@art15',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center').place(x=185,y=325)
art16 = Button(f0,text='@art16',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center').place(x=265,y=325)
art17 = Button(f0,text='@art17',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center').place(x=345,y=325)
art18 = Button(f0,text='@art18',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center').place(x=425,y=325)
art19 = Button(f0,text='@art19',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center').place(x=505,y=325)
art20 = Button(f0,text='@art20',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center').place(x=585,y=325)
art21 = Button(f0,text='@art21',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center').place(x=665,y=325)
art22 = Button(f0,text='@art22',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center').place(x=745,y=325)
art23 = Button(f0,text='@art23',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center').place(x=825,y=325)
art24 = Button(f0,text='@art24',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center').place(x=905,y=325)
# third line :
art25 = Button(f0,text='@art25',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center').place(x=25,y=380)
art26 = Button(f0,text='@art26',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center').place(x=105,y=380)
art27 = Button(f0,text='@art27',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center').place(x=185,y=380)
art28 = Button(f0,text='@art28',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center').place(x=265,y=380)
art29 = Button(f0,text='@art29',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center').place(x=345,y=380)
art30 = Button(f0,text='@art30',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center').place(x=425,y=380)
art31 = Button(f0,text='@art31',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center').place(x=505,y=380)
art32 = Button(f0,text='@art32',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center').place(x=585,y=380)
art33 = Button(f0,text='@art33',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center').place(x=665,y=380)
art34 = Button(f0,text='@art34',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center').place(x=745,y=380)
art35 = Button(f0,text='@art35',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center').place(x=825,y=380)
art36 = Button(f0,text='@art36',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',anchor='center').place(x=905,y=380)

# hardware info frame :
def hardware_info ():
    try :
        k.destroy()
    except :
        pass
    def get_size(bytes, suffix="B"):
        """
        Scale bytes to its proper format
        e.g:
            1253656 => '1.20MB'
            1253656678 => '1.17GB'
        """
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f}{unit}{suffix}"
            bytes /= factor
    uname = platform.uname()
    sys_frame = Frame(f7,width=433,height=146,bg='#F8D004').place(x=50,y=20)
    k = Label(f7,text=50*" "+" SYSTEM INFO "+43*" ",fg='black',bg='#F8D004',border=5,anchor='center',font=("arial",8,"bold")).place(x=50,y=20)
    k = Label(f7,text=f"System : {uname.system}",fg='black',bg='#F8D004',border=5,anchor='center',font=("arial",8,"bold")).place(x=50,y=40)
    k = Label(f7,text=f"Node Name : {uname.node}",fg='black',bg='#F8D004',border=5,anchor='center',font=("arial",8,"bold")).place(x=50,y=60)
    k = Label(f7,text=f"Release : {uname.release}",fg='black',bg='#F8D004',border=5,anchor='center',font=("arial",8,"bold")).place(x=50,y=80)
    k = Label(f7,text=f"Version : {uname.version}",fg='black',bg='#F8D004',border=5,anchor='center',font=("arial",8,"bold")).place(x=50,y=100)
    k = Label(f7,text=f"Machine : {uname.machine}",fg='black',bg='#F8D004',border=5,anchor='center',font=("arial",8,"bold")).place(x=50,y=120)
    k = Label(f7,text=f"Processor : {uname.processor}",fg='black',bg='#F8D004',border=5,anchor='center',font=("arial",8,"bold")).place(x=50,y=140)
    cpu_frame = Frame(f7,width=430,height=186,bg='#F8D004').place(x=50,y=180)
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    k = Label(f7,text=50*" "+" BOOT & CPU INFO "+40*" ",fg='black',bg='#F8D004',border=5,anchor='center',font=("arial",8,"bold")).place(x=50,y=180)
    k = Label(f7,text=f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}",fg='black',bg='#F8D004',border=5,anchor='center',font=("arial",8,"bold")).place(x=50,y=200)
    k = Label(f7,text="Total cores : "+str(psutil.cpu_count(logical=True))+" cores",fg='black',bg='#F8D004',border=5,anchor='center',font=("arial",8,"bold")).place(x=50,y=200)
    cpufreq = psutil.cpu_freq()
    k = Label(f7,text=f"Max Frequency : {cpufreq.max:.2f} Mhz",fg='black',bg='#F8D004',border=5,anchor='center',font=("arial",8,"bold")).place(x=50,y=200)
    k = Label(f7,text=f"Min Frequency : {cpufreq.min:.2f} Mhz",fg='black',bg='#F8D004',border=5,anchor='center',font=("arial",8,"bold")).place(x=50,y=220)
    k = Label(f7,text=f"Current Frequency : {cpufreq.current:.2f} Mhz",fg='black',bg='#F8D004',border=5,anchor='center',font=("arial",8,"bold")).place(x=50,y=240)
    # do not forget to change values (i) and if conditions
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        if i < 4:
            k = Label(f7,text=f"Core {i} : {percentage}%",fg='black',bg='#F8D004',border=5,anchor='center',font=("arial",8,"bold")).place(x=50,y=260+20*i)
        if 3 < i < 8 :
            k = Label(f7,text=f"Core {i} : {percentage}%",fg='black',bg='#F8D004',border=5,anchor='center',font=("arial",8,"bold")).place(x=150,y=260+20*i)
        if 7 < i < 12 :
            k = Label(f7,text=f"Core {i} : {percentage}%",fg='black',bg='#F8D004',border=5,anchor='center',font=("arial",8,"bold")).place(x=250,y=260+20*i)
        if 11 < i < 16 :
            k = Label(f7,text=f"Core {i} : {percentage}%",fg='black',bg='#F8D004',border=5,anchor='center',font=("arial",8,"bold")).place(x=350,y=260+20*i)
    k = Label(f7,text=f"Total CPU Usage: {psutil.cpu_percent()}%",fg='black',bg='#F8D004',border=5,anchor='center',font=("arial",8,"bold")).place(x=50,y=280+60)
    svmem = psutil.virtual_memory()
    memory_frame = Frame(f7,width=430,height=180,bg='#F8D004').place(x=50,y=380)
    k = Label(f7,text=40*" "+" SYSTEM MEMORY & DISK"+40*" ",fg='black',bg='#F8D004',border=5,anchor='center',font=("arial",8,"bold")).place(x=50,y=380)
    k = Label(f7,text=f"Total memory (RAM): {get_size(svmem.total)}",fg='black',bg='#F8D004',border=5,anchor='center',font=("arial",8,"bold")).place(x=50,y=400)
    k = Label(f7,text=f"Available: {get_size(svmem.available)}",fg='black',bg='#F8D004',border=5,anchor='center',font=("arial",8,"bold")).place(x=50,y=420)
    k = Label(f7,text=f"Used: {get_size(svmem.used)}",fg='black',bg='#F8D004',border=5,anchor='center',font=("arial",8,"bold")).place(x=50,y=440)
    k = Label(f7,text=f"Percentage: {svmem.percent}%",fg='black',bg='#F8D004',border=5,anchor='center',font=("arial",8,"bold")).place(x=50,y=460)
    # disk space :
    partitions = psutil.disk_partitions()
    ilk = 0
    for partition in partitions:
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            # this can be catched due to the disk that
            # isn't ready
            continue
        if 0 <= ilk < 1 :
            k = Label(f7,text=f"=== Device: {partition.device} ===",fg='black',bg='#F8D004',anchor='center',font=("arial",8,"bold")).place(x=50,y=480)
            k = Label(f7,text=f"  Total Size: {get_size(partition_usage.total)}",fg='black',bg='#F8D004',anchor='center',font=("arial",8,"bold")).place(x=50,y=500)
            k = Label(f7,text=f"  Used: {get_size(partition_usage.used)}",fg='black',bg='#F8D004',anchor='center',font=("arial",8,"bold")).place(x=50,y=520)
            k = Label(f7,text=f"  Free: {get_size(partition_usage.free)}",fg='black',bg='#F8D004',anchor='center',font=("arial",8,"bold")).place(x=50,y=540)
        if 1 <= ilk < 2 :
            k = Label(f7,text=f" ========== Device: {partition.device} ====================",fg='black',bg='#F8D004',anchor='center',font=("arial",8,"bold")).place(x=160,y=480)
            k = Label(f7,text=f"  Total Size: {get_size(partition_usage.total)}",fg='black',bg='#F8D004',anchor='center',font=("arial",8,"bold")).place(x=160,y=500)
            k = Label(f7,text=f"  Used: {get_size(partition_usage.used)}",fg='black',bg='#F8D004',anchor='center',font=("arial",8,"bold")).place(x=160,y=520)
            k = Label(f7,text=f"  Free: {get_size(partition_usage.free)}",fg='black',bg='#F8D004',anchor='center',font=("arial",8,"bold")).place(x=160,y=540)
        if 2 <= ilk < 3 :
            k = Label(f7,text=f" ========== Device: {partition.device} ====================",fg='black',bg='#F8D004',anchor='center',font=("arial",8,"bold")).place(x=270,y=480)
            k = Label(f7,text=f"  Total Size: {get_size(partition_usage.total)}",fg='black',bg='#F8D004',anchor='center',font=("arial",8,"bold")).place(x=270,y=500)
            k = Label(f7,text=f"  Used: {get_size(partition_usage.used)}",fg='black',bg='#F8D004',anchor='center',font=("arial",8,"bold")).place(x=270,y=520)
            k = Label(f7,text=f"  Free: {get_size(partition_usage.free)}",fg='black',bg='#F8D004',anchor='center',font=("arial",8,"bold")).place(x=270,y=540)
        if 3 <= ilk < 4 :
            k = Label(f7,text=f" ========== Device: {partition.device} =====================",fg='black',bg='#F8D004',anchor='center',font=("arial",8,"bold")).place(x=380,y=480)
            k = Label(f7,text=f"  Total Size: {get_size(partition_usage.total)}",fg='black',bg='#F8D004',anchor='center',font=("arial",8,"bold")).place(x=380,y=500)
            k = Label(f7,text=f"  Used: {get_size(partition_usage.used)}",fg='black',bg='#F8D004',anchor='center',font=("arial",8,"bold")).place(x=380,y=520)
            k = Label(f7,text=f"  Free: {get_size(partition_usage.free)}",fg='black',bg='#F8D004',anchor='center',font=("arial",8,"bold")).place(x=380,y=540)
        ilk+=1
    disk_frame = Frame(f7,width=430,height=480,bg='#F8D004').place(x=500,y=20)
    if_addrs = psutil.net_if_addrs()
    lk = 0
    k = Label(f7,text=50*" "+"NETWORK INFO"+40*" ",fg='black',bg='#F8D004',anchor='center',font=("arial",8,"bold")).place(x=500,y=20)
    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            k = Label(f7,text=f" ============ Interface: {interface_name} ====================",fg='black',bg='#F8D004',anchor='center',font=("arial",8,"bold")).place(x=500,y=40+lk)
            if str(address.family) == 'AddressFamily.AF_INET':
                k = Label(f7,text=f"  IP Address: {address.address}",fg='black',bg='#F8D004',anchor='center',font=("arial",8,"bold")).place(x=500,y=60+lk)
                k = Label(f7,text=f"  Netmask: {address.netmask}",fg='black',bg='#F8D004',anchor='center',font=("arial",8,"bold")).place(x=500,y=80+lk)
                k = Label(f7,text=f"  Broadcast IP: {address.broadcast}",fg='black',bg='#F8D004',anchor='center',font=("arial",8,"bold")).place(x=500,y=100+lk)
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                k = Label(f7,text=f"  MAC Address: {address.address}",fg='black',bg='#F8D004',anchor='center',font=("arial",8,"bold")).place(x=500,y=120+lk)
                k = Label(f7,text=f"  Netmask: {address.netmask}",fg='black',bg='#F8D004',anchor='center',font=("arial",8,"bold")).place(x=500,y=140+lk)
                k = Label(f7,text=f"  Broadcast MAC: {address.broadcast}",fg='black',bg='#F8D004',anchor='center',font=("arial",8,"bold")).place(x=500,y=160+lk)
        lk+=80
hardware_info()
refresh_btn = Button(f7,text='refresh',height=2,width=8,fg='black',bg='#F8D004',border=0,activebackground='red',activeforeground="white",anchor='center',font=("arial",12,"bold"),command=lambda:hardware_info()).place(x=845,y=514)

def start():
    bar = ttk.Progressbar(f3,orient=HORIZONTAL,length=300)
    bar.pack()
    tasks = 100
    x = 0
    while (x<tasks):
        time.sleep(0.01)
        bar['value']+=1
        x+=1
        win.update_idletasks()
    bar.destroy()
button = Button(f3,text="download",command=start).pack()        
win.mainloop()