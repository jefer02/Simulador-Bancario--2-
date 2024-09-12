
class CDT:
 '''# --------------------------------------------------------
     #atributos 
     ------------------------------------------#'''



_method_ = "MontoAInvertir"
_parameter_ ="InvertirMonto"
_returns_ = "ActualizarMontoAInvertir"
_description_ ="MetodoParaInvertirMonto"
def DarMontoAInvertir(self):
    self.monto+DarMontoAInvertir




_method_ = "plazo"
_parameter_ ="TiempoPorInteres"
_returns_ = "Ninguno"
_description_ ="MetodoParaDarElPlazo"
def Plazo(self):
  return self.plazo



_method_ = "DarTasaDeInteres"
_parameter_ ="MostrarTasaDeInteres"
_returns_ = "ninguno"
_description_ ="MetodoParaVerLaTasaDeInteres"
def DarTasaDeInteres(self):
   return self.DarTasaDeInteres
 



method_="DarCDT"
_parameter_="ninguno "
_returns_=" CDT "
_Descripcion_="metodoParaDarPlazoYMontoAInvertirDelCTD"
def DarCuentaCoriente(self):
     return self.MontoInvertido+'/'+self.plazo


def calcular_cdt(capital, tasa_interes, plazo_meses):
    
    interes = capital * (tasa_interes / 100) * (plazo_meses / 12)
    monto_total = capital + interes
   
    return monto_total

