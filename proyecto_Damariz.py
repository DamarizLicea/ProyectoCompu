"""
Proyecto Keikiz by Mayiz
Damariz Licea Carrisoza A01369045
Punto de venta, cotizador de órdenes para
un negocio de pastelería.
Despliega menú para venta regular de productos,
permite cotizar una orden varias veces para que
el cliente lo haga hasta estar contento.
Después permite que el usuario haga la orden
como tal de un pedido y le da opción de pagar.
En el ultimo punto, es un contador de dinero
segun el numero de monedas/billetes que el usuario ingrese.

"""
"""
LAS CORRECIONES SE ENCUENTRAN EN UN DOCUMENTO DE TEXTO EN MI GITHUB,
SE LLAMA "correciones_Damariz"
"""
"""
------------------funciones del programa-------------------
"""

    
import colorama
from colorama import Fore,Back,Style
colorama.init()

"""
Importación e inicialización de Colorama
Obtenido del sitio oficial de Python.
Código de inicialización y extras para uso
de sus funciones en: https://pypi.org/project/colorama/
Ese es mi elemento extra. Uso en líneas: 108, 149, 163, 164, 200, 204, 207, 209,
282, 284, 315, 317, 336, 339, 346, 349, 352, 354, 374, 375, 380, 381, 383, 384.
"""


def imprfor(lista_pan):
    
    """
    Crea el menú a partir de una matriz de 7x2
    Usa ciclos for, listas y funciones.
    Recibe: Lista que contiene los sabores de pan,
    con sus respectivos números de orden.
    Devuelve: No devuelve valor como tal,
    solo imprime el menú.
    """
    
    for linea in lista_pan:
        for columna in linea:
            print(columna, end = " ")
        print()

def impwhile(lista_relleno):
    
    """
    Crea o ordena el menú (de una matriz de 7 x 2)gracias a un ciclo while.
    Usa funciones, ciclos while, listas.
    Recibe: lista_relleno, lista en la que están los numeros de orden de
    cada sabor de relleno y los respectivos sabores de relleno.
    Devuelve: No devuelve un valor.
    """
    
    valor = 0
    i = 0
    while i<len(lista_relleno):
        j = 0
        while j<len(lista_relleno[0]):
            print(lista_relleno[i][j], end = " ")
            j = j + 1
        print()
        i = i + 1
        

def impwhile(listadeco):
    
    """"
    Misma acción que la funcion de arriba.
    Usa funciones, ciclos while, listas.
    Recibe: listadeco, lista en la que están las opciones de
    decoración y sus respectivos números de orden.
    Devuelve: No devuelve un valor.
    """
    
    valor = 0
    i = 0
    while i<len(listadeco):
        j = 0
        while j<len(listadeco[0]):
            print(listadeco[i][j],end = " ")
            j = j + 1
        print()
        i = i + 1


def menu1():
    
    """
    Aquí están las matrices que se usan en las primeras funciones del programa,
    también aquí ejecuto y englobo las primeras tres funciones,
    para poder imprimir el menú entero de una sola vez.
    Uso de: print, Colorama, listas, funciones.
    Recibe: No recibe argumentos, solo se manda a llamar y se ejecuta.
    Devuelve: No devuelve un valor.
    """
    
    print()
    print(Style.BRIGHT + Fore.MAGENTA + Back.WHITE + "Hola! Bienvenido a Keikiz, nuestro menú para ordenes de pasteles es éste:")
    print()
    
    lista_pan = [
        
        ['1','Red Velvet'],
        ['2','Zanahoria'],
        ['3','Gansito'],
        ['4','Chocolate Clásico'],
        ['5','Chai'],
        ['6','Vainilla'],
        ['7','Limón']
        
        ]
    imprfor(lista_pan)
    print()

    print("El menú de rellenos es éste:")
    lista_relleno = [
        
        ['1','Buttercream de Vainilla'],
        ['2','Crema de Queso'],
        ['3','Mermelada de frutos rojos'],
        ['4','Buttercream de chocolate'],
        ['5','Buttercream de PB'],
        ['6','Lemon Curd']
        
        ]
    impwhile(lista_relleno)
    print()

    print("Nuestro menú para decoraciones es este:")
    listadeco = [
        
        ['1','Fondant'],
        ['2','Chocolate'],
        ['3','Buttercream'],
        ['4','Moldeado']
        
        ]
    impwhile(listadeco)
    print(Style.RESET_ALL)
    print()

    
