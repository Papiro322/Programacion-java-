def mostrar():
    print("======================================")

    p='''
    /$$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$  /$$      /$$  /$$$$$$        /$$$$$$$  /$$$$$$$$        /$$$$$$   /$$$$$$  /$$      /$$ /$$$$$$$  /$$$$$$  /$$$$$$        /$$$$$$$  /$$$$$$$$        /$$$$$$   /$$$$$$  /$$       /$$$$$$$$  /$$$$$$ 
    | $$__  $$| $$__  $$ /$$__  $$ /$$__  $$| $$__  $$ /$$__  $$| $$$    /$$$ /$$__  $$      | $$__  $$| $$_____/       /$$__  $$ /$$__  $$| $$$    /$$$| $$__  $$|_  $$_/ /$$__  $$      | $$__  $$| $$_____/       /$$__  $$ /$$__  $$| $$      | $$_____/ /$$__  $$
    | $$  \ $$| $$  \ $$| $$  \ $$| $$  \__/| $$  \ $$| $$  \ $$| $$$$  /$$$$| $$  \ $$      | $$  \ $$| $$            | $$  \__/| $$  \ $$| $$$$  /$$$$| $$  \ $$  | $$  | $$  \ $$      | $$  \ $$| $$            | $$  \__/| $$  \ $$| $$      | $$      | $$  \__/
    | $$$$$$$/| $$$$$$$/| $$  | $$| $$ /$$$$| $$$$$$$/| $$$$$$$$| $$ $$/$$ $$| $$$$$$$$      | $$  | $$| $$$$$         | $$      | $$$$$$$$| $$ $$/$$ $$| $$$$$$$   | $$  | $$  | $$      | $$  | $$| $$$$$         |  $$$$$$ | $$  | $$| $$      | $$$$$   |  $$$$$$ 
    | $$____/ | $$__  $$| $$  | $$| $$|_  $$| $$__  $$| $$__  $$| $$  $$$| $$| $$__  $$      | $$  | $$| $$__/         | $$      | $$__  $$| $$  $$$| $$| $$__  $$  | $$  | $$  | $$      | $$  | $$| $$__/          \____  $$| $$  | $$| $$      | $$__/    \____  $$
    | $$      | $$  \ $$| $$  | $$| $$  \ $$| $$  \ $$| $$  | $$| $$\  $ | $$| $$  | $$      | $$  | $$| $$            | $$    $$| $$  | $$| $$\  $ | $$| $$  \ $$  | $$  | $$  | $$      | $$  | $$| $$             /$$  \ $$| $$  | $$| $$      | $$       /$$  \ $$
    | $$      | $$  | $$|  $$$$$$/|  $$$$$$/| $$  | $$| $$  | $$| $$ \/  | $$| $$  | $$      | $$$$$$$/| $$$$$$$$      |  $$$$$$/| $$  | $$| $$ \/  | $$| $$$$$$$/ /$$$$$$|  $$$$$$/      | $$$$$$$/| $$$$$$$$      |  $$$$$$/|  $$$$$$/| $$$$$$$$| $$$$$$$$|  $$$$$$/
    |__/      |__/  |__/ \______/  \______/ |__/  |__/|__/  |__/|__/     |__/|__/  |__/      |_______/ |________/       \______/ |__/  |__/|__/     |__/|_______/ |______/ \______/       |_______/ |________/       \______/  \______/ |________/|________/ \______/ 
    '''
    print("======================================")
    print(p)  
    print("Menu de Opciones")
    print("1. Cambiar soles a dolares")
    print("2. Cambiar dolares a Soles")
    print("3. Cambiar soles a Euros")

def solucion():
    import getpass
    soles="1"
    dolares="2"
    euros="3"
    accion=input("Indique la Opcion del Menu[1,2,3,]:")
    if soles==accion:
        print("Ud. ingreso al cambio de soles a dolares")
        print("========================================")
        dolares=3.38
        a=int(input("Ingrese el monto en soles: "))
        resultado1=a*dolares
        print("El monto total es: ",resultado1) 
    else:
        if dolares==accion:
            print("Ud. ingreso al cambio de dolares a soles")
            print("========================================")
            sol=3.38
            b=float(input("Ingrese el monto en euros: "))
            resultado2=b*sol
            print("El monto total es: ",resultado2)
        else:
            euros==accion
            print("Ud. ingreso al cambio de soles a euros")
            print("========================================")
            euro=3.82
            c=float(input("Ingrese el monto en soles: "))
            resultado3=c*euro
            print("El monto total es: ",resultado3)

mostrar()
solucion()