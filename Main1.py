from Funciones1 import *
from Inputs1 import *
import os

bandera_uno = False
bandera_dos = False
participantes = crear_array(5, "")
puntajes = crear_matriz(5, 3, 0)

def mostrar_menu():
    ancho = 60
    opciones = [
        "1.  Cargar participantes",
        "2.  Cargar puntuaciones",
        "3.  Mostrar puntuaciones",
        "4.  Participantes con promedio mayor a 4",
        "5.  Participantes con promedio mayor a 7",
        "6.  Promedio de cada jurado",
        "7.  Jurado más estricto",
        "8.  Buscar participante por nombre",
        "9.  Top 3 participantes",
        "10. Orden alfabético de participantes",
        "11. Mostrar ganador",
        "12. Desempatar",
        "13. Limpiar pantalla",
        "0.  Salir"
    ]
    print("\n" + "=" * ancho)
    print(" MENÚ DE OPCIONES ".center(ancho, "="))
    print("=" * ancho)
    for opcion in opciones:
        print(opcion)
    print("=" * ancho)

while True:
    mostrar_menu()
    try:
        opcion = pedir_opcion_menu()
    except ValueError:
        print("Opción inválida. Intente nuevamente.")
        continue

    if opcion == 1:
        cargar_nombre_participante(participantes)
        input_nombre_participante(participantes)
        bandera_uno = True

    elif opcion == 2 and bandera_uno:
        cargar_puntajes(puntajes)
        bandera_dos = True

    elif opcion == 3 and bandera_dos:
        mostrar_participantes_con_promedios(participantes, puntajes)
        promedio_general = calcular_promedio_general(puntajes)
        print(f"Promedio general: {promedio_general:.2f}")

    elif opcion == 4 and bandera_dos:
        hay_resultados = False
        for i in range(len(participantes)):
            promedio = calcular_promedio_fila(puntajes, i)
            if promedio > 4:
                mostrar_un_participante(participantes, puntajes, i)
                hay_resultados = True
        if not hay_resultados:
            print("No hay participantes con promedio mayor a 4.")

    elif opcion == 5 and bandera_dos:
        hay_resultados = False
        for i in range(len(participantes)):
            promedio = calcular_promedio_fila(puntajes, i)
            if promedio > 7:
                mostrar_un_participante(participantes, puntajes, i)
                hay_resultados = True
        if not hay_resultados:
            print("No hay participantes con promedio mayor a 7.")

    elif opcion == 6 and bandera_dos:
        for jurado in range(3):
            promedio = calcular_promedio_columna(puntajes, jurado)
            print(f"Promedio del jurado {jurado+1}: {promedio:.2f}")

    elif opcion == 7 and bandera_dos:
        promedios = crear_array(3, 0)
        for jurado in range(3):
            promedio = calcular_promedio_columna(puntajes, jurado)
            promedios[jurado] = promedio

        minimo = promedios[0]
        for i in range(1, 3):
            if promedios[i] < minimo:
                minimo = promedios[i]
        print("Jurado/s más estricto/s: ")
        for i in range(3):
            if promedios[i] == minimo:
                print(f"Jurado {i + 1} con un promedio de {promedios[i]:.2f}")

    elif opcion == 8 and bandera_dos:
        nombre_buscado = input("Ingrese el nombre a buscar: ")
        encontrados = False
        for i in range(len(participantes)):
            if participantes[i].lower() == nombre_buscado.lower():
                mostrar_un_participante(participantes, puntajes, i)
                print("")
                encontrados = True
        if not encontrados:
            print("No se encontró participante con ese nombre.")

    elif opcion == 9 and bandera_dos:
        ordenar_participantes_por_total(participantes, puntajes)
        print("Top tres participantes con mayor puntaje total:")
        mostrados = 0
        for i in range(len(participantes)):
            if mostrados < 3:
                mostrar_un_participante(participantes, puntajes, i)
                print("")
                mostrados += 1

    elif opcion == 10 and bandera_dos:
        ordenar_participantes_alfabeticamente(participantes, puntajes)
        mostrar_participantes(participantes, puntajes)

    elif opcion == 11 and bandera_dos:
        mostrar_ganador(participantes, puntajes)

    elif opcion == 12 and bandera_dos:
        desempatar(participantes, puntajes)

    elif (opcion in [2,3,4,5,6,7,8,9,10,11,12]) and not bandera_dos:
        print("Error: Primero debe cargar los participantes y sus puntajes (opciones 1 y 2).")

    elif opcion == 13:
        os.system("cls")
        continue

    elif opcion == 0:
        print("Saliendo...")
        break

    else:
        print("Opción inválida.")

    input("Toque cualquier botón para continuar...")
    os.system("cls")