from tkinter import *

from tkinter import ttk
import xlrd

# iportar usuario
import locale

locale.setlocale(locale.LC_MONETARY, "en_US.UTF-8")

win = Tk()

dataUser = {
    "id": {
        "nombre": "Juan Daniel",
        "apellido": "Perez",
        "cc":1005090349,
        "saldo": 1000000,
        "clave": 1234,
        "cuenta": "Ahorros",
        "fecha creacion": "12/12/2020",
        "fecha modificacion": "12/12/2020",
        "estado": "Activo",
        "tipo": "Natural",
        "email": " daniel@gmail.com",
        "telefono": 3003764571,
        "direccion": "Calle 12 # 12 - 12",
        "ciudad": "Bogota",
        "pais": "Colombia",
        "genero": "Masculino",
        "fecha nacimiento": "12/12/1990",
        "edad": 30,
        "estado civil": "Soltero",
        "profesion": "Estudiante",
        "nivel educativo": "Universitario",
        "ocupacion": "Estudiante",
        "empresa": "Universidad Nacional",
        "cargo": "Estudiante",
        "ingresos": 1000000,
        "egresos": 0,
       

    }
}
win.resizable(0, 0)
win.title("Cajero Automatico ")
content = Label(win, text="Bienvenido al Cajero Automatico", font=("Arial", 15), fg="blue",
     bg="yellow", padx=20, pady=20, bd=10, relief="groove", anchor="center")


span1 = Label(win, text="Ingrese su numero de cedula", font=("Arial", 10), )
span2 = Label(win, text="Ingrese su clave", font=("Arial", 10), )
btn = Button(win, text="Ingresar", bg="blue", fg="white", font=("Arial", 15),  anchor="center", cursor="hand2")
numeroCuenta = Entry(win, text="Ingrese su numero de cuenta", font=("Arial", 15), takefocus=True,)
clave = Entry(win, text="clave", font=("Arial", 15), show="*", 
              takefocus=True, validatecommand=(win.register(lambda P: P.isdigit()), '%P'))
salir = Button(win, text="Salir", bg="red", fg="white", font=("Arial", 15),  anchor="center", cursor="hand2")
welcome = Label(win, text="Welcome")
salir.pack(side="bottom", padx=5, pady=5, ipadx=5, ipady=5, )
salir.bind("<Button-1>", lambda event: win.destroy())
content.pack(ipadx=5, ipady=5)
span1.pack(ipadx=5, ipady=5,padx=5, pady=5)
numeroCuenta.pack(ipadx=5, ipady=5,padx=5, pady=5)
span2.pack(ipadx=5, ipady=5,padx=5, pady=5)
clave.pack(ipadx=5, ipady=5,padx=5, pady=5, )
btn.pack( padx=5, pady=5, anchor="center", ipadx=5, ipady=5,)
error = Label(win, text="Error los datos no son validos", font=("Arial", 10), fg="red")

win.geometry("400x400+700+250")

dataUser.keys()
id = dataUser["id"]["cc"]
claveAcceso = dataUser["id"]["clave"]
def validar():
    if numeroCuenta.get() == str(id) and clave.get() == str(claveAcceso):
        win.destroy()
        interfaceUsuario()
        
    else:
        error.pack( )

