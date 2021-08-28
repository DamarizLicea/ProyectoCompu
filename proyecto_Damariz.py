"""Profe, ignore por ahorita si mis funciones no estan muy bien hechas, la parte de operadores creo que esta sobretodo en la de venta y calcular orden, cuando corra
el programa, porfavor solo seleccione la opcion de venta, porque es la que tengo ya terminada para que se evaluara lo de operadores, gracias :)"""
def acumulador_dinero():
    dinero=0
    dinero=dinero+valorventa
    print("El dinero en caja es",dinero)
def menu1():
    print("Hola! Bienvenido a Keikiz, nuestro menú para ordenes de pasteles es éste: \n1)Red Velvet\n2)Zanahoria \n3)Gansito \n4)Chocolate Clásico \n5)Chai \n6)Vainilla \n7)Limón")
    print("El menú de rellenos es éste: \n1)Buttercream de Vainilla \n2)Crema de queso \n3)Mermelada de frutos rojos \n4)Buttercream de chocolate \n5)Buttercream de PB \n6)Lemon Curd")
    print("Nuestro menú para decoraciones es este: \n1)Fondant \n2)Chocolate \n3)Buttercream \n4)Moldeado")
def menu2():
    print("Hola! Bienvenido a Keikiz, nuestro menú por rebanadas para hoy es éste: \n1)Tarta de nuez $20 \n2)Pastel de miel $40 \n3)Pastel de rollo $35 \n4)Pastel de Brownie $30 \n5)Cheesecake de pera $45 \n6)Pay de manzana $45")
def venta():
    menu2()
    producto=int(input("¿Qué va a querer?"))
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
def sabores():
    sabor=int(input("¿Qué sabor le gustaría?"))
    if sabor==1:
        pan=str("Red Velvet")
    if sabor==2:
        pan=str("Zanahoria")
    if sabor==3:
        pan=str("Gansito")
    if sabor==4:
        pan=str("Chocolate Clasico")
    if sabor==5:
        pan=str("Chai")
    if sabor==6:
        pan=str("Vainilla")
    if sabor==7:
        pan=str("Limón")
    return pan
def cremas():
    relleno=int(input("¿Qué relleno le gustaría?"))
    if relleno==1:
        crema=str("Buttercream de Vainilla")
    if relleno==2:
        crema=str("Crema de Queso")
    if relleno==3:
        crema=str("Mermelada de frutos rojos")
    if relleno==4:
        crema=str("Buttercream de chocolate")
    if relleno==5:
        crema=str("Buttercream de PB")
    if relleno==6:
        crema=str("Lemon Curd")
    return crema
def decoracion():
    decorado=int(input("¿Qué tipo de decorado quiere? "))
    if decorado==1:
        deco=str("Fondant")
    if decorado==2:
        deco=str("Chocolate")
    if decorado==3:
        deco=str("Buttercream")
    if decorado==4:
        deco=str("Moldeado")
    return deco
def calcularorden():
    personas=int(input("¿Para cuantas porciones sería? "))
    sabores()
    cremas()
    decoracion()
    precio=personas*60+(personas*4)+45+((personas*60)/2)
    print("Su precio final es ", precio)
def resumen():
    print("Su orden es: su decoración ", deco, " sus porciones serían para ", personas," personas,su sabor es ", pan, " y su relleno es ", crema)
def contento():
    repono=str(input(("¿Se encuentra satisfecho con su orden? Indiquenos Sí o No: ")))
#falta lo del loop
def cotizar():
    menu1()
    calcularorden()
    resumen()
    contento()

def inicio():
    h=int(input(print("Hola! ¿Qué te gustaría hacer? \n1)Registrar una venta \n2)Cotizar una orden \n3)Hacer un pedido \n4)Corte de caja \npor ahora solo seleccione venta, profe")))
    if h==1:
        venta()
    if h==2:
        cotizar()
    if h==3:
        pedido()
    if h==4:
        corte()
inicio()
    

