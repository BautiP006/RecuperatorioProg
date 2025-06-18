import random

# GENERAL
def validar_entero_positivo(cadena:str) -> bool: #1
    """
    Valida que la cadena sea un entero positivo.
    Args:
        cadena (str): La cadena a validar.
    Returns:
        bool: True si es entero positivo, False en caso contrario.
    """
    if len(cadena) == 0:
        return False
    for caracter in cadena:
        if ord(caracter) < 48 or ord(caracter) > 57:
            return False
    return True

# GENERAL
def crear_array(cantidad_elementos:int,valor_inicial:any) -> list: #2
    """
    Crea un array (lista) con una cantidad de elementos y un valor inicial dado.
    Args:
        cantidad_elementos (int): Cantidad de elementos del array.
        valor_inicial (any): Valor con el que se inicializa cada elemento.
    Returns:
        list: El array creado.
    """
    array = [valor_inicial] * cantidad_elementos
    return array

# ESPECIFICA
def es_nombre_valido(cadena: str) -> bool: #3
    """
    Valida que el nombre tenga al menos 3 letras (mayúsculas o minúsculas) y permite espacios.
    Args:
        cadena (str): Nombre a validar.
    Returns:
        bool: True si es válido, False si contiene caracteres no permitidos o tiene menos de 3 letras.
    """
    if len(cadena) == 0:
        return False
    contador_letras = 0
    for caracter in cadena:
        codigo = ord(caracter)
        if (65 <= codigo <= 90) or (97 <= codigo <= 122):
            contador_letras += 1
        elif codigo != 32:
            return False
    return contador_letras >= 3

# GENERAL
def crear_matriz(cantidad_filas:int,cantidad_columnas:int,valor_inicial:any) -> list: #4
    """
    Crea una matriz (lista de listas) con un valor inicial dado.
    Args:
        cantidad_filas (int): Número de filas.
        cantidad_columnas (int): Número de columnas.
        valor_inicial (any): Valor con el que se inicializa cada elemento.
    Returns:
        list: La matriz creada.
    """
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz

# GENERAL
def validar_estructura(array: list, matriz: list, indice: int) -> bool: #5
    """
    Valida que las estructuras sean listas, no estén vacías y el índice sea válido.
    Args:
        array (list): Lista de participantes.
        matriz (list): Matriz de puntajes.
        indice (int): Índice a validar.
    Returns:
        bool: True si todo es válido, False en caso contrario.
    """
    if type(array) != list or type(matriz) != list:
        print("Error: las estructuras deben ser listas.")
        return False
    if len(array) == 0 or len(matriz) == 0:
        print("Error: las estructuras no pueden estar vacias.")
        return False
    if indice < 0 or indice >= len(array):
        print("Error: indice fuera de rango en el array.")
        return False
    if indice >= len(matriz):
        print("Error: el indice no coincide con la cantidad de filas en la matriz.")
        return False
    return True

# GENERAL
def calcular_promedio_general(matriz: list) -> float: #6
    """
    Calcula el promedio general de todos los valores de la matriz.
    Args:
        matriz (list): Matriz de puntajes.
    Returns:
        float: Promedio general.
    """
    suma_total = 0
    cantidad_total = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            suma_total += matriz[i][j]
            cantidad_total += 1
    if cantidad_total == 0:
        return 0
    promedio = suma_total / cantidad_total
    return promedio

# ESPECIFICA
def mostrar_un_participante(participantes: list, puntajes: list, indice: int) -> None: #7
    """
    Muestra el nombre y los puntajes de un participante dado su índice.
    Args:
        participantes (list): Lista de nombres.
        puntajes (list): Matriz de puntajes.
        indice (int): Índice del participante.
    """
    if not validar_estructura(participantes, puntajes, indice):
        return
    print(f"Nombre: {participantes[indice]}")
    fila = puntajes[indice]
    for i in range(len(fila)):
        print(f"Puntaje Jurado {i+1}: {fila[i]}")

# ESPECIFICA
def mostrar_participantes(participantes: list, puntajes: list) -> None: #8
    """
    Muestra todos los participantes y sus puntajes.
    Args:
        participantes (list): Lista de nombres.
        puntajes (list): Matriz de puntajes.
    """
    for i in range(len(participantes)):
        mostrar_un_participante(participantes, puntajes, i)
        print("")

# ESPECIFICA
def mostrar_participantes_con_promedios(participantes: list, puntajes: list) -> None: #9
    """
    Muestra todos los participantes, sus puntajes y su promedio individual.
    Args:
        participantes (list): Lista de nombres.
        puntajes (list): Matriz de puntajes.
    """
    for i in range(len(participantes)):
        mostrar_un_participante(participantes, puntajes, i)
        promedio = calcular_promedio_fila(puntajes, i)
        print(f"Promedio individual: {promedio:.2f}")
        print("")

