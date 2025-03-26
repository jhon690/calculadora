procesado = None

while not procesado:
    try:
        print(f"1. SUMA\n2. RESTA\n3. MULTIPLICACIÓN\n4. DIVISIÓN" )
        tipo_matematica = int(input("Ingrese el número del tipo de acción que quiere realizar: "))
        if 1 <= tipo_matematica <= 4:
            numero1 = int(input("Ingrese el primer numero: "))
            numero2 = int(input("Ingrese el segundo numero: "))
            procesado = True
        else:
            print("El numero ingresado no existe, intente nuevamente.")
    except:
        print("El dato ingresado no es un numero, intente de nuevo") 


resultado = None

# Verificar el tipo de operación seleccionada
if tipo_matematica == 1:
    resultado = numero1 + numero2
    print(f"La suma entre los numeros: {numero1} y {numero2} es: {resultado}")
elif tipo_matematica == 2:
    resultado = numero1 - numero2
    print(f"La resta entre los numeros: {numero1} y {numero2} es: {resultado}")
elif tipo_matematica == 3:
    resultado = numero1 * numero2
    print(f"La multiplicación entre los numeros: {numero1} y {numero2} es: {resultado}")
elif tipo_matematica == 4:
    if numero2 != 0 and numero1 != 0:
        resultado = numero1 // numero2
        print(f"La división entre los numeros: {numero1} y {numero2} es: {resultado}")


# Solo mostrar todos los procesos si la operación es válida
respuesta = int(input(f"¿Quieres ver el resultados de todas las opreaciones? Escribre 1 para si o 0 para no\n"))

if respuesta == 1:
    if tipo_matematica in [1, 2, 3, 4]:
        if numero2 != 0 and numero1 != 0: 
            print(f"La suma es: {numero1 + numero2} \nla resta es: {numero1 - numero2}\n la multiplicación es: {numero1 * numero2}\n la división es:  { numero1 // numero2}")  
        else:
            print(f"No se puede divir los numero {numero1} y {numero2}")
else:
    print("Fin de calculadora")
