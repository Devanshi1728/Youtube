from tkinter import *
import math
import parser
import tkinter.messagebox
root=Tk()
root.title("Calculator")
tinput=StringVar()
operator = ""
class Calc:
    def __init__(self,root):
        self.f=Frame(root, height=600, width=600, bg="black")
       
        self.f.grid()
        
        def buttonClick(numbers):
            global operator
            operator = operator + str(numbers)
            tinput.set(operator)

        def buttonEquals():
            global operator
            sumup=str(eval(operator))
            tinput.set(sumup)
            operator=""
            
        def buttonclear():
            global operator
            operator=''
            tinput.set("0")

        def standard():
            root.resizable(width=False, height=False)
            root.geometry("410x315+0+0")

        def scicalc():
            root.resizable(width=False, height=False)
            root.geometry("860x315+0+0")

        def cos():
            global a
            a=float(tinput.get())
            tinput.set(math.cos(a))

        def sin():
            global a
            a=int(tinput.get())
            tinput.set(math.sin(a))

        def cosh():
            global a
            a=int(tinput.get())
            tinput.set(math.cosh(a))

        def tan():
            global a
            a=int(tinput.get())
            tinput.set(math.tan(a))

        def factorial():
            global a
            a=int(tinput.get())
            tinput.set(math.factorial(a))

        def tanh():
            global a
            a=int(tinput.get())
            tinput.set(math.tanh(a))
            
        def ceil():
            global a
            a=float(tinput.get())
            tinput.set(math.ceil(a))

        def trunc():
            global a
            a=int(tinput.get())
            tinput.set(math.trunc(a))

        def acosh():
            global a
            a=int(tinput.get())
            tinput.set(math.acosh(a))

        def log():
            global a
            a=int(tinput.get())
            tinput.set(math.log(a))

        def log2():
            global a
            a=int(tinput.get())
            tinput.set(math.log2(a))

        def exp():
            global a
            a=int(tinput.get())
            tinput.set(math.exp(a))

        def expm1():
            global a
            a=int(tinput.get())
            tinput.set(math.expm1(a))

        def floor():
            global a
            a=float(tinput.get())
            tinput.set(math.floor(a))

        def radians():
            global a
            a=int(tinput.get())
            tinput.set(math.radians(a))

        def log10():
            global a
            a=int(tinput.get())
            tinput.set(math.log10(a))

        def degrees():
            global a
            a=int(tinput.get())
            tinput.set(math.degrees(a))

        def fabs():
            global a
            a=int(tinput.get())
            tinput.set(math.fabs(a))
            
        def asin():
            global a
            a=float(tinput.get())
            tinput.set(math.asin(a))

        def asinh():
            global a
            a=float(tinput.get())
            tinput.set(math.asinh(a))

        def sqrt():
            global a
            a=int(tinput.get())
            tinput.set(math.sqrt(a))

        def acos():
            global a
            a=float(tinput.get())
            tinput.set(math.acos(a))

        def pow():
            global a
            a=int(tinput.get())
            b=int(tinput.get())
            tinput.set(math.pow(a,b))


        self.menubar=Menu(root) 
        root.config(menu=self.menubar) 
        
        self.filemenu=Menu(root,tearoff=0) 
        self.filemenu.add_command(label="Standard", command=standard) 
        self.filemenu.add_separator() 
        self.filemenu.add_command(label="Scientific", command=scicalc)

        self.menubar.add_cascade(label='File', menu=self.filemenu) 
        
        self.t=Entry(self.f, font=('Rockwell Condensed Bold',20),  textvariable=tinput, justify='right', fg='white', bg='grey', bd=25, width=24)
        self.t.grid(columnspan=4)
        self.t.insert(0,"0")


 ############################################################################################################################
    
        self.ce=Button(self.f, text=chr(67) + chr(69), width=10, height=1, bg='grey', fg='white',  command = buttonclear)
        self.ce.grid(row=1, column=0, padx=5, pady=10)

        self.c=Button(self.f, text='√', width=10, height=1, bg='grey', fg='white', command = sqrt)
        self.c.grid(row=1, column=1, padx=5, pady=10)

        self.sqrt=Button(self.f, text= chr(94), width=10, height=1, bg='grey', fg='white',  command = lambda:buttonClick("**"))                                                                                                                     
        self.sqrt.grid(row=1, column=2, padx=5, pady=10)
        
        self.mod=Button(self.f, text='%', width=10, height=1, bg='grey', fg='white', command = lambda:buttonClick("%"))
        self.mod.grid(row=1, column=3, padx=5, pady=10)

        self.mod=Button(self.f, text='π', width=10, height=1, bg='grey', fg='white', command=lambda:buttonClick(math.pi))
        self.mod.grid(row=1, column=4, padx=5, pady=10)

        self.mod=Button(self.f, text='cos', width=10, height=1, bg='grey', fg='white', command = cos)
        self.mod.grid(row=1, column=5, padx=5, pady=10)

        self.mod=Button(self.f, text='tan', width=10, height=1, bg='grey', fg='white', command = tan)
        self.mod.grid(row=1, column=6, padx=5, pady=10)

        self.mod=Button(self.f, text='factorial', width=10, height=1, bg='grey', fg='white', command = factorial)
        self.mod.grid(row=1, column=7, padx=5, pady=10)

        self.mod=Button(self.f, text='^n', width=10, height=1, bg='grey', fg='white', command = pow)
        self.mod.grid(row=1, column=8, padx=5, pady=10)

    
