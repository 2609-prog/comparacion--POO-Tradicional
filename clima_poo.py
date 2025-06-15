class ClimaSemanal:
    def __init__(self):
        # Lista para almacenar las temperaturas diarias
        self._temperaturas = []

    def ingresar_temperatura(self, temperatura):
        # Encapsulación: método para agregar temperatura diaria
        if len(self._temperaturas) < 7:
            self._temperaturas.append(temperatura)
        else:
            print("Ya se han ingresado 7 temperaturas.")

    def calcular_promedio(self):
        # Cálculo del promedio semanal
        if len(self._temperaturas) == 0:
            return 0
        return sum(self._temperaturas) / len(self._temperaturas)

    def mostrar_promedio(self):
        promedio = self.calcular_promedio()
        print(f"El promedio semanal de temperatura es: {promedio:.2f}°C")

def main():
    print("=== Promedio semanal del clima (POO) ===")
    clima = ClimaSemanal()

    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
        clima.ingresar_temperatura(temp)

    clima.mostrar_promedio()

if __name__ == "__main__":
    main()
    