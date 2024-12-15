class ClimaSemanal:
    def __init__(self):
        self.temperaturas = []  # Lista para almacenar temperaturas

    # Método para ingresar temperaturas
    def ingresar_temperaturas(self):
        print("Ingrese las temperaturas para cada día de la semana:")
        for dia in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]:
            temp = float(input(f"{dia}: "))
            self.temperaturas.append(temp)

    # Método para calcular el promedio semanal
    def calcular_promedio(self):
        if len(self.temperaturas) == 0:
            return 0  # Asegurar que haya datos
        return sum(self.temperaturas) / len(self.temperaturas)

# Programa principal
def main():
    clima = ClimaSemanal()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()
    print(f"\nEl promedio semanal de temperaturas es: {promedio:.2f}°C")

# Llamada al programa principal
if __name__ == "__main__":
    main()
