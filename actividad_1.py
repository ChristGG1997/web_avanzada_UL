# en una playa de estacionamiento cobran  $2.00 por hora o por fraccion los dias lunes , martes y miercoles ,
# $2.50 los dias jueves y viernes,  $3.00 los sabados y domingos. se considera una fraccion de hora cuando 
# haya pasado 5 minutos. diseñe un programa que determine cuanto debe pagar un cliente por su estacionamiento 
# en un solo dia de la semana. si le tiempo es incorrecto imprima un mensaje de error.

def calcular_pago(horas, minutos, dia_semana):
    if dia_semana in ["lunes", "martes", "miércoles"]:
        tarifa = 2.00
    elif dia_semana in ["jueves", "viernes"]:
        tarifa = 2.50
    elif dia_semana in ["sábado", "domingo"]:
        tarifa = 3.00
    else:
        print("Día de la semana incorrecto")
        return

    tiempo_total = horas + minutos / 60

    if minutos % 5 != 0:
        tiempo_total = round(tiempo_total) + 1

    total_pagar = tarifa * tiempo_total
    print(f"El total a pagar es: ${total_pagar:.2f}")

# Obtener datos de entrada
horas = int(input("Ingrese las horas estacionadas: "))
minutos = int(input("Ingrese los minutos estacionados: "))
dia_semana = input("Ingrese el día de la semana: ").lower()

calcular_pago(horas, minutos, dia_semana)