#####################################################

        self.b7=Button(self.f, text='7', width=10, height=1, bg='grey', fg='white', command = lambda:buttonClick(7))
        self.b7.grid(row=2, column=0, padx=5, pady=10)

        self.b8=Button(self.f, text='8', width=10, height=1, bg='grey', fg='white',  command = lambda:buttonClick(8))
        self.b8.grid(row=2, column=1, padx=5, pady=10)

        self.b9=Button(self.f, text='9', width=10, height=1, bg='grey', fg='white',  command = lambda:buttonClick(9))
        self.b9.grid(row=2, column=2, padx=5, pady=10)

        self.badd=Button(self.f, text='+', width=10, height=1, bg='grey', fg='white', command = lambda:buttonClick("+"))
        self.badd.grid(row=2, column=3, padx=5, pady=10)
        
        self.badd=Button(self.f, text='2π', width=10, height=1, bg='grey', fg='white', command = lambda:buttonClick(math.pi*2))
        self.badd.grid(row=2, column=4, padx=5, pady=10)

        self.mod=Button(self.f, text='cosh', width=10, height=1, bg='grey', fg='white', command = cosh)
        self.mod.grid(row=2, column=5, padx=5, pady=10)

        self.mod=Button(self.f, text='tanh', width=10, height=1, bg='grey', fg='white', command = tanh)
        self.mod.grid(row=2, column=6, padx=5, pady=10)

        self.mod=Button(self.f, text='ceil', width=10, height=1, bg='grey', fg='white', command = ceil)
        self.mod.grid(row=2, column=7, padx=5, pady=10)

        self.mod=Button(self.f, text='trunc', width=10, height=1, bg='grey', fg='white', command = trunc)
        self.mod.grid(row=2, column=8, padx=5, pady=10)

        
