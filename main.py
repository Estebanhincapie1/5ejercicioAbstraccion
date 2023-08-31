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
    def NuevaVisita(self, j):
        self.__visitas[j.VerFechaVisita()] = j

    def VerNombre(self):
        return self.__nombre
    def VerCedula(self):
        return self.__cedula
    def VerGenero(self):
        return self.__genero
    def VerVisitas(self):
        return self.__visitas
    

class Visita():
    def __init__(self) -> None:
        self.__fechaVisita  = '' #datetime
        self.__registroEncefalografico = ''
        self.__notas  = ''

    def AsignarFechaVisita(self, f):
        self.__fechaVisita = f
    def AsignarRuta(self, r):
        self.__registroEncefalografico= r
    def AsignarNotas(self, no):
        self.__notas = no

    def VerFechaVisita(self):
        return self.__fechaVisita
    def VerRuta(self):
        return self.__registroEncefalografico
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
        self.__RegistroPacientes = {}
    #FUNCION PARA AGREGAR NUEVO PACIENTE
    def nuevoPaciente(self,j):
        self.__RegistroPacientes[j.VerCedula()] = j
     
    def VerSistema(self):
        return self.__RegistroPacientes
    


p1 = Persona()
nombre = 'juan'
cedula = 1041440201
genero = 'm'

visita = 12/12/2023
notas = 'Eta aliviado'
ruta = 'ESTA ES LA RUTA DE PRUEBA'

delta  = 0
theta  = 0
alfa1  = 0
alfa2  = 0
beta   = 0
gamma  = 0

p1.AsignarCedula(cedula)
p1.AsignarNombre(nombre)
p1.AsignarGenero(genero)

vis = Visita()
vis.AsignarRuta(ruta)
vis.AsignarFechaVisita(visita)
vis.AsignarNotas(notas)

indices = Indices()
indices.asignarPDELTA(delta)
indices.asignarPTHETA(theta)
indices.asignarPALFA1(alfa1)
indices.asignarPALFA2(alfa2)
indices.asignarPBETA(beta)
indices.asignarPGAMMA(gamma)

sis1 = Sistema()
sis1.nuevoPaciente(p1)

conVisitas = (str(vis.VerFechaVisita() +'RUTA: '+ vis.VerRuta()+ ' ' +'NOTAS: '+ vis.VerNotas()))
indi = str('POTENCIAL DELTA: '+ str(indices.VerPDELTA()) + 'POTENCIAL THETA: '+ str(indices.VerPTHETA())+'POTENCIAL ALFA1: '+ str(indices.VerPALFA1())+ '\n'+'POTENCIAL ALFA2: '+str(indices.VerPALFA2())+ '\n' + 'POTENCIAL BETA: '+ str(indices.VerPBETA())+ '\n' +'POTENCIAL GAMMA: '+ str(indices.VerPGAMMA())+ '\n')

# with open('ListaPacientes.txt', 'a') as archivo:
#     contenido = str("CC: " + str(p1.VerCedula()) +' '+ 'NOMBRE: '+ p1.VerNombre() +' '+ "GENERO :"+ p1.VerGenero())
#     archivo.write(contenido + "\n")


