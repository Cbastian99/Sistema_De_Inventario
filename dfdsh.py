def puede_votar(edad):
    if edad >= 18:
        return "Puede Votar"
    else:
        return "No puede votar"
    


nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

puede_votar(edad)
