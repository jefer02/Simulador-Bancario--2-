
class CuentaDeAhorros:
 '''# --------------------------------------------------------
     #atributos 
     ------------------------------------------#'''




por=int(input('ingresa el porsentaje'))
total= int(input('ingrese el valor total' ))

resultado=total/100*por
print(f'el porsentaje es :[resultado]')
 
Numero1=int(input('ingresa el nuemro 1'))
Numero2=int(input('ingresa el nuemro 2'))

resultado2= Numero1/Numero2
print(f'el de valor [Numero1]en[Numero2], equivale al [resultado2]')






_method_="interesMensual"
_parameter_="NuevoInteresMensual"
_returns_="interesMensual"
_Descripcion_="metodoParaDarElNuevoInteresMensual"
def DarInteresMensual(self):   
    # Aqui va mi codigo 
    return self.interes_mensual


_method_="ActualizarValorPorPasoMes"
_parameter_="SaldoPorPasoMes"
_returns_="NuevoValor"
_Descripcion_="MetodoParaActualizarSaldoPorPasoMes"   
def ActualizarSaldoPorPasoMes(self):
  return self.saldo



_method_="DarDeposito"
_parameter_="ninguno"
_returns_="Dueposito"
_Descripcion_="MetodoParaDarElDeposito"
def depositar(self, NuevoDeposito):
    self.deposito+NuevoDeposito


_method_="DarRetiro"
_parameter_="ninguno"
_returns_="nuevoSaldo"
_Descripcion_="MetodoParaRetirar"   
def retirar(self, nuevoSaldo):
  self.saldo-nuevoSaldo


 
interes,mensual=30


_method_="calcularSaldoDeCuentaDeAhorros"
_parameter_="ninguno "
_returns_="saldoDeCuentaDeAharros "
_Descripcion_="muestra al usuario el saldo de la cuenta "
def cualcularSaldoDecuemtaDeCorriente(self):
     # aqui va mi codigo 
     # forma 1 
     total= self.saldo*12
     return total



_method_method_="calcularlatasasdeinteresmensual"
_parameter_="ninguno "
_returns_="tasadeinteresmensual "
_Descripcion_="muestra al usuario la tasa de interes mensual "
def calcularTasaDeInteresMensual(self):
   # Aqui inisia mi codigo
  # forma 1
  saldoecuentadeahorros=self.calcularSaldoAnual
  saldsoanual=saldsoanual*0,19
    
  #forma2
  return self.calcularSaldoAnual()*0,19






