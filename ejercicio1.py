""" Un laboratorio esta evaluando el comportamiento de una sustancia respecto de la variación de la temperatura. 

Por cada medición se ingresa la temperatura registrada 
(variación posible de la temperatura de -100 a +100 grados centígrados- validar el ingreso de este dato). 
El ingreso de las temperaturas finaliza con un valor de temperatura 0.

Se pide calcular e informar:

(0,5 puntos) Porcentaje de temperaturas registradas entre 80 y 100 grados.
(1 punto) Valor de temperatura mínima registrada.
(0,5 puntos) Temperatura promedio."""

cant_temp_80_100=0
sumatoria_temp_80_100=0
temperatura_maxima=0
temperaturas=0
cant=0
temperatura=int(input("Ingresa temperatura"))
while temperatura <-100 or temperatura>100:
    temperatura=int(input("Ingresa temperatura entre -100 y 100"))

while temperatura !=0:
    cant+=1
    temperaturas+=temperatura
    if cant ==1:
        temperatura_minima=temperatura
        temperatura_maxima=temperatura
    else:
        if temperatura_maxima<temperatura:
            temperatura_maxima=temperatura
        if temperatura_minima>temperatura:
            temperatura_minima=temperatura
    if temperatura>=80 and temperatura<=100:
        cant_temp_80_100+=1
        sumatoria_temp_80_100+=temperatura
        
        
    temperatura=int(input("Ingresa temperatura"))
    while temperatura <-100 or temperatura>100:
        temperatura=int(input("Ingresa temperatura"))


promedio=temperaturas/cant
porcentaje_temp_80_100=(cant_temp_80_100//cant)*100

print("Porcentaje de la temperatura entre 80 y 100: ",porcentaje_temp_80_100,"%")      
print("Valor de temperatura mínima registrada: ",temperatura_minima)
print("Temperatura promedio: ",promedio)