############################################################

        
        self.b4=Button(self.f, text='4', width=10, height=1, bg='grey', fg='white', command = lambda:buttonClick(4))
        self.b4.grid(row=3, column=0, padx=5, pady=10)

        self.b5=Button(self.f, text='5', width=10, height=1, bg='grey', fg='white',  command = lambda:buttonClick(5))
        self.b5.grid(row=3, column=1, padx=5, pady=10)

        self.b6=Button(self.f, text='6', width=10, height=1, bg='grey', fg='white',  command = lambda:buttonClick(6))
        self.b6.grid(row=3, column=2, padx=5, pady=10)

        self.sub=Button(self.f, text='-', width=10, height=1, bg='grey', fg='white', command = lambda:buttonClick("-"))
        self.sub.grid(row=3, column=3, padx=5, pady=10)

        self.sub=Button(self.f, text='log', width=10, height=1, bg='grey', fg='white', command = log)
        self.sub.grid(row=3, column=4, padx=5, pady=10)

        self.mod=Button(self.f, text='acosh', width=10, height=1, bg='grey', fg='white', command = acosh)
        self.mod.grid(row=3, column=5, padx=5, pady=10)

        self.mod=Button(self.f, text='Exp', width=10, height=1, bg='grey', fg='white', command = exp)
        self.mod.grid(row=3, column=6, padx=5, pady=10)

        self.mod=Button(self.f, text='floor', width=10, height=1, bg='grey', fg='white', command = floor)
        self.mod.grid(row=3, column=7, padx=5, pady=10)

        self.mod=Button(self.f, text='radians', width=10, height=1, bg='grey', fg='white', command = radians)
        self.mod.grid(row=3, column=8, padx=5, pady=10)

 ############################################
        self.b1=Button(self.f, text='1', width=10, height=1, bg='grey', fg='white', command = lambda:buttonClick(1))
        self.b1.grid(row=4, column=0, padx=5, pady=10)

        self.b2=Button(self.f, text='2', width=10, height=1, bg='grey', fg='white',  command = lambda:buttonClick(2))
        self.b2.grid(row=4, column=1, padx=5, pady=10)

        self.b3=Button(self.f, text='3', width=10, height=1, bg='grey', fg='white',  command = lambda:buttonClick(3))
        self.b3.grid(row=4, column=2, padx=5, pady=10)

        self.mul=Button(self.f, text='*', width=10, height=1, bg='grey', fg='white', command = lambda:buttonClick("*"))
        self.mul.grid(row=4, column=3, padx=5, pady=10)
 
        self.sub=Button(self.f, text='log2', width=10, height=1, bg='grey', fg='white', command = log2)
        self.sub.grid(row=4, column=4, padx=5, pady=10)

        self.mod=Button(self.f, text='deg', width=10, height=1, bg='grey', fg='white', command = degrees)
        self.mod.grid(row=4, column=5, padx=5, pady=10)
        
        self.mod=Button(self.f, text='sin', width=10, height=1, bg='grey', fg='white', command = sin)
        self.mod.grid(row=4, column=6, padx=5, pady=10)
        
        self.mod=Button(self.f, text='e', width=10, height=1, bg='grey', fg='white', command = lambda:buttonClick(math.e))
        self.mod.grid(row=4, column=7, padx=5, pady=10)

        self.mod=Button(self.f, text='fabs', width=10, height=1, bg='grey', fg='white', command = fabs)
        self.mod.grid(row=4, column=8, padx=5, pady=10)

######################################

        self.dot=Button(self.f, text='.', width=10, height=1, bg='grey', fg='white', command = lambda:buttonClick("."))
        self.dot.grid(row=5, column=0, padx=5, pady=10)
        
        self.b0=Button(self.f, text='0', width=10, height=1, bg='grey', fg='white',  command = lambda:buttonClick(0))
        self.b0.grid(row=5, column=1, padx=5, pady=10)

        self.bequ=Button(self.f, text='=', width=10, height=1, bg='grey', fg='white', command = buttonEquals)
        self.bequ.grid(row=5, column=2, padx=5, pady=10)

        self.div=Button(self.f, text=chr(247), width=10, height=1, bg='grey', fg='white',  command =lambda:buttonClick("/"))
        self.div.grid(row=5, column=3, padx=5, pady=10)

        self.sub=Button(self.f, text='log10', width=10, height=1, bg='grey', fg='white', command = log10)
        self.sub.grid(row=5, column=4, padx=5, pady=10)

        self.sub=Button(self.f, text='e**x-1', width=10, height=1, bg='grey', fg='white', command = expm1)
        self.sub.grid(row=5, column=5, padx=5, pady=10)

        self.sub=Button(self.f, text='asin', width=10, height=1, bg='grey', fg='white', command = asin)
        self.sub.grid(row=5, column=6, padx=5, pady=10)

        self.sub=Button(self.f, text='asinh', width=10, height=1, bg='grey', fg='white', command=asinh)
        self.sub.grid(row=5, column=7, padx=5, pady=10)

        self.sub=Button(self.f, text='acos', width=10, height=1, bg='grey', fg='white', command=acos)
        self.sub.grid(row=5, column=8, padx=5, pady=10)
       

op=Calc(root)
root.mainloop()
