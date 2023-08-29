print('Bienvenido')

class Persona:
    def __init__(self) -> None:
        self.__nombre   = ''
        self.__cedula    = 0
        self.__genero   = ''
        self.__visitas = {}
    
    def AsignarNombre(self, n):
        self.__nombre = n
    def AsignarCedula(self,c):
        self.__cedula= c
    def AsignarGenero(self, g):
        self.__genero = g

    def VerNombre(self):
        return self.__nombre
    def VerCedula(self):
        return self.__cedula
    def VerGenero(self):
        return self.__genero
    

class Visita():
    def __init__(self) -> None:
        self.__fechaVisita  = '' #datetime
        self.registroEncefalografico = ''
        self.__notas  = ''

    def AsignarFechaVisita(self, f):
        self.__fechaVisita = f
    def AsignarRuta(self, r):
        self.registroEncefalografico= r
    def AsignarNotas(self, no):
        self.__notas = no

    def VerFechaVisita(self):
        return self.__fechaVisita
    def VerRuta(self):
        return self.__fechaVisita
    def VerNotas(self):
        return self.__notas


class Indices:
    def __init__(self) -> None:
        self.__pDELTA   = 0
        self.__pTHETA   = 0
        self.__pALFA1   = 0
        self.__pALFA2   = 0 
        self.__pBETA    = 0   
        self.__pGAMMA   = 0   
    
    def asignarPDELTA(self, n):
        self.__pDELTA = n
    def asignarPTHETA(self, n):
        self.__pTHETA = n
    def asignarPALFA1(self, n):
        self.__pALFA1 = n
    def asignarPALFA2(self, n):
        self.__pALFA2 = n
    def asignarPBETA(self, n):
        self.__pBETA = n
    def asignarPGAMMA(self, n):
        self.__pGAMMA = n

    def VerPDELTA(self):
        return self.__pDELTA
    def VerPTHETA(self):
        return self.__pTHETA
    def VerPALFA1(self):
        return self.__pALFA1
    def VerPALFA2(self):
        return self.__pALFA2
    def VerPBETA(self):
        return self.__pBETA
    def VerPGAMMA(self):
        return self.__pGAMMA
    
class Sistema:
    def __init__(self) -> None:
        self.__RegistroPacientees = {}

        def nuevoPaciente(self,j):


 i = Persona()
nombre = 'juan'
cedula = 1041440201
genero = 'm'

p1.AsignarCedula(cedula)
p1.AsignarNombre(nombre)
p1.AsignarGenero(genero)

