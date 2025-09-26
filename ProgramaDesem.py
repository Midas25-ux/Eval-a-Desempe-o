afirmacion = True
Bienvenida = "Comencemos a gestionar los perfiles de tus colaboradores y su desempeño"
colaboradores_proyecto = []  
Menu = """
-------------------------------------------------
|                                               |
           Gestor de Desempeño de Empleados     |
|-----------------------------------------------|
|                                               |
|           1. Registrar desempeño del empleado |
|           2. Calcular promedio de desempeño   |
|           3. Clasificar desempeño             |
|           4. Mostrar reporte final            |
|           5. Salir                            |
|-----------------------------------------------|
"""


def registrar_desempeño():
    print("Ha seleccionado la opción 1: Registrar desempeño del empleado")
    nombre = input("Nombre del empleado: ")
    calidad = float(input("calidad (0-10): "))
    puntualidad = float(input("puntualidad (0-10): "))
    colaboracion = float(input("colaboración (0-10): "))
    eficiencia = float(input("eficiencia (0-10): "))
    
   
    desempeño = (calidad, puntualidad, colaboracion, eficiencia)
    empleado = {
        "nombre": nombre,
        "desempeno": desempeño
    }
    colaboradores_proyecto.append(empleado)
    print(f"Desempeño registrado para {nombre}.")


def calcular_promedio():
    print("Ha seleccionado la opción 2: Calcular promedio de desempeño")
    for empleado in colaboradores_proyecto:
        promedio = sum(empleado["desempeno"]) / len(empleado["desempeno"])
        print(f"{empleado['nombre']} - Promedio: {promedio:.2f}")


def clasificar_desempeño():
    print("Ha seleccionado la opción 3: Clasificar desempeño")
    for empleado in colaboradores_proyecto:
        promedio = sum(empleado["desempeno"]) / len(empleado["desempeno"])
        if promedio >= 8.5:
            estado = "Sobresaliente"
        elif promedio >= 5:
            estado = "Aceptable"
        else:
            estado = "Bajo"
        empleado["estado"] = estado
        print(f"{empleado['nombre']} - Estado: {estado}")


def mostrar_reporte():
    print("Ha seleccionado la opción 4: Mostrar reporte final")
    if not colaboradores_proyecto:
        print("No hay empleados registrados.")
    else:
        print("Reporte Final de Desempeño:")
        for empleado in colaboradores_proyecto:
            print("Nombre:", empleado['nombre'], "Desempeño:", empleado['desempeno'])
    u''
while afirmacion:
    print(Menu)
    opcion = input("Seleccione una opción (1-5): ")

    if opcion == "1":
        registrar_desempeño()
    elif opcion == "2":
        calcular_promedio()
    elif opcion == "3":
        clasificar_desempeño()
    elif opcion == "4":
        mostrar_reporte()
    elif opcion == "5":
        print("Gracias por usar nuestro sistema de gestión de desempeño de empleados. ¡Hasta pronto!")
        afirmacion = False
    else:
        print("Opción inválida. Intente nuevamente.")
