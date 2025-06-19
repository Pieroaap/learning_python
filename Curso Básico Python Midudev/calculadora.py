def calculadora():
    bienvenida = "Bienvenido a la calculadora \nPara salir escribre Salir \nLas operaciones que puedes realizas son suma, multi, div y resta"
    print(bienvenida)
    resultado = ""
    while True:
        if not resultado:
            resultado = input("Ingrese un número: ")
            if resultado.lower() == 'salir':
                print("Adios")
                break
            resultado = int(resultado)
        op = input("Ingrese la operación que desea realizar: ")
        if op.lower() == 'salir':
            print("Adios")
            break
        n2 = input("Ingrese otro número: ")
        if(op.lower() == 'suma'):
            resultado += int(n2)
        elif(op.lower() == 'resta'):
            resultado -= int(n2)
        elif(op.lower() =='multi'):
            resultado *= int(n2)
        elif(op.lower() == 'div'):
            resultado /= int(n2)
        else:
            print("Operación no válida")
            break

        print(f"El resultado es: {resultado}")

calculadora()

