""" Una empresa cuenta con 10 empleados. 
Por cada empleado se ingresa legajo, sueldo básico (valor mayor a 150000$. Validar el ingreso de este dato) 
y antigüedad, 
siendo que los empleados con antigüedad mayor o igual a 10 años cobran un adicional de 10% 
y si la antigüedad supera los 25 años cobran el doble del sueldo básico.

Se pide informar:

(1 punto) Informar el sueldo a cobrar por empleado
(1 punto) Total de sueldos que abona la empresa"""


total_sueldo=0
for i in range (10):
    legajo=int(input("Ingresar legajo"))
    sueldo=float(input("Ingresar sueldo"))
    while sueldo <150000:
        sueldo=float(input("Ingresar sueldo"))
    antiguedad=int(input("Ingresa antiguedad en anios"))

    if antiguedad>=10 and antiguedad<=25:
        sueldo+=(sueldo*0.10)

    if antiguedad>25:
        sueldo+=sueldo
    total_sueldo+=sueldo
    print("Sueldo a cobrar: ",sueldo)

print("Total de sueldos que abona la empresa: ",total_sueldo)
