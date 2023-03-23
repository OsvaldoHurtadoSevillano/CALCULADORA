from tkinter import*
from PIL import ImageTk,Image
root= Tk()


number1=StringVar()
number2=StringVar()


def resultado():
    global operador
    try:
        opera=str(eval(operador))
        input_text.set(opera)
    except:
        input_text.set("ERROR")
    operador = ""


def result(num):
    global operador
    operador=operador+str(num)
    input_text.set(operador)

def resultado():
    global operador
    try:
        opera=str(eval(operador))
        input_text.set(opera)
    except:
        input_text.set("ERROR")
    operador=""
 
ventanaprincipal=Tk()
ventanaprincipal.title("CALCULADORA")
ventanaprincipal.geometry("392x600")

input_text=StringVar()
operador=""



numero1=Label(ventanaprincipal,text="NUMERO 1:",
             font=("roboto",15)).grid(row=4,column=1,padx=30,pady=30)
num1=Entry(ventanaprincipal,font=("roboto",15),textvariable=number1).grid(row=4,column=2,padx=30,pady=15)


numero2=Label(ventanaprincipal,text="NUMERO 2:",
                 font=("roboto",15)).grid(row=6,column=1,padx=15,pady=10)
num2=Entry(ventanaprincipal,
                  font=("roboto",15),textvariable=number2).grid(row=6,column=2,padx=30,pady=15)

Result=Label(ventanaprincipal,text="RESULTADO:",
                 font=("roboto",15)).grid(row=8,column=1,padx=15,pady=10)
textresult=Entry(ventanaprincipal,
                  font=("roboto",15),textvariable=operador).grid(row=8,column=2,padx=30,pady=15)

Button(ventanaprincipal,text="SUMA",bg=("gray77"),width=11,height=3,command=result("+")).place(
    x=17,y=300)

Button(ventanaprincipal,text="RESTA",bg=("gray77"),width=11,height=3,command=result("-")).place(
    x=107,y=300)

Button(ventanaprincipal,text="MULT",bg=("gray77"),width=11,height=3,command=result("*")).place(
    x=197,y=360)

Button(ventanaprincipal,text="DIV",bg=("gray77"),width=11,height=3,command=lambda:result("/")).place(
    x=197,y=300)

Button(ventanaprincipal,text="=",bg=("gray77"),width=11,height=3,command=lambda:result("=")).place(
    x=17,y=360)

Button(ventanaprincipal,text="C",bg=("gray77"),width=11,height=3).place(x=107,y=360)


root.mainloop()