import datetime
import time
import pandas as pd
SEPARADOR = ("*" * 20) + "\n"

def menu_principal():
    print("\n- MENÚ DEL SISTEMA -")
    print("[1] Registrar una venta")
    print("[2] Consultar ventas de un día específico")
    print("[3] Exportar y Salir")
    
    
diccionario_detallesArt = {}


ciclo = True
while ciclo:
    continuar = True
    menu_principal()
    opcion = int(input("Eliga el número de la opción que desee: "))

    if opcion == 1:
        
        while continuar:
            print(SEPARADOR)
            print("\n MENÚ ARTICULOS")
            print("-DESCRIPCION-         -PRECIO-")
            print("Collar de oro          $3612")
            print("Reloj Gucci            $21343")
            print("Pendientes de plata    $1400")
            print("Cadena de plata        $2999")
            print("Anillo de oro          $7566")
            print(SEPARADOR)
                       
            descripcion_art = input("Ingrese la descripcion del articulo: ")
            print(SEPARADOR)
            cantidad_piezasVendidas = int(input("Ingrese la cantidad de piezas que se vendieron: "))
            print(SEPARADOR)
            precio_deVenta = int(input("Ingrese el precio de venta por articulo: "))    
            fecha_deVenta = datetime.date.today() 
            monto_total = (cantidad_piezasVendidas*precio_deVenta)
            diccionario_detallesArt[fecha_deVenta] = [descripcion_art,cantidad_piezasVendidas,precio_deVenta]
            print(f"El monto total a pagar es de ${monto_total}")
            print(SEPARADOR)
            print("---VENTA AGREGADA---")
            print(diccionario_detallesArt)
            print(SEPARADOR)
            seguir = int(input("¿Desea agregar otra venta? captura la clave 0 (cero) para terminar: "))
            if seguir == 0:
                continuar = False

    if opcion == 2:
        notas_ventas = pd.DataFrame(diccionario_detallesArt)
        notas_ventas.index = ["Descripcion","Cantidad_vendida_de_piezas","Precio_de_venta_Unitarios"]
        print(notas_ventas)
        print(SEPARADOR)
        fecha_consultada = input("Ingrese la fecha de la venta que desea consultar: ")
        fecha_procesada = datetime.datetime.strptime(fecha_consultada, "%d/%m/%Y").date()
        if fecha_procesada in notas_ventas:
            print(f"\n VENTAS REGISTRADAS EN {fecha_procesada}")
            print(notas_ventas[fecha_procesada])
        else:
            print("FECHA INEXISTENTE")
            
            
    elif opcion == 3:
        ciclo = False
        print("\n Procederemos a crear el archivo CSV....")
        time.sleep(5)
        notas_ventas.to_csv(r'notas_ventas.csv', index=True, header=True)
        print("-- Exportado -- \n")
        print("PROGRAMA CONCLUIDO")   