def obtener_temperaturas_diarias():
    
    #Función para obtener las temperaturas diarias de la semana.
    
    temperaturas = []
    for dia in range(1, 8):
        temp = float(input(f"Ingresa la temperatura del día {dia}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio_semanal(temperaturas):

#Función para calcular el promedio semanal de temperaturas.
    
    total_temp = sum(temperaturas)
    promedio_semanal = total_temp / len(temperaturas)
    return promedio_semanal

def main():
    
    #Función principal que coordina el flujo del programa.
    
    print("Bienvenido al programa de promedio semanal de temperaturas.")
    temperaturas_diarias = obtener_temperaturas_diarias()
    promedio_semanal = calcular_promedio_semanal(temperaturas_diarias)
    print(f"El promedio semanal de temperaturas es: {promedio_semanal:.2f} grados.")

if __name__ == "__main__":
    main()