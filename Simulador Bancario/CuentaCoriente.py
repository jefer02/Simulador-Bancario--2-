
class CuentaCoriente:
 '''# --------------------------------------------------------
     #atributos 
     ------------------------------------------#'''



saldo=0
'TuSaldoEsDe"+self.saldo"'
 
 
 
 # --------------------------------------------------------
 #metodos
#-----------------------------------------


_method_="DarSaldo"
_parameter_="Ninguno"
_returns_="SaldoDelaCuenta"
_Descripcion_="MetodoQueMuestraElsaldoDeLacuenta"  
def DarSaldo(self):
     return self._saldo







_method_="ConsignarSaldo"
_parameter_="Monto"
_returns_="ninguno"
_Descripcion_="Metodo que permite consigar un monto al cuenta coriente "
def ConsignarMonto(self,monto):
    # Aqui va mi codigo 
     self.__saldo=self.__saldo+monto






_method_="retiraSaldo"
_parameter_="monto"
_returns_="ninguno"
_Descripcion_="MetodoParaRetirarmontoDeLaCuneta"     
def RetirarSaldo(self,monto):
   # Aqui va mi codigo 
     self._saldo =self.__saldo-monto






_method_="DarCuentaCoriente"
_parameter_="ninguno "
_returns_=" cuenta corriente del simulador "
_Descripcion_="metodoParaDarlaCuentaCorriente"
def DarCuentaCoriente(self):
     return self.DarSaldo+'/'+self.SaldoDeLaCuenta




_method_="calcularSaldoDeCuenta"
_parameter_="ninguno "
_returns_="saldoDeCuenta  "
_Descripcion_="muestra al usuario el saldo de la cuenta "
def cualcularSaldoDecuemtaDeCorriente(self):
     # aqui va mi codigo 
     # forma 1 
     total= self.saldo*12
     return total

def calcularsaldodecunetacorriente(self):
     #Aqui va mi codigo
     #forma 2
     return self.saldo*12

method_="calcular"
_parameter_="ninguno "
_returns_="saldoDeCuenta  "
_Descripcion_="muestra al usuario el saldo de la cuenta "