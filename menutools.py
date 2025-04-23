#baner
import os
import subprocess


print("                                     ")
print(" ###  ### ### ###  ## ## ##### ##   #")
print(" #  # ##  # # #  # # # #  #### # #  #")
print(" #  # #   ### #  # #   # #   # #  # #")
print(" ###  ### # # ###  #   # ##### #   ##")

print(" 1- NMAP")
print(" 2- SQLMAP")
print(" 3- NECAT")


try:
    opcion = int(input("Elige una opcion >>"))
    if opcion == 1:
        subprocess.run(["pkg", "install", "nmap", "-y"])
        input("Presione enter para continuar")
    elif opcion == 2:
        subprocess.run(["pkg", "install", "sqlmap", "-y"])
        input("Presione enter para continuar")
    elif opcion == 3:
        subprocess.run(["pkg", "install", "netcat", "-y"])
        input("Presione enter para continuar")
    else:
        print("Opción inválida")
except ValueError:
    print("Error debes ingresar un número valido")