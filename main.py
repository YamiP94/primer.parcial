import funciones

funciones.mostrar_menu
funciones.cargar_pacientes
funciones.mostrar_pacientes
funciones.buscar_paciente
funciones.ordenar_pacientes
funciones.paciente_mas_dias
funciones.paciente_menos_dias
funciones.pacientes_mas_cinco_dias
funciones.promedio_dias_internacion

# Menú interactivo dentro de bucle para avanzar con las opciones

while True:
    funciones.mostrar_menu()
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        funciones.cargar_pacientes()
    elif opcion == "2":
        funciones.mostrar_pacientes()
    elif opcion == "3":
        funciones.buscar_paciente()
    elif opcion == "4":
        funciones.ordenar_pacientes()
    elif opcion == "5":
        funciones.paciente_mas_dias()
    elif opcion == "6":
        funciones.paciente_menos_dias()
    elif opcion == "7":
        funciones.pacientes_mas_cinco_dias()
    elif opcion == "8":
        funciones.promedio_dias_internacion()
    elif opcion == "9":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida, intenta de nuevo.")
        
        