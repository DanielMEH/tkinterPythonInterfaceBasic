from  tkinter import  *
from  tkinter import  ttk
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
opciones =["Nequi", "Bancolombia", "Daviviena"]
valor_en_dolar_formateado = locale.currency(dataUser["id"]["saldo"], grouping=True)

cb1 = ttk.Combobox(win, values=opciones, width=10)
print(cb1.get())
cb1.grid(row=1, column=1, padx=5, pady=5)
win.geometry("500x500")

win.mainloop()

