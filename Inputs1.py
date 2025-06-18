def input_Puntuación_del_Jurado(mensaje):
    """
    Solicita y valida la puntuación de un jurado para un participante.
    La puntuación debe ser un número entero entre 1 y 10.
    Args:
        mensaje (str): El mensaje que se muestra al usuario para pedir la puntuación.
    Returns:
        int: La puntuación validada ingresada por el usuario.
    """
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 1 or valor > 10:
                print("La puntuación debe estar entre 1 y 10.")
                continue
            return valor
        except ValueError:
            print("Debe ingresar un número entero.")

def input_nombre_participante():
    """
    Solicita y valida un nombre en el formato: letra espacio letra espacio letra (ej: 'a b c').
    Solo se permiten letras y espacios, y debe haber exactamente ese orden.
    Returns:
        str: El nombre validado.
    """
    while True:
        nombre = input("Ingrese el nombre (formato: letra espacio letra espacio letra, ej: 'a b c'): ")
        if len(nombre) != 5:
            print("El nombre debe tener exactamente 5 caracteres (letra espacio letra espacio letra).")
            continue
        # Verificar la posición de las letras y espacios manualmente
        valido = True
        for validacion_nombre in range(5):
            c = nombre[validacion_nombre]
            codigo = ord(c) #Uso ord() para convertir un carácter en su valor numérico y así verificar si es una letra
            if validacion_nombre % 2 == 0:  # Deben ser letras (posiciones 0, 2, 4)
                if not ((65 <= codigo <= 90) or (97 <= codigo <= 122)):
                    valido = False
                    break
            else:  # Deben ser espacios (posiciones 1, 3)
                if codigo != 32:
                    valido = False
                    break
        if not valido:
            print("Formato inválido. Debe ser letra espacio letra espacio letra.")
            continue
        return nombre

def pedir_opcion_menu() -> int:
    """
    Solicita y valida la opción del menú ingresada por el usuario.
    La opción debe ser un número entero entre 0 y 13.
    Returns:
        int: La opción validada seleccionada por el usuario.
    """
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion < 0 or opcion > 13:
                print("Opción fuera de rango.")
                continue
            return opcion
        except ValueError:
            print("Debe ingresar un número entero.")

def cargar_nombre_participante(array_participantes:list) -> None:
    """
    Carga los nombres de los participantes en la lista recibida por parámetro.
    Solicita un nombre válido para cada posición de la lista.
    Args:
        array_participantes (list): Lista donde se almacenarán los nombres de los participantes.
    Returns:
        None
    """
    for i in range(len(array_participantes)):
        array_participantes[i] = input_nombre_participante()

def cargar_puntajes(matriz_puntajes: list) -> None:
    """
    Carga las puntuaciones de los jurados para cada participante en la matriz recibida.
    Solicita una puntuación válida para cada jurado y cada participante.
    Args:
        matriz_puntajes (list): Matriz donde se almacenarán las puntuaciones.
    Returns:
        None
    """
    for i in range(len(matriz_puntajes)):
        for j in range(len(matriz_puntajes[i])):
            mensaje = f"Ingrese la puntuación del jurado {j+1} para el participante {i+1} (1-10): "
            matriz_puntajes[i][j] = input_Puntuación_del_Jurado(mensaje)