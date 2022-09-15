# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import pickle

class Persona():
    def __init__(self,nom,ape,telf):
        self.nombre = nom
        self.apellido = ape
        self.telefono = telf
        

class Transaccion:
    def __init__(self,numCuen,sald,tip):
        self.numeroCuenta=numCuen
        self.valor=sald
        self.tipo=tip

class Cuenta():
    def __init__(self,numCuen,sald,propie):
        self.numeroCuenta=numCuen
        self.saldo=sald
        self.propietario=propie
        
class Principal():
    
    def __init__ (self):
        pass
    
    def CargarCuentas(self):
        lista = []
        with open("Cuentas.txt", "rb") as archivo:
            lista = pickle.load(archivo)
        archivo.close()
        return lista
    
    def CargarTransacciones(self):
        lista = []
        with open("Transacciones.txt", "rb") as archivo:
            lista = pickle.load(archivo)
        archivo.close()
        return lista
    
    def guardarCuentas(self):
        with open("Cuentas.txt", "wb") as archivo:
            pickle.dump(cuentas_list, archivo, pickle.HIGHEST_PROTOCOL)           
        archivo.close()
        
    def guardarTransaccion(self):
        with open("Transacciones.txt", "wb") as archivo:
            pickle.dump(transacciones_list, archivo, pickle.HIGHEST_PROTOCOL)           
        archivo.close()
    
    def transaccion(self,tipo):
        def transaccion_retiro(numCuenta,retiro):
            x=0
            for cuenta in cuentas_list:
                if(numCuenta==cuenta.numeroCuenta):
                    if(cuenta.saldo-retiro<=0):
                        print("No puede Retirarse esa cantidad de Dinero ya que no tiene fondos suficientes")
                    else:
                        cuenta.saldo=cuenta.saldo-retiro
                        print("\nTransaccion Realizada de tipo RETIRO\nNuevo Saldo : ",cuenta.saldo)#Se imprime tipo de transaccion y nuevo saldo
                        transaccion=Transaccion(numCuenta,retiro,"Retiro")
                        transacciones_list.append(transaccion)
                        
            
        def transaccion_deposito(numCuenta,deposito):
            x=0
            for cuenta in cuentas_list:
                if(numCuenta==cuenta.numeroCuenta):
                    cuenta.saldo=cuenta.saldo+deposito
                    print("\nTrnasaccion Realizada de tipo DEPOSITO\nNuevo Saldo : ",cuenta.saldo)#Se imprime tipo de transaccion y nuevo saldo
                    transaccion=Transaccion(numCuenta,deposito,"Deposito")
                    transacciones_list.append(transaccion)
                    x=1
            if(x==0):
                print("Cuenta no registrada")
            
        lang_func = {   "retiro":transaccion_retiro,
                        "deposito":transaccion_deposito}
        
        return lang_func[tipo]
        
    def menu(self):
        print("\n\tAplicacion Bancaria\n1) Agregar Usuario y Cuenta\n2) Listar datos de Cuentas\n3) Realizar Transaccion\n4) Listar Transacciones Realizadas en el Banco\n5) Salir")
        
    def submenu(self):
        print("\n\tTipo de transaccion\n1) Deposito\n2) Retiro\n3) Salir")
        
    def agregarCuenta(self,cuentaAgregar):
        for i in cuentas_list:
            if(cuentaAgregar.numeroCuenta==i.numeroCuenta):
                print("Cuenta ya Existente")
                return False
        cuentas_list.append(cuentaAgregar)    
        print("Cuenta Agregada Existosamente") 
        return True
    
    def validarnumero(self,numeroDig):
        if(len(numeroDig)==9):
            return True
        else:
            return False
        
    def verificarSaldo(self,saldo):
        if(saldo<=0):
            return False
        else:
            return True
        
    def listarCuentas(self):
        for cuenta in cuentas_list:
            print("Numero de Cuenta : ",cuenta.numeroCuenta,
                    "\nSaldo : ",cuenta.saldo,
                    "\nPropietario : ",cuenta.propietario.nombre," ",cuenta.propietario.apellido," ",cuenta.propietario.telefono,"\n\n")
        
    def listarTransacciones(self):
        for transaccion in transacciones_list:
            print("Numero de Cuenta = ",transaccion.numeroCuenta,"\nValor de Transaccion = ",transaccion.valor,"\nTipo de Transaccion = ",transaccion.tipo,"\n")
            
        

principal = Principal()
cuentas_list=principal.CargarCuentas()
transacciones_list=principal.CargarTransacciones()

while True:
    principal.menu()
    opc=str(input("Ingrese una opcion = "))
    #La opcion de crear usuario debe ir unida directamente con crear cuenta 
    #ya que no tendria sentido crear un usuario en una opcion y una cuenta en otra
    if(opc=="1"): 
        nombre=str(input("Ingrese nombre del Usuario = "))
        apellido=str(input("Ingrese Apellido del Usuario = "))
        telefono=str(input("Ingrese telefono del Usuario = "))
        nuevaPersona=Persona(nombre,apellido,telefono)
        if(principal.validarnumero(telefono)==True):
            numCuen = str(input("Ingrese numero numero para la Cuenta = "))
            saldo = int(input("Ingrese saldo inicial de la Cuenta = "))
            if(principal.verificarSaldo(saldo)==True):
                cuenta=Cuenta(numCuen,saldo,nuevaPersona)
                if(principal.agregarCuenta(cuenta)==True):
                    principal.guardarCuentas()
                    print("\tNuevo Usuario y Cuenta creada")
            else:
                print("\nSaldo no Valido,debe ser mayor a Cero")
        else:
            print("Numero Telefonico no valido")
    elif (opc=="2"):
        principal.listarCuentas()
    elif (opc=="3"):
        principal.submenu()
        while True:
            opc1=str(input("Ingrese una opcion = "))
            if (opc1=="1"):
                numCuent = str(input("Ingrese numero de Cuenta en la que desea depositar = "))
                deposito = int(input("Ingrese saldo a depositar = "))
                principal.transaccion("deposito")(numCuent,deposito) #en el Enunciado decia que pasa como parametro solo tipo de transaccion y cantidad pero sin numero de cuenta no es posible
                principal.guardarTransaccion()
                break
            if (opc1=="2"):
                numCuent = str(input("Ingrese numero de Cuenta de la cual desea retirar = "))
                retiro = int(input("Ingrese saldo a retirar = "))
                principal.transaccion("retiro")(numCuent,retiro)#en el Enunciado decia que pasa como parametro solo tipo de transaccion y cantidad pero sin numero de cuenta no es posible
                principal.guardarTransaccion()
                break
            if (opc1=="3"):
                break
            else:
                print("\nIngrese una opcion valida")
    elif (opc=="4"):
        principal.listarTransacciones()
    elif (opc=="5"):
        print("\nFin Programa")
        break
    else:
        print("\nIngrese una opcion valida.")
