"""
Proyecto Keikiz by Mayiz
Damariz Licea Carrisoza A01369045
Punto de venta, cotizador de órdenes para un negocio de pastelería.
Despliega menú para venta regular de productos, permite cotizar una orden varias veces para que el cliente lo haga hasta estar contento.
Después permite que el usuario haga la orden como tal de un pedido y le da opción de pagar.
En el ultimo punto, es un contador de dinero segun el numero de monedas/billetes que el usuario ingrese.
"""
"""
------------------funciones del programa-------------------
"""
import colorama
from colorama import Fore,Back,Style
colorama.init()
""" Uso de Colorama
	Código de: https://pypi.org/project/colorama/ """

def imprfor(lista_pan):
    """ Crea el menú a partir de una matriz de 7x2 """
    for linea in lista_pan:
        for columna in linea:
            print(columna,end=" ")
        print()
def impwhile(lista_relleno):
    """Crea o ordena el menú (de una matriz de 7x2) gracias a un ciclo while"""
    valor=0
    i=0
    while i<len(lista_relleno):
        j=0
        while j<len(lista_relleno[0]):
            print(lista_relleno[i][j],end=" ")
            j=j+1
        print()
        i=i+1
def impwhile(listadeco):
    """" Misma acción que la funcion de arriba """
    valor=0
    i=0
    while i<len(listadeco):
        j=0
        while j<len(listadeco[0]):
            print(listadeco[i][j],end=" ")
            j=j+1
        print()
        i=i+1

def menu1():
    
    """Aquí está la matriz que se usa en la primera función del programa,
        también aquí englobo las primeras tres funciones,
        para poder imprimir el menú entero de una sola vez"""
    
    print()
    print(f"{Fore.GREEN}Hola! Bienvenido a Keikiz, nuestro menú para ordenes de pasteles es éste:")
    lista_pan=[['1','Red Velvet'],
              ['2','Zanahoria'],
              ['3','Gansito'],
              ['4','Chocolate Clásico'],
              ['5','Chai'],
              ['6','Vainilla'],
              ['7','Limón']]
    imprfor(lista_pan)
    print()

    print("El menú de rellenos es éste:")
    lista_relleno=[['1','Buttercream de Vainilla'],
                   ['2','Crema de Queso'],
                   ['3','Mermelada de frutos rojos'],
                   ['4','Buttercream de chocolate'],
                   ['5','Buttercream de PB'],
                   ['6','Lemon Curd']]
    impwhile(lista_relleno)
    print()

    print("Nuestro menú para decoraciones es este:")
    listadeco=[['1','Fondant'],
           ['2','Chocolate'],
           ['3','Buttercream'],
           ['4','Moldeado']]
    impwhile(listadeco)
    print()
    
def menu2():
    
    """ Aquí está el menú que ocupo en la parte
        de venta directa (menú de venta normal)"""
    
    print("Hola! Bienvenido a Keikiz, nuestro menú por rebanadas para hoy es éste: \n1)Tarta de nuez $20 \n2)Pastel de miel $40 \n3)Pastel de rollo $35 \n4)Pastel de Brownie $30 \n5)Cheesecake de pera $45 \n6)Pay de manzana $45")

def venta_directa():
    
    """ Despliega el menú para vender normalmente,
    da el precio del producto según el número del producto en el menú,
    y las porciones que pidió. El precio puede cambiar según la opción de pago."""
    
    menu2()
    producto=int(input("¿Qué va a querer? (Indique el número del producto): "))
    if producto==1:
        valor=20
    if producto==2:
        valor=40
    if producto==3:
        valor=35
    if producto==4:
        valor=30
    if producto==5 or producto==6:
        valor=45
    rebanadas=int(input("¿Cuantas rebanadas? "))
    cuenta=valor*rebanadas
    print("Su cuenta es de $", cuenta)
    forma_de_pago=str(input("¿Su pago es en efectivo o tarjeta de crédito o tarjeta de débito? Si es efectivo, por favor escriba efectivo, si es tarjeta de crédito, por favor escriba credito, y si no es ninguna de las anteriores, escriba debito: "))
    if forma_de_pago==("efectivo"):
        valorventa=cuenta
        print("Su cuenta final fue de $",valorventa)
        print("gracias, vuelva pronto")
    if forma_de_pago=="credito":
        valorventa=cuenta+(cuenta*0.10)
        print("Su cuenta final fue de $",valorventa,",gracias,vuelva pronto")
    if forma_de_pago=="debito":
        valorventa=cuenta+(cuenta*0.15)
        print("Su cuenta final fue de $",valorventa,",gracias,vuelva pronto")
        
def precioventa(producto,rebanadas):
    return producto*rebanadas

def calcular_precio(personas):
    
    """Función que calcula el precio según el
    numero de porciones que requiere el cliente"""
    
    return personas*60+(personas*4)+45+((personas+60/2))

