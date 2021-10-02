"""
-------------------------------------------------------------------------funciones del programa-------------------------------------------------------------------------------------
"""
def menu1():
    print()
    print("Hola! Bienvenido a Keikiz, nuestro menú para ordenes de pasteles es éste:")
    lista_pan=[['1','Red Velvet'],
              ['2','Zanahoria'],
              ['3','Gansito'],
              ['4','Chocolate Clásico'],
              ['5','Chai'],
              ['6','Vainilla'],
              ['7','Limón']]
    
    def imprfor(lista_pan):
        for linea in lista_pan:
            for columna in linea:
                print(columna,end=" ")
            print()
    imprfor(lista_pan)
    print()
    print("El menú de rellenos es éste:")
    lista_relleno=[['1','Buttercream de Vainilla'],
                   ['2','Crema de Queso'],
                   ['3','Mermelada de frutos rojos'],
                   ['4','Buttercream de chocolate'],
                   ['5','Buttercream de PB'],
                   ['6','Lemon Curd']]
    def impwhile(lista_relleno):
        valor=0
        i=0
        while i<len(lista_relleno):
            j=0
            while j<len(lista_relleno[0]):
                print(lista_relleno[i][j],end=" ")
                j=j+1
            print()
            i=i+1
    impwhile(lista_relleno)
    print()
    print("Nuestro menú para decoraciones es este:")
    listadeco=[['1','Fondant'],
               ['2','Chocolate'],
               ['3','Buttercream'],
               ['4','Moldeado']]
    def impwhile(listadeco):
        valor=0
        i=0
        while i<len(listadeco):
            j=0
            while j<len(listadeco[0]):
                print(listadeco[i][j],end=" ")
                j=j+1
            print()
            i=i+1
    impwhile(listadeco)
    print()
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
def imprimir_orden(sabor,crema,deco):
    print("Usted pidio un pastel sabor ",sabor.lower(),",con crema de ",crema.lower()," y decoración de ",deco.lower())
"""
===============================================================================AQUÍ YA CORRE EL PROGRAMA===========================================================================
"""
h=int(input(print("Hola! ¿Qué te gustaría hacer? \n1)Registrar una venta \n2)Cotizar una orden \n3)Hacer un pedido \n4)Corte de caja")))
while h!=5:
    if h==1:
        venta_directa()
        rep=input("¿Desea seguir comprando?")
        if rep=="si" or rep=="Si":
            continue
        else:
            break
    if h==2:
        print("Hola, bienvenido a nuestro sistema de cotizaciones")
        menu1()
        sabor=(str(input("¿Qué sabor de pan le interesa? ")))
        personas=int(input("¿Para cuántas porciones sería? "))
        crema=(str(input("¿Qué sabor de crema le interesa? ")))
        deco=(str(input("¿Qué tipo de decoración le interesa? ")))
        print("Su costo es", calcular_precio(personas))
        imprimir_orden(sabor,crema,deco)
        rep=str(input(("¿Se encuentra satisfecho con su cotización? Indiquenos Sí o No: ")))
        if rep=="No" or rep=="No":
            continue
        else:
            break
    if h==3:
        print("Hola, bienvenido a nuestro sistema de ordenes")
        menu1()
        sabor=(str(input("¿Qué sabor de pan le interesa? ")))
        personas=int(input("¿Para cuántas porciones sería? "))
        crema=(str(input("¿Qué sabor de crema le interesa? ")))
        deco=(str(input("¿Qué tipo de decoración le interesa? ")))
        print("Su costo es", calcular_precio(personas))
        cuenta=calcular_precio(personas)
        imprimir_orden(sabor,crema,deco)
        rep=str(input(("¿Se encuentra satisfecho con su orden? Indiquenos Sí o No: ")))
        if rep=="no" or rep=="No":
            continue
        else:
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
        break
    if h==4:
        print("Todavia no hay nada aquí.")
        rep=str(input(("¿Quieres cerrar el corte?")))
        if rep=="si" or rep=="Si":
            continue
        else:
            break
else:
    print("Hemos cerrado, ten una buena noche.")
