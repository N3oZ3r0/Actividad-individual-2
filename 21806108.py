import numpy as np
import six

six.MAXSIZE
9223372036854775807

n = 21806108
log = False


# Funcion que tiene el Ejercicio A
def ejercicio_a():
    global n
    k = []
    j = []
    for i in range(n):
        k.append(i + 1)
        j.append(i + 1)

    k.extend(j)
    k.sort()
    x = int(len(k) / 2)
    print("La mediana es : ", k[x])


# Funcion que tiene el Ejercicio B
def ejercicio_b():
    global n
    x = []
    y = []
    for i in range(n):
        x.append(i + 1)
        y.append(i + 1)
    if np.array_equal(x, y):
        print("Los array son iguales")
    else:
        print("Los array no son iguales")


# Funcion que tiene el Ejercicio C
def ejercicio_c():
    global n
    M = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append((j+1)*(i+1))
        M.append(fila)

    np.transpose(M)

    for i in range(n):
        print(M[i])

# Funcion que tiene el Ejercicio D
def ejercicio_d():
    global n
    ant = None
    act = None
    pico = 0
    picoant = 0
    valle = 0
    valleant = 0
    X = np.random.randint(1, 21806108, n)

    for i in X:
        if act == None:
            act = i
        else:
            if i != act:
                if ant != None:
                    if (ant < act and i < act):
                        pico = i
                        distancia = abs(pico - valle)
                        distanciaant = abs(picoant - valleant)
                        if (distancia > distanciaant):
                            picoant = pico

                    elif (ant > act and i > act):
                        valle = i
                        distancia= abs(pico - valle)
                        distanciaant = abs(picoant - valleant)
                        if (distancia > distanciaant):
                            valleant = valle

                else:
                    ant = act
                    valle = i
                    distancia = abs(pico - valle)
                    distanciaant = abs(picoant - valleant)
                    if (distancia > distanciaant):
                        valleant = valle
                ant = act
                act = i

    distancia = abs(picoant - valleant)

    print("La distancia es ", distancia)


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