def menu2():
    
    """
    Aquí está el menú que ocupo en la parte de venta directa (menú de venta normal)
    Uso de: Colorama, print, funciones.
    Recibe: No recibe ningún argumento
    Devuelve: No devuelve ningún valor, solo ejecuta un print
    """
    
    print()
    print(Back.WHITE + Fore.CYAN + Style.BRIGHT + "Hola! Bienvenido a Keikiz, nuestro menú por rebanadas para hoy es éste: \n1)Tarta de nuez $40 \n2)Pastel de miel $60 \n3)Pastel de rollo $40 \n4)Pastel de Brownie $50 \n5)Cheesecake de pera $45 \n6)Pay de manzana $45")
    print(Style.RESET_ALL)
    print()


def venta_directa():
    
    """
    Despliega el menú para vender normalmente, da el precio del producto según el número
    del producto en el menú, y las porciones que pidió.
    El precio puede cambiar según la opción de pago.
    Uso de: Condicionales, input, Colorama, operadores, funciones.
    Recibe: No recibe ningún parámetro
    Devuelve: No devuelve ningún valor, solo ejecuta lo que lleva dentro
    """
    
    menu2()
    producto = int(input("¿Qué va a querer? (Indique el número del producto): "))
    if producto == 1:
        valor = 40
    if producto == 2:
        valor = 60
    if producto == 3:
        valor = 40
    if producto == 4:
        valor = 50
    if producto == 5 or producto == 6:
        valor = 45
    rebanadas = int(input("¿Cuantas rebanadas? "))
    cuenta = valor * rebanadas
    print(Back.WHITE + Fore.CYAN + Style.BRIGHT + "Su cuenta es de $", cuenta)
    print(Style.RESET_ALL)
    print()
    
    forma_de_pago = str(input("¿Su pago es en efectivo o tarjeta de crédito o tarjeta de débito? Si es efectivo, por favor escriba efectivo, si es tarjeta de crédito, por favor escriba credito, y si no es ninguna de las anteriores, escriba debito: "))
    if forma_de_pago == ("efectivo"):
        valorventa = cuenta
        print(Back.WHITE + Fore.CYAN + Style.BRIGHT + "Su cuenta final fue de $", valorventa)
        print("gracias, vuelva pronto")
    if forma_de_pago == "credito":
        valorventa = cuenta + (cuenta * 0.10)
        print(Back.WHITE + Fore.CYAN + Style.BRIGHT + "Su cuenta final fue de $", valorventa , ",gracias, vuelva pronto")
    if forma_de_pago == "debito":
        valorventa = cuenta + (cuenta * 0.15)
        print(Back.WHITE + Fore.CYAN + Style.BRIGHT + "Su cuenta final fue de $" , valorventa , ",gracias, vuelva pronto")
        
    print(Style.RESET_ALL)    
    print()

def calcular_precio(personas):
    
    """
    Función que calcula el precio según el numero de porciones que requiere el cliente
    Uso de: operadores, funciones.
    Recibe: El número de personas para el que es un pedido
    Devuelve: El precio de un pastel que sería calculado al multiplicar las personas por 60
    (60 es el precio de cada rebanada estándar), sumandole a eso el producto de personas
    por 4 (costo de mano de obra), más la suma de los gastos estándar de los empaques (cajas, bases),
    más el cociente de la suma de personas y 60, entre 2 (gastos luz, gas, batidora).  
    """
    
    return (personas * 60 + (personas * 4) + 45 + ((personas + 60 )/ 2))


