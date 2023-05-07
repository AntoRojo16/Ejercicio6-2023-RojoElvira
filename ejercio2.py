from ClaseViajeroFrecuente import ViajeroFrecuente
from claseManejadorViajeros import Viajeros
    
if __name__=="__main__":
    lista=Viajeros()
    lista.inicializar()
    print(lista)
    numero=input("ingrese un numero de viajero frecuente")
    viajeroNuevo=lista.buscar(numero)
    opcion=0
    while opcion!=4:
       print("__MENU__")
       print("1-Consultar mayor \n2-Acumular millas \n3- Canjear millas \n4- Salir menu")
       opcion=int(input("Ingrese la opcion que desea realizar"))
       if opcion==1:
           lista.ViajerosConMayorMillas()
       if opcion==2:
           valor=int(input("Ingrese la cantidad de millas a acumular"))
           viajeroNuevo+valor
           print("La cantidad de millas se actualizo a {}".format(viajeroNuevo.getMillas()))
       if opcion==3:
           valor=int(input("Ingrese la cantidad de millas a canjear"))
           viajeroNuevo-valor
           print("La cantidad de millas se actualizo a {}".format(viajeroNuevo.getMillas()))

            


    

    
    
    