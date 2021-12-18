# Variable Inicializador - Acumulador
total = 0
# Texti Inicial
precio = int (input ("Ingrese Precio o digite '0' (CERO) para Calcular):"))

#Ciclo que se ejecuta y suma hasta que el precio sea "0"
while (precio != 0):
    total = total + precio # acumulador
    precio = int (input ("Ingrese Precio o digite '0' (CERO) para Calcular):"))

# IF para Calculos de descuentos
if total < 50000: 
    #print ("Aplicamos descuento de 7%")
    desapp = '7 %'
    desc = total * 7 / 100
    totcdesc = total - desc

else:
    #print ("Aplicamos descuento de 12%")
    desapp = '12%'
    desc = total * 12 / 100
    totcdesc = total - desc

#Despliegue por pantalla de Resultados.
print ("Suma Precios Ingresados:", total)
print ("Descuento Logrado", desapp,  ":", round(desc))
print ("Total a Pagar (Total - Descuentos): ", round(totcdesc))

# TAP003 - S3 - ANDRES MUÑOZ CATALAN - AIEP"
