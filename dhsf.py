def calcular_salario(horas, valor_hora):
    if horas <= 40:
        salario = horas * valor_hora
    else:
        horas_extra = horas - 40
        salario = (40 * valor_hora) + (horas_extra * valor_hora * 2)
        print("El salario total es:", salario)


nombre = input("Ingrese su nombre: ")
horas = float(input("Ingrese sus horas trabajadas: "))
valor_hora = float(input("Ingrese el valor por hora: "))
calcular_salario(horas,valor_hora)
