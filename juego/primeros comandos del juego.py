# -*- coding: utf-8 -*-
"""
Creado el viernes 31 de enero a las 13:23:02 del año 2025

@author: Jair Ronquillo 
"""

"""
Inicio:
    Se ingresan las variables de entrada, en este caso son:
        *Usuario: es creada con el nombre del jugador.
        *numero_adv: Es la variable en donde se aloja el número ingresado
        por el usuario.Utilizo el int para que directamente le salga error al
        usuario si no ingresa un número.
        
"""
usuario= input ("ingresa tu nombre:")

numero_adv=int(input("ingresa un número del 1 al 5 para que la maquina adivine:"))

    
"""
Primer problematica a resolver:
    Si el usuario ingresa un valor de tipo letras en la variable número el
    algoritmo mostrara el mensaje, "Tu número no esta dentro del rango".
"""


if numero_adv==1:
    print("Hola ",usuario)
    print("Tu número es ",numero_adv)
else:
    if numero_adv==2:
        print("Hola ",usuario)
        print("Tu número es ",numero_adv)
    else:
        if numero_adv==3:
            print("Hola ",usuario)
            print("Tu número es ",numero_adv)
        else:
            if numero_adv==4:
                print("Hola ",usuario)
                print("Tu número es ",numero_adv)
            else:
                if numero_adv==5:
                    print("Hola ",usuario)
                    print("Tu número es ",numero_adv)
                else:
                    print("Hola ",usuario)
                    print("Tu número no esta dentro del rango")
                    print("Vuelve a intentarlo")
        
    
print("fin del programa, gracias por jugar :)")

