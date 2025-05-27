# Lista anidada para almacenar los pacientes
pacientes = []

# Función para mostrar el menú
def mostrar_menu():
    print("\nMenú Interactivo - Sistema de Gestión de Pacientes")
    print("1. Cargar pacientes")
    print("2. Mostrar lista de pacientes")
    print("3. Buscar paciente por historia clínica")
    print("4. Ordenar pacientes por número de historia clínica")
    print("5. Paciente con más días de internación")
    print("6. Paciente con menos días de internación")
    print("7. Cantidad de pacientes con más de 5 días de internación")
    print("8. Promedio de días de internación")
    print("9. Salir")

# Función para cargar pacientes
def cargar_pacientes():
    cantidad = int(input("Ingrese la cantidad de pacientes a registrar: "))
    nuevos_pacientes = []  # Lista temporal para almacenar los pacientes ingresados

    for _ in range(cantidad):
        historia = int(input("Número de historia clínica: "))
        nombre = input("Nombre del paciente: ")
        edad = int(input("Edad del paciente: "))
        diagnostico = input("Diagnóstico: ")
        dias = int(input("Cantidad de días de internación: "))

        nuevos_pacientes += [[historia, nombre, edad, diagnostico, dias]] 

    pacientes[:] = pacientes + nuevos_pacientes  
    print("Pacientes cargados correctamente.")


# Función para mostrar todos los pacientes
def mostrar_pacientes():
    if not pacientes:
        print("No hay pacientes registrados.")
        return
    print("\nLista de Pacientes:")
    for paciente in pacientes:
        print(f"Historia: {paciente[0]}, Nombre: {paciente[1]}, Edad: {paciente[2]}, Diagnóstico: {paciente[3]}, Días Internación: {paciente[4]}")

# Función para buscar un paciente por historia clínica
def buscar_paciente():
    """
    Usa -if not pacientes- para comprobar si la lista está vacía.
    Si no hay pacientes, muestra "No hay pacientes registrados." y termina la ejecución con return.
    Caso contrio, utiliza -for paciente in pacientes- para recorer la listaa y retonar los datos de la lista. 
    """
    if not pacientes:
        print("No hay pacientes registrados.")
        return
    historia = int(input("Ingrese el número de historia clínica a buscar: "))
    for paciente in pacientes:
        if paciente[0] == historia:
            print(f"Paciente encontrado: {paciente}")
            return
    print("Paciente no encontrado.")

# Función para ordenar pacientes por historia clínica
def ordenar_pacientes():
    """
    Usa -if not pacientes- para comprobar si la lista pacientes está vacía.
    Si no hay pacientes, muestra un mensaje y retorna, evitando errores. 
    Caso contario organiza la lista en orden ascendente
    """
    if not pacientes:
        print("No hay pacientes registrados.")
        return
    
    n = len(pacientes)
    for i in range(n):
        for j in range(0, n-i-1):
            if pacientes[j][0] > pacientes[j+1][0]: 
                pacientes[j], pacientes[j+1] = pacientes[j+1], pacientes[j]

    print("Pacientes ordenados correctamente.")

# Función para determinar paciente con más días de internación
def paciente_mas_dias():
    """
    La funcion recorre la lista completa usando un for y compara los días de internación. Si encuentra un paciente con más días, lo actualiza en paciente_max.
    Retornar el paciente con más días de internación.
    """
    if not pacientes:
        print("No hay pacientes registrados.")
        return
    
    paciente_max = pacientes[0]
    for paciente in pacientes:
        if paciente[4] > paciente_max[4]:  
            paciente_max = paciente
    
    print("Paciente con más días de internación:", paciente_max)
    
    
# Función para determinar paciente con menos días de internación
def paciente_menos_dias():
    """
    La funcion recorre la lista completa usando un for y compara los días de internación. Si encuentra un paciente con menos días, lo actualiza en paciente_min.
    Retornar el paciente con menor días de internación.
    """
    if not pacientes:
        print("No hay pacientes registrados.")
        return
    
    paciente_min = pacientes[0]  
    for paciente in pacientes:
        if paciente[4] < paciente_min[4]:  
            paciente_min = paciente  
    
    print("Paciente con menos días de internación:", paciente_min)

# Función para contar pacientes con más de 5 días de internación
def pacientes_mas_cinco_dias():
    if not pacientes:
        print("No hay pacientes registrados.")
        return
    
    cantidad = 0  # 
    for paciente in pacientes:
        if paciente[4] > 5:
            cantidad += 1 
    
    print(f"Cantidad de pacientes con más de 5 días de internación: {cantidad}")

# Función para calcular el promedio de días de internación
def promedio_dias_internacion():
    """
    La funcion recorre la lista pacientes y sumas los días de internacion. Calcula el promedio diviendo total de dias entre cantidad de pacientes
    """
    if not pacientes:
        print("No hay pacientes registrados.")
        return
    
    total_dias = 0  
    cantidad_pacientes = 0 
    
    for paciente in pacientes:
        total_dias += paciente[4]  
        cantidad_pacientes += 1  
    
    promedio = total_dias / cantidad_pacientes  # Calculamos el promedio
    print(f"Promedio de días de internación: {promedio:.2f}")