def interfaceUsuario(updatePrecio=0):
    
    if updatePrecio != 0:
       valor_en_dolar_formateado = locale.currency(updatePrecio["id"]["saldo"], grouping=True)
    
    else:
        valor_en_dolar_formateado = locale.currency(dataUser["id"]["saldo"], grouping=True)

    

    win2 = Tk()
    
    win2.resizable(0, 0)
    name = Label(win2, text="Nombre: " + dataUser["id"]["nombre"]+": " )
    datos_personales = Label(win2, text="Datos Personales", font=("Arial", 15), fg="blue",)
    saldo = Label(win2, text="Saldo: " + str(valor_en_dolar_formateado), fg="green" )
    cuenta = Label(win2, text="Cuenta: " + dataUser["id"]["cuenta"], )
    fechaCreacion = Label(win2, text="Fecha Creacion: " + dataUser["id"]["fecha creacion"], )
    fechaModificacion = Label(win2, text="Fecha Modificacion: " + dataUser["id"]["fecha modificacion"], )
    estado = Label(win2, text="Estado: " + dataUser["id"]["estado"], fg="green" )
    tipo = Label(win2, text="Tipo: " + dataUser["id"]["tipo"], anchor="w" )
    email = Label(win2, text="Email: " + dataUser["id"]["email"], )
    telefono = Label(win2, text="Telefono: " + str(dataUser["id"]["telefono"]), )
    direccion = Label(win2, text="Direccion: " + dataUser["id"]["direccion"], )
    ciudad = Label(win2, text="Ciudad: " + dataUser["id"]["ciudad"], )
    pais = Label(win2, text="Pais: " + dataUser["id"]["pais"], )
    genero = Label(win2, text="Genero: " + dataUser["id"]["genero"], )
    btnTransferir = Button(win2, text="Transferir", bg="#5C10E1", fg="white", font=("Arial", 15), cursor="hand2"  )
    btnSacarDinero = Button(win2, text="Sacar Dinero", bg="#FFC733", fg="white", font=("Arial", 15), cursor="hand2")
    btnDepositarDinero = Button(win2, text="Depositar Dinero", bg="#33AFFF", fg="white", font=("Arial", 15), cursor="hand2")
    btn_pagina_principal = Button(win2, text="PaginaPrinccipal", bg="red", fg="white", font=("Arial", 15), cursor="hand2")

    estado.grid(row=0, column=0)
    tipo.grid(row=3, column=0)
    email.grid(row=4, column=0)
    telefono.grid(row=5, column=0)
    direccion.grid(row=6, column=0)
    ciudad.grid(row=7, column=0)
    pais.grid(row=8, column=0)
    genero.grid(row=9, column=0)
    btnTransferir.grid(row=3, column=3)
    btnSacarDinero.grid(row=4, column=3)
    btnDepositarDinero.grid(row=5, column=3)
    btn_pagina_principal.grid(row=6, column=3)

    name.grid(row=1, column=0)
    datos_personales.grid(row=2, column=0)
    saldo.grid(row=1, column=3)
    win2.title("Bienvenido")
    name.config(font=("Arial", 15))
    saldo.config(font=("Arial"))
    win2.geometry("400x400+700+250")
    btnTransferir.bind("<Button-1>", lambda event: transferirDinero())
    btnDepositarDinero.bind("<Button-1>", lambda event: depositarDinero())
    btnSacarDinero.bind("<Button-1>", lambda event: sacarDinero())
    btn_pagina_principal.bind("<Button-1>", lambda event: paginaPrincipal())

    def paginaPrincipal():
        win2.destroy()
        interfaceUsuario()



    def depositarDinero():
        win3 = Tk()
        win3.resizable(0, 0)
        win3.title("Depositar Dinero")
        sacarInput = Entry(win3,  width=10)
        sacarInput.grid(row=2, column=1, padx=5, pady=5)
        sacarDepositar = Button(win3, text="Depositar", bg="#FFC733", fg="white", font=("Arial", 15), cursor="hand2")
        sacarDepositar.grid(row=3, column=1, padx=5, pady=5)
        sacarDepositar.bind("<Button-1>", lambda event: Depositar(sacarInput.get()))
        
        def Depositar(depositar):
            aumentar = float(dataUser["id"]["saldo"]) + float(depositar)
            updatePrecio = {"id": {"saldo": aumentar}}
            resultado = Label(win3, text="La solicitud fue exitosa", fg="red")
            resultado.grid(row=4, column=1)
            win2.destroy()
            interfaceUsuario(updatePrecio)
            win3.destroy()
        win3.geometry("200x200")
        win3.mainloop()

    def transferirDinero():
        win3 = Tk()
        win3.resizable(0, 0)
        opciones =["Nequi", "Bancolombia", "Daviviena"]
        cb1 = ttk.Combobox(win3, values=opciones, width=10)
        sacarInput = Entry(win3,  width=10)
        span1 = Label(win3, text="A que banco desea transferir")
        span2 = Label(win3, text="Cuanto desea transferir")
        numberCuenta= Entry(win3,  width=10)
        numero = Label(win3, text="Numero de Cuenta")
        sacar = Button(win3, text="Sacar", bg="#FFC733", fg="white", font=("Arial", 15), cursor="hand2")
        cb1.grid(row=1, column=1, padx=5, pady=5)
        sacarInput.grid(row=2, column=1, padx=5, pady=5)
        span1.grid(row=1, column=0, padx=5, pady=5)
        span2.grid(row=2, column=0, padx=5, pady=5)
        numberCuenta.grid(row=3, column=1, padx=5, pady=5)
        numero.grid(row=3, column=0, padx=5, pady=5)
        sacar.grid(row=4, column=1, padx=5, pady=5)
        sacar.bind("<Button-1>", lambda event: transferirUsuarrio(sacarInput.get()))
        def transferirUsuarrio(sacar):
           
           if float(sacar) > float(dataUser["id"]["saldo"]):
                resultado = Label(win3, text="No tienes saldo suficiente", fg="red")
                resultado.grid(row=4, column=1)
                
           else:
                saldo.grid(row=1, column=3)
                descontar = float(dataUser["id"]["saldo"]) - float(sacar)
                updatePrecio = {"id": {"saldo": descontar}}
                
                resultado = Label(win3, text="La solicitud fue exitosa", fg="green")
                resultado.grid(row=4, column=1)
                win2.destroy()
                interfaceUsuario(updatePrecio)
                win3.destroy()
                
        win3.title("Transferir Dinero")
        win3.geometry("500x500")
        win3.mainloop()

    def sacarDinero():
        win3 = Tk()
        win3.resizable(0, 0)
        win3.title("Sacar Dinero")
       
        sacarInput = Entry(win3,  width=10)
        sacar = Button(win3, text="Sacar", bg="#FFC733", fg="white", font=("Arial", 15), cursor="hand2")
        
        sacarInput.grid(row=2, column=1, padx=5, pady=5)
        sacar.grid(row=3, column=1, padx=5, pady=5)
        sacar.bind("<Button-1>", lambda event: updatesaldo(sacarInput.get()))
        def updatesaldo(sacar):
           
           if float(sacar) > float(dataUser["id"]["saldo"]):
                resultado = Label(win3, text="No tienes saldo suficiente", fg="red")
                resultado.grid(row=4, column=1)
                
           else:
                saldo.grid(row=1, column=3)
                descontar = float(dataUser["id"]["saldo"]) - float(sacar)
                updatePrecio = {"id": {"saldo": descontar}}
                resultado = Label(win3, text="La solicitud fue exitosa", fg="green")
                resultado.grid(row=4, column=1)
                win2.destroy()
                interfaceUsuario(updatePrecio)
                win3.destroy()
                destroyWin3()

        def destroyWin3():
            win3.destroy()
        win3.geometry("200x200")
        win3.mainloop()

    win2.mainloop()


btn.bind("<Button-1>", lambda event: validar())

win.mainloop()