def imprimir_orden(sabor, crema, deco):
    
    """
    Reimprime y ordena la orden del cliente, según los datos que nos brindó.
    Uso de: Funciones 
    Recibe: El sabor del pan, el sabor de la crema y la decoración que quieren,
    como las variables sabor, crema y deco, respectivamente.
    Devuelve: No devuelve ningún valor, solo ejecuta lo que lleva dentro.
    """
    print()
    print("Usted pidio un pastel sabor ",sabor.lower(),",con crema de ",crema.lower()," y decoración de ",deco.lower())
    print()

    
def calcular_corte(m50, m1, m2, m5, m10, b20, b50, b100, b200, b500, b1000):
    
    """
    Calcula el dinero que hay hasta ese momentoen la caja,
    según los valores y cantidad de monedas y billetes.
    Uso de: operadores, funciones.
    Recibe: Cantidad de monedas o billetes de cada valor. Siendo
    los que empiezan con m, las monedas, y los que empiezan con
    b, los billetes.
    Devuelve: La suma de los valores totales de monedas y billetes.
    """
    
    m = ((m50 * 0.5) + (m1) + (m2 * 2) + (m5 * 5) + (m10 * 10))
    b = ((b20 * 20) + (b50 * 50) + (b100 * 100) + (b200 * 200) + (b500 * 500) + (b1000 * 1000))
    
    return (m + b)


"""
================================Parte principal del programa=================================
"""
"""
Aquí empieza la parte principal del programa.
Abajo se importa el modulo datetime,que permite
insertar la fecha exacta con el tiempo
"""
    
from datetime import datetime

h = 1

