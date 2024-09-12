__author__= "jeferson morillo vallejo"
__license__="GPL"
__version__="1.0.0"
__email__="jefersonmorillo5858@gmail.com"


'''# --------------------------------------------------------
#Importaciones 
------------------------------------------#'''

from CuentaDeAhorros import CuentaDeAhorros  
from Fecha import Fecha
from CuentaCoriente import CuenraCoriente
from CDT import CDT 

class SimuladorBancario:
      
       
       
       
        # Aqui iniciamos la declaracion de la clase
     '''# --------------------------------------------------------
     #atributos 
     ------------------------------------------#'''
     __nombre=''
     __apellido=''
     __NuemeroDeDocumento=''
     __MesActual=''
    
     '''# --------------------------------------------------------
     # Asosiasiones
       ------------------------------------------#'''
     __CuentaDeAhorros=CuentaDeAhorros()
     __CuenraCoriente=CuenraCoriente()
     __CDT=CDT()
     
_method_="DepociatarCuentaCorriente"
_parameter_="metodo"
_returns_="ninguno"
_Descripcion_="metodo que permite depopsiatar en la cuenta corriente"
def DarInteresMensual(self,monto):   
    # Aqui va mi codigo 
     self.__CuentaCoriente.cosignarSaldo(monto)
     
     
     
_method_="calcularSaldoTotal"
_parameter_="ninguno"
_returns_="saldo t0tal de todas las cuentas "
_Descripcion_="metodo que permite calcular el saldo total actual de todad las cuentas "
def calcularSaldoTotal(self):
    # Aqui va mi codigo 
      def saldoCorriente(self):
      #Aqui va mi codigo 
      # metodo 1
       total= self.__cuentaCoriente.DarSaldo()+self.__CuentaAhorros.DarSaldo()
       return total
     



_method_="PasarAhorroACorriente"
_parameter_="ninguno"
_returns_="ninguno"
_Descripcion_="metodo que permite pasar saldo de la cuenta de ahorros a la cuenta corriente"
def PasarAhorrosCorriente(self):
    # Aqui va mi codigo 
    saldoAhorros=self.__cuentaAhorros.DarSaldo()
    self.__cuentaAhorros.RetirarSaldo(saldoAhorros)
    self.__cuentaCorriente.ConsignarSaldo(saldoAhorros)
    
    
_method_="pasarDeCorrienteAhorrar"
_parameter_="ninguno"
_returns_="ninguno"
_Descripcion_="metodo que permite Ahorrar en la cuenta de ahorros  "
def paasarCorrienteAhorrro (self,monto):
      # Aqui va mi codigo
      saldoCoriente= self.__cuentaCorrinete.darSaldo()
      self.__cuentaCorrinte.__retirarSaldo(saldoCoriente)
      self.__cuentaAhorros.__ConsignarSaldo(saldoCoriente)
      
      
      
      
_method_="RetirarAhorros"
_parameter_="monto"
_returns_="ninguno"
_Descripcion_="metodo que permite retirar ahorros de la cuenta "
def retirarAhorros(self,monto):
    # Aqui va mi codigo
    self.__cuentaAhorros.__RetirarValor(monto)
    
    
    



_method_="darSaldoCorriente"
_parameter_="ninguno"
_returns_="ninguno"
_Descripcion_="metodo que permite dar saldo corriente  "
def DarsaldoCorrinete(self):
   # Aqui va mi codigo 
  total= self.__cuentaCoriente.__DarSaldo()
  



_method_="duplicarSaldoDeAhorros"
_parameter_="ninguno"
_returns_="ninguno"
_Descripcion_="metodo que permite duplicar el saldo en Ahorros "
def duplicarAhorros(self):
    # Aqui va mi codigo
    self.__cuenta.ConsignarSaldo(self.__cuentaDarSaldo())



_method_="d¡DarSaldoCorriente"
_parameter_="ninguno"
_returns_="ninguno"
_Descripcion_="metodo que permite dar el saldo de la cuenta  corriente"
def darSaldoCorriete(self):
    #Aqui va mi codigo
    self.__cuentaAhorros.retirarvalor(self.__CuenetaAhorros.darDaldo())


