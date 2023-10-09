from tkinter import *
from tkinter import ttk

#cores
COR1 = "#242424"  #cinza escuro
COR2 = "#feffff"  #branco
COR3 = "#38576b"  #azul
COR4 = "#ECEFF1"  #cinzenta
COR5 = "#FFAB40" #laranja

janela = Tk() #criando a janela
janela.title("calculadora")
janela.geometry("239x306")
janela.config(bg=COR1)

#criando frames
frame_janela = Frame(janela, width=239, height=50, bg=COR3)
frame_janela.grid(row=0, column=0)

frame_janela_corpo = Frame(janela, width=239, height=268)
frame_janela_corpo.grid(row=1, column=0)


#criando labels
valor_texto = StringVar()

#variavel que armazena valores digitados
todos_valores = ''


#criando função
def entrar_valores(event):

    global todos_valores
    todos_valores = todos_valores + str(event)
    #passando valor para a tela
    valor_texto.set(todos_valores)


#função para calcular
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))


#limpa tela
def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")


app_label = Label(frame_janela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT,
                  anchor="e", justify=RIGHT, font=('Ivy 18'), bg=COR3, fg=COR2)
app_label.place(x=0, y=0)


#criando botões
b_1 = Button(frame_janela_corpo, command = lambda: limpar_tela(), text="C", width=11, height=2,
             bg=COR4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0) # x = vertical, y = horizontal
b_2 = Button(frame_janela_corpo, command = lambda: entrar_valores('%'), text="%", width=5, height=2,
             bg=COR4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=120, y=0)
b_3 = Button(frame_janela_corpo, command = lambda: entrar_valores('/'), text="/", width=5, height=2,
             bg=COR5, fg=COR2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=180, y=0)


b_4 = Button(frame_janela_corpo, command = lambda: entrar_valores('7'), text="7", width=5, height=2,
             bg=COR4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=51)
b_5 = Button(frame_janela_corpo, command = lambda: entrar_valores('8'), text="8", width=5, height=2,
             bg=COR4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=60, y=51)
b_6 = Button(frame_janela_corpo, command = lambda: entrar_valores('9'), text="9", width=5, height=2,
             bg=COR4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=120, y=51)
b_7 = Button(frame_janela_corpo, command = lambda: entrar_valores('*'), text="x", width=5, height=2,
             bg=COR5, fg=COR2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=180, y=51)


b_8 = Button(frame_janela_corpo, command = lambda: entrar_valores('4'), text="4", width=5, height=2,
             bg=COR4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=102)
b_9 = Button(frame_janela_corpo, command = lambda: entrar_valores('5'), text="5", width=5, height=2,
             bg=COR4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=60, y=102)
b_10 = Button(frame_janela_corpo, command = lambda: entrar_valores('6'), text="6", width=5,
              height=2, bg=COR4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=120, y=102)
b_11 = Button(frame_janela_corpo, command = lambda: entrar_valores('-'), text="-", width=5,
              height=2, bg=COR5, fg=COR2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=180, y=102)


b_12 = Button(frame_janela_corpo, command = lambda: entrar_valores('3'), text="3", width=5,
              height=2, bg=COR4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=153)
b_13 = Button(frame_janela_corpo, command = lambda: entrar_valores('2'), text="2", width=5,
              height=2, bg=COR4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=60, y=153)
b_14 = Button(frame_janela_corpo, command = lambda: entrar_valores('1'), text="1", width=5,
              height=2, bg=COR4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=120, y=153)
b_15 = Button(frame_janela_corpo, command = lambda: entrar_valores('+'), text="+", width=5,
              height=2, bg=COR5, fg=COR2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=180, y=153)


b_16 = Button(frame_janela_corpo, command = lambda: entrar_valores('0'), text="0", width=11,
              height=2, bg=COR4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=204)
b_17 = Button(frame_janela_corpo, command = lambda: entrar_valores('.'), text=".", width=5,
              height=2, bg=COR4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=120, y=204)
b_18 = Button(frame_janela_corpo, command = lambda: calcular(), text="=", width=5, height=2,
              bg=COR4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=180, y=204)


janela.mainloop() #executa o app