def imprimir_orden(sabor,crema,deco):
    """ Reimprime y ordena la orden del cliente,
    según los datos que nos brindó"""
    print("Usted pidio un pastel sabor ",sabor.lower(),",con crema de ",crema.lower()," y decoración de ",deco.lower())
def calcular_corte(m50,m1,m2,m5,m10,b20,b50,b100,b200,b500,b1000):
    """"""
    m=((m50*0.5)+(m1)+(m2*2)+(m5*5)+(m10*10))
    b=((b20*20)+(b50*50)+(b100*100)+(b200*200)+(b500*500)+(b1000*1000))
    return m+b
"""
==================================================================AQUÍ YA CORRE EL PROGRAMA=============================================================
"""
from datetime import datetime
h=1
while h<6 and h>0:
    h=int(input("Hola! ¿Qué te gustaría hacer? \n1)Registrar una venta \n2)Cotizar una orden \n3)Hacer un pedido \n4)Corte de caja \n5)Terminar el programa \nQuisiera (indica el numero de la opción): "))
    if h==1:
        rep=""
        venta_directa()
        while rep!="No" and rep!="no":
            rep=str(input("¿Desea seguir comprando? "))
            rep=""
            venta_directa()
            while rep!="No" and rep!="no":
                rep=str(input("¿Desea seguir comprando? "))
    
    if h==2:
        rep=""
	while rep!="No" and rep!="no":
		print(f"{Fore.GREEN}Hola, bienvenido a nuestro sistema de cotizaciones")
        	menu1()
        	sabor=(str(input("¿Qué sabor de pan le interesa? ")))
        	personas=int(input("¿Para cuántas porciones sería? "))
        	crema=(str(input("¿Qué sabor de crema le interesa? ")))
       		deco=(str(input("¿Qué tipo de decoración le interesa? ")))
        	print("Su costo es", calcular_precio(personas))
        	imprimir_orden(sabor,crema,deco)
		rep=str(input(("¿Quiere volver a realizar su cotización? Indiquenos Sí o No: ")))
    
      
    if h==3:
        rep=""
        while rep!="Si" and rep!="si":
            print("Hola, bienvenido a nuestro sistema de ordenes")
            menu1()
            sabor=(str(input("¿Qué sabor de pan le interesa? ")))
            personas=int(input("¿Para cuántas porciones sería? "))
            crema=(str(input("¿Qué sabor de crema le interesa? ")))
            deco=(str(input("¿Qué tipo de decoración le interesa? ")))
            print("Su costo es", calcular_precio(personas))
            cuenta=calcular_precio(personas)
            imprimir_orden(sabor,crema,deco)
            print("Su fecha de pedido es",datetime.today().strftime('%d-%m-%Y %H:%M'))
            rep=str(input(("¿Se encuentra satisfecho con su orden? Indiquenos Sí o No: ")))
            
        forma_de_pago=str(input("¿Su pago es en efectivo o tarjeta de crédito o tarjeta de débito? Si es efectivo, por favor escriba efectivo, si es tarjeta de crédito, por favor escriba credito, y si no es ninguna de las anteriores, escriba debito: "))
        if forma_de_pago==("efectivo"):
            valorventa=cuenta
            print("Su cuenta final fue de $",valorventa,",gracias, vuelva pronto")
        if forma_de_pago=="credito":
            valorventa=cuenta+(cuenta*0.10)
            print("Su cuenta final fue de $",valorventa,",gracias, vuelva pronto")
        if forma_de_pago=="debito":
            valorventa=cuenta+(cuenta*0.15)
            print("Su cuenta final fue de $",valorventa,",gracias, vuelva pronto")
        imprimir_orden(sabor,crema,deco)
        
    if h==4:
        m50=int(input("¿Cuantas monedas de 50 c tenemos? "))
        m1=int(input("¿Cuantas monedas de $1 tenemos? "))
        m2=int(input("¿Cuantas monedas de $2 tenemos? "))
        m5=int(input("¿Cuantas monedas de $5 tenemos? "))
        m10=int(input("¿Cuantas monedas de $10 tenemos? "))
        b20=int(input("¿Cuantos billetes de $20 tenemos? "))
        b50=int(input("¿Cuantos billetes de $50 tenemos? "))
        b100=int(input("¿Cuantos billetes de $100 tenemos? "))
        b200=int(input("¿Cuantos billetes de $200 tenemos? "))
        b500=int(input("¿Cuantos billetes de $500 tenemos? "))
        b1000=int(input("¿Cuantos billetes de $1000 tenemos? "))
        print("El corte final es: ", calcular_corte(m50,m1,m2,m5,m10,b20,b50,b100,b200,b500,b1000))
        print("Realizaste el corte el: ", datetime.today().strftime('%d-%m-%Y %H:%M'))
        h=6
    if h==5:
        print(Fore.GREEN+"Hola bby")

else:
    print("Adios, nos vemos pronto  :) ")