# GENERAL
def calcular_promedio_fila(matriz: list, fila: int) -> float: #10
    """
    Calcula el promedio de una fila específica de la matriz.
    Args:
        matriz (list): Matriz de puntajes.
        fila (int): Índice de la fila.
    Returns:
        float: Promedio de la fila.
    """
    suma = 0
    cantidad_columnas = len(matriz[fila])
    for col in range(cantidad_columnas):
        suma += matriz[fila][col]
    if cantidad_columnas == 0:
        return 0
    promedio = suma / cantidad_columnas
    return promedio

# GENERAL
def calcular_promedio_columna(matriz: list, columna: int) -> float: #11
    """
    Calcula el promedio de una columna específica de la matriz.
    Args:
        matriz (list): Matriz de puntajes.
        columna (int): Índice de la columna.
    Returns:
        float: Promedio de la columna.
    """
    suma = 0
    cantidad_filas = len(matriz)
    for fil in range(cantidad_filas):
        suma += matriz[fil][columna]
    if cantidad_filas == 0:
        return 0
    promedio = suma / cantidad_filas
    return promedio

# ESPECIFICA
def ordenar_participantes_por_total(participantes: list, puntajes: list) -> None: #12
    """
    Ordena los participantes y sus puntajes de mayor a menor según el total de puntaje.
    Args:
        participantes (list): Lista de nombres.
        puntajes (list): Matriz de puntajes.
    """
    for izq in range(len(puntajes) - 1):
        for der in range(izq + 1, len(puntajes)):
            suma_izq = sumar_fila(puntajes, izq)
            suma_der = sumar_fila(puntajes, der)
            if suma_izq < suma_der:
                intercambiar_elementos(participantes, izq, der)
                intercambiar_elementos(puntajes, izq, der)

# GENERAL
def sumar_fila(matriz: list, fila: int) -> int: #13
    """
    Suma todos los elementos de una fila de la matriz.
    Args:
        matriz (list): Matriz de puntajes.
        fila (int): Índice de la fila.
    Returns:
        int: Suma de la fila.
    """
    suma = 0
    for col in range(len(matriz[fila])):
        suma += matriz[fila][col]
    return suma

# GENERAL
def intercambiar_elementos(array:list,izq:int,der:int) -> None: #14
    """
    Intercambia dos elementos de un array dados sus índices.
    Args:
        array (list): Lista donde se intercambian los elementos.
        izq (int): Índice del primer elemento.
        der (int): Índice del segundo elemento.
    """
    auxiliar = array[izq]
    array[izq] = array[der]
    array[der] = auxiliar

# ESPECIFICA
def ordenar_participantes_alfabeticamente(participantes: list, puntajes: list) -> None: #15
    """
    Ordena los participantes y sus puntajes alfabéticamente por nombre.
    Args:
        participantes (list): Lista de nombres.
        puntajes (list): Matriz de puntajes.
    """
    for izq in range(len(participantes) - 1):
        for der in range(izq + 1, len(participantes)):
            if participantes[izq] > participantes[der]:
                intercambiar_elementos(participantes, izq, der)
                intercambiar_elementos(puntajes, izq, der)

# ESPECIFICA
def mostrar_ganador(participantes: list, puntajes: list) -> None: #16
    """
    Muestra el ganador (o ganadores en caso de empate) según el puntaje total.
    Args:
        participantes (list): Lista de nombres.
        puntajes (list): Matriz de puntajes.
    """
    if not participantes or not puntajes:
        print("No hay participantes o puntajes para evaluar.")
        return
    totales = crear_array(len(participantes), 0)
    for i in range(len(participantes)):
        totales[i] = sumar_fila(puntajes, i)
    max_total = totales[0]
    for i in range(1, len(totales)):
        if totales[i] > max_total:
            max_total = totales[i]
    ganadores = []
    for i in range(len(participantes)):
        if totales[i] == max_total:
            ganadores += [participantes[i]]
    if len(ganadores) == 1:
        print(f"El ganador es: {ganadores[0]} con un puntaje total de {max_total}")
    else:
        print("Hay un empate entre los siguientes participantes:")
        for nombre in ganadores:
            print(f"- {nombre}")
        print("Debe realizarse un desempate.")

def desempatar(participantes: list, puntajes: list) -> None: #17
    """
    Realiza un desempate aleatorio entre los participantes empatados con el mayor puntaje.
    Args:
        participantes (list): Lista de nombres.
        puntajes (list): Matriz de puntajes.
    """
    if not participantes or not puntajes:
        print("No hay participantes o puntajes para desempatar.")
        return
    totales = crear_array(len(participantes), 0)
    for i in range(len(participantes)):
        totales[i] = sumar_fila(puntajes, i)
    max_total = totales[0]
    for i in range(1, len(totales)):
        if totales[i] > max_total:
            max_total = totales[i]
    empatados = []
    for i in range(len(participantes)):
        if totales[i] == max_total:
            empatados += [participantes[i]]
    if len(empatados) <= 1:
        print("No hay empate para desempatar.")
        return
    ganador = random.choice(empatados)
    print("Desempate realizado. El ganador elegido al azar es:")
    print(f"{ganador} con un puntaje total de {max_total}")