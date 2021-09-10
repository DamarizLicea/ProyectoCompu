"""
-------------------------------------------------------------------------funciones del programa-------------------------------------------------------------------------------------
"""
def menu1():
    print("Hola! Bienvenido a Keikiz, nuestro menú para ordenes de pasteles es éste: \n1)Red Velvet\n2)Zanahoria \n3)Gansito \n4)Chocolate Clásico \n5)Chai \n6)Vainilla \n7)Limón")
    print("El menú de rellenos es éste: \n1)Buttercream de Vainilla \n2)Crema de queso \n3)Mermelada de frutos rojos \n4)Buttercream de chocolate \n5)Buttercream de PB \n6)Lemon Curd")
    print("Nuestro menú para decoraciones es este: \n1)Fondant \n2)Chocolate \n3)Buttercream \n4)Moldeado")
def menu2():
    print("Hola! Bienvenido a Keikiz, nuestro menú por rebanadas para hoy es éste: \n1)Tarta de nuez $20 \n2)Pastel de miel $40 \n3)Pastel de rollo $35 \n4)Pastel de Brownie $30 \n5)Cheesecake de pera $45 \n6)Pay de manzana $45")
def venta_directa():
    menu2()
    producto=int(input("¿Qué va a querer?")) """amigo becario, aquí empieza mi entrega de if's para el 10/09/2021"""
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
    rebanadas=int(input("¿Cuantas rebanadas?"))
    cuenta=valor*rebanadas
    print("Su cuenta es de $", cuenta)
    forma_de_pago=str(input("¿Su pago es en efectivo o tarjeta de crédito o tarjeta de débito? Si es efectivo, por favor escriba efectivo, si es tarjeta de crédito, por favor escriba credito, y si no es ninguna de las anteriores, escriba debito: "))
    if forma_de_pago==("efectivo"):
        valorventa=cuenta
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
    return personas*60+(personas*4)+45+((personas+60/2))
def contento():
    repono=str(input(("¿Se encuentra satisfecho con su orden? Indiquenos Sí o No: ")))
def imprimir_orden(sabor,crema,deco):
    print("usted pidio un pastel sabor ",sabor,",con crema de ",crema," y decoración de ",deco)
"""
===============================================================================AQUÍ YA CORRE EL PROGRAMA===========================================================================
"""
h=int(input(print("Hola! ¿Qué te gustaría hacer? \n1)Registrar una venta \n2)Cotizar una orden \n3)Hacer un pedido \n4)Corte de caja")))
if h==1:
    
    precioventa()
if h==2:
    print("Hola, bienvenido a nuestro sistema de cotizaciones")
    menu1()
    sabor=(str(input("¿Qué sabor de pan le interesa? ")))
    personas=int(input("¿Para cuántas porciones sería? "))
    crema=(str(input("¿Qué sabor de crema le interesa? ")))
    deco=(str(input("¿Qué tipo de decoración le interesa? ")))
    fecha=str(input())
    print("Su costo es", calcular_precio(personas))
    imprimir_orden(sabor,crema,deco)
if h==3:
    print("Hola, bienvenido a nuestro sistema de ordenes")
    menu1()
    sabor=(str(input("¿Qué sabor de pan le interesa? ")))
    personas=int(input("¿Para cuántas porciones sería? "))
    crema=(str(input("¿Qué sabor de crema le interesa? ")))
    deco=(str(input("¿Qué tipo de decoración le interesa? ")))
    print("Su costo es", calcular_precio(personas))
    cuenta=calcular_precio(personas)
    forma_de_pago=str(input("¿Su pago es en efectivo o tarjeta de crédito o tarjeta de débito? Si es efectivo, por favor escriba efectivo, si es tarjeta de crédito, por favor escriba credito, y si no es ninguna de las anteriores, escriba debito: "))
    if forma_de_pago==("efectivo"):
        valorventa=cuenta
        print("gracias, vuelva pronto")
    if forma_de_pago=="credito":
        valorventa=cuenta+(cuenta*0.10)
        print("Su cuenta final fue de $",valorventa,",gracias, vuelva pronto")
    if forma_de_pago=="debito":
        valorventa=cuenta+(cuenta*0.15)
        print("Su cuenta final fue de $",valorventa,",gracias, vuelva pronto")
    imprimir_orden(sabor,crema,deco)
if h==4:
    """amigo becario, todavia no hay nada programado para esta parte, gracias   :)"""
    corte()
