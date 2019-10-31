from tkinter import *

root = Tk()
entradatxt = StringVar()
operador = '' #Vai armazenzar os números e operações inseridos

#Entrada dos números e operações
def btEntrada(num):
    global operador
    operador += str(num)
    textBox.insert(INSERT, num)

#Função do botão igual(=)
def btIgual(x):
    global operador
    if x.find("+"): #Se for encontrado no campo de texto a operação '+'
        soma = str(eval(operador)) #então será feito a soma
        textBox.delete("1.0", END)
        textBox.insert(INSERT, soma)
        operador = ''
        operador = soma
    elif x.find("-") :
        sub = str(eval(operador))
        textBox.delete("1.0", END)
        textBox.insert(INSERT, sub)
        operador = ''
        operador = sub
    elif x.find("*"):
        mul = str(eval(operador))
        textBox.delete("1.0", END)
        textBox.insert(INSERT, mul)
        operador = ''
        operador = mul
    elif x.find("/"):
        div = str(eval(operador))
        textBox.delete("1.0", END)
        textBox.insert(INSERT, div)
        operador = ''
        operador = div
        
#Função do botão C(clear)
def btClear():
    global operador
    operador = ''
    textBox.delete("1.0", END)

#Botões e campo de texto
textBox = Text(root, height=4, width=10, font=(5))
textBox.pack(side=TOP, fill=X)
bt1 = Button(root, width=5, text="1", font=(5), command=lambda: btEntrada(1))
bt2 = Button(root, width=5, text="2", font=(5), command=lambda: btEntrada(2))
bt3 = Button(root, width=5, text="3", font=(5), command=lambda: btEntrada(3))
bt4 = Button(root, width=5, text="4", font=(5), command=lambda: btEntrada(4))
bt5 = Button(root, width=5, text="5", font=(5), command=lambda: btEntrada(5))
bt6 = Button(root, width=5, text="6", font=(5), command=lambda: btEntrada(6))
bt7 = Button(root, width=5, text="7", font=(5), command=lambda: btEntrada(7))
bt8 = Button(root, width=5, text="8", font=(5), command=lambda: btEntrada(8))
bt9 = Button(root, width=5, text="9", font=(5), command=lambda: btEntrada(9))
bt0 = Button(root, width=5, text="0", font=(5), command=lambda: btEntrada(0))
bt_clear = Button(root, width=5,font=(5), text="C", bg="orange", command=btClear) #OK
bt_soma = Button(root, width=5, font=(5), text="+", bg="green", command=lambda: btEntrada("+"))
bt_sub = Button(root, width=5, font=(5),text="-", bg="green", command=lambda: btEntrada("-"))
bt_div = Button(root, width=5, font=(5),text="/", bg="green", command=lambda: btEntrada("/"))
bt_mult = Button(root, width=5, font=(5),text="*", bg="green", command=lambda: btEntrada("*"))
bt_igual = Button(root, width=5, font=(5),text="=", bg="green", foreground="white", command=lambda: btIgual(operador))

#Posição dos botões
bt_clear.place(x=0, y=90)
bt_igual.place(x=120, y=250)
bt_soma.place(x=180, y=250)
bt_sub.place(x=180, y=210)
bt_mult.place(x=180, y=170)
bt_div.place(x=180, y=130)

bt7.place(x=0, y=130)
bt8.place(x=60, y=130)
bt9.place(x=120, y=130)

bt4.place(x=0, y=170)
bt5.place(x=60, y=170)
bt6.place(x=120, y=170)

bt1.place(x=0, y=210)
bt2.place(x=60, y=210)
bt3.place(x=120, y=210)

bt0.place(x=60, y=250)

root['bg'] = "black"
root.geometry("250x300+100+100")
root.title("Calculadora")
root.mainloop()
