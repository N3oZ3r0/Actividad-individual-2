import six
six.MAXSIZE
9223372036854775807

n = 21806108
log = True


# Funcion que tiene tres bucles diferentes
def ejercicio_a():
    global n
    k = [n]
    j = [n]
    i = 0
    for i in range(n-1):
        k.append(i+1)
        j.append(i+1)
    k.extend(j)
    print("La mediana del array es : ", k.index(n/2))

# Funcion que determina si el numero es primo
def ejercicio_b():
    n = 0


# Funcion que calcula el producto de dos matrices
def ejercicio_c():
    n = 0


# Funcion recursiva que indica si el numero es capicua
def ejercicio_d():
    n = 0


# Funcion principal
def main():
    ejercicio = '0'
    loop = True

    while loop:
        print("\n\n\nElija una de las opciones")
        print("Escriba 1 para el Ejercicio A")
        print("Escriba 2 para el Ejercicio B")
        print("Escriba 3 para el Ejercicio C")
        print("Escriba 4 para el Ejercicio D")
        print("Escriba 0 para finalizar")

        ejercicio = input("Escriba una opcion: ")

        if ejercicio == '1':
            ejercicio_a()
        elif ejercicio == '2':
            ejercicio_b()
        elif ejercicio == '3':
            ejercicio_c()
        elif ejercicio == '4':
            ejercicio_d()
        elif ejercicio == '0':
            loop = False
            print("Que pase un buen dia.")
        else:
            print("Elija una opcion valida.")


def login():
    global log
    while log == False:
        email = input("Ingrese su email: ")
        contra = input("Ingrese su password: ")
        if (email == '21806108@live.uem.es'):
            if (contra == '1234'):
                print("Acceso concedido")
                log = True
        else:
            print("Email y password invalidos")
            exit()


login()
if log:
    main()