while h<5 and h>0:
    
    """
    Aquí empieza el primer menú de opciones, para que el usuario
    pueda ir a cualquiera de todas las opciones.
    También hacemos uso de Colorama.
    Todo está dentro de un ciclo while.
    """
    
    print()
    print(Back.WHITE + Fore.YELLOW + "Hola! ¿Qué te gustaría hacer?" )
    h=int(input("\n1)Registrar una venta \n2)Cotizar una orden \n3)Hacer un pedido \n4)Corte de caja \n5)Terminar el programa \nQuisiera (indica el numero de la opción): "))
    print(Style.RESET_ALL)
    print()


    """
    Error de Avance 2 Corregido: No necesitaba parámetros,
    pero ya corre sin errores.
    Uso de un ciclo while para repetir las acciones de venta directa
    hasta que el cliente quiera dejar de comprar.
    """
    
    if h == 1:
        rep = ""
        while rep != "No" and rep != "no" and rep != "NO":
            venta_directa()
            rep = str(input("¿Desea seguir comprando? Indica Si o No: "))

                
    """
    Menú de cotizaciones, se repite hasta que el cliente quiera dejar de
    realizar su cotización.
    """
    
    if h == 2:
        rep = ""
        while rep != "No" and rep != "no" and rep != "NO":
            menu1()
            sabor = (str(input("¿Qué sabor de pan le interesa? \n(Por favor escriba el nombre, no el número): ")))
            personas = int(input("¿Para cuántas porciones sería? \n(Escríbalo con número): "))
            crema = (str(input("¿Qué sabor de crema le interesa? \n(Por favor escriba el nombre, no el número):")))
            deco = (str(input("¿Qué tipo de decoración le interesa? \n(Por favor escriba el nombre, no el número):")))
            print(Fore.WHITE + Back.MAGENTA + Style.BRIGHT + "Su costo es", calcular_precio(personas))
            imprimir_orden(sabor, crema, deco)
            print(Style.RESET_ALL)
            rep = str(input(("¿Quiere volver a realizar su cotización? \nIndiquenos Sí o No: ")))

    
    """
    Menú de órdenes. Se repite hasta la linea: 439 ,cuando el cliente esta satisfecho con su orden,
    lo lleva a pagar y le reimprime el precio con cambio (si lo hubo) y su orden.
    """
    
    if h == 3:
        
        rep = ""
        while rep != "Si" and rep != "si" and rep != "SI":
            
            menu1()
            sabor = (str(input("¿Qué sabor de pan le interesa? \n(Por favor escriba el nombre, no el número): ")))
            personas = int(input("¿Para cuántas porciones sería? \n(Escríbalo con número): "))
            crema = (str(input("¿Qué sabor de crema le interesa? \n(Por favor escriba el nombre, no el número): ")))
            deco = (str(input("¿Qué tipo de decoración le interesa? \n(Por favor escriba el nombre, no el número): ")))
            print(Back.WHITE + Fore.MAGENTA + Style.BRIGHT + "Su costo es", calcular_precio(personas))
            cuenta = calcular_precio(personas)
            imprimir_orden(sabor, crema, deco)
            print(Style.RESET_ALL)
            print("Su fecha de pedido es", datetime.today().strftime('%d-%m-%Y %H:%M'))
            rep = str(input(("¿Se encuentra satisfecho con su orden? \nIndiquenos Sí o No: ")))
            
        forma_de_pago = str(input("¿Su pago es en efectivo o tarjeta de crédito o tarjeta de débito? \nSi es efectivo, por favor escriba efectivo, si es tarjeta de crédito, por favor escriba credito, y si no es ninguna de las anteriores, escriba debito: "))
        if forma_de_pago == ("efectivo"):
            valorventa = cuenta
            print(Back.WHITE + Fore.BLUE + Style.BRIGHT + "Su cuenta final fue de $", valorventa, ",gracias, vuelva pronto")
        if forma_de_pago == "credito":
            valorventa = cuenta + (cuenta * 0.10)
            print(Back.WHITE + Fore.CYAN + Style.BRIGHT + "Su cuenta final fue de $", valorventa, ",gracias, vuelva pronto")
        if forma_de_pago == "debito":
            valorventa = cuenta + (cuenta * 0.15)
            print(Back.WHITE + Fore.MAGENTA + Style.BRIGHT + "Su cuenta final fue de $",valorventa,",gracias, vuelva pronto")
        imprimir_orden(sabor, crema, deco)
        print(Style.RESET_ALL)

    """
    Calculadora del corte. Se ingresan cantidades de monedas/ billetes de diferentes
    denominaciones, e imprime la cantidad. Luego imprime qué cantidad de ese dinero
    se va a mis ganancias, y a la pastelería. El restante no se toma en cuenta.
    """    
    if h == 4:
        
        m50 = int (input("¿Cuantas monedas de 50 c tenemos? "))
        m1 = int (input("¿Cuantas monedas de $1 tenemos? "))
        m2 = int (input("¿Cuantas monedas de $2 tenemos? "))
        m5 = int (input("¿Cuantas monedas de $5 tenemos? "))
        m10 = int (input("¿Cuantas monedas de $10 tenemos? "))
        b20 = int (input("¿Cuantos billetes de $20 tenemos? "))
        b50 = int (input("¿Cuantos billetes de $50 tenemos? "))
        b100 = int (input("¿Cuantos billetes de $100 tenemos? "))
        b200 = int (input("¿Cuantos billetes de $200 tenemos? "))
        b500 = int (input("¿Cuantos billetes de $500 tenemos? "))
        b1000 = int (input("¿Cuantos billetes de $1000 tenemos? "))
        print(Back.GREEN+Fore.WHITE+"El corte final es: ", calcular_corte(m50 ,m1, m2, m5, m10, b20, b50, b100, b200, b500, b1000))
        print(Back.RED+Fore.WHITE+"Recuerda dejar el 50% del total para gastos de la pastelería: ",((calcular_corte(m50 ,m1, m2, m5, m10, b20, b50, b100, b200, b500, b1000))/2))
        
        ganancia_dam = ((calcular_corte(m50 ,m1, m2, m5, m10, b20, b50, b100, b200, b500, b1000)) / 2) / (2.5)
        
        if ganancia_dam > 0:
            print(Back.WHITE+Fore.MAGENTA+"Hoy te ganaste:", ganancia_dam)
            print(Style.RESET_ALL)
        else:
            print(Back.WHITE+Fore.BLUE+"Hoy no ganaste dinero, mañana será un mejor día :) ")
            print(Style.RESET_ALL)
            
        print("Realizaste el corte el: ", datetime.today().strftime('%d-%m-%Y %H:%M'))
        
        h = 6

else:
    """
    Se termina el ciclo y el programa.
    """
    print("Adios, nos vemos pronto  :) ")
