def calculadora():
    bienvenida = "Bienvenido a la calculadora \nPara salir escribre Salir \nLas operaciones que puedes realizas son suma, multi, div y resta"
    print(bienvenida)
    n1 = input("Ingrese un número: ")
    if(n1 == 'Salir'):
        print("Adios")
        return
    else:
        n2 = input("Ingrese otro número: ")
        operacion = input("Ingrese la operación que desea realizar: ")
        if(operacion == 'suma'):
            print("El resultado de la suma es: ", float(n1) + float(n2))
        elif(operacion == 'resta'):
            print("El resultado de la resta es: ", float(n1) - float(n2))
        elif(operacion == 'multi'):
            print("El resultado de la multiplicación es: ", float(n1) * float(n2))
        elif(operacion == 'div'):
            print("El resultado de la división es: ", float(n1) / float(n2))
        else:
            print("Operación no válida")

calculadora()

