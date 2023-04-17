#coding=utf-8

class RondaAbiertaExcesoBolas(Exception):
    message = "Hay más de dos bolas en una ronda abierta"

class RondaStrikeExcesoBolas(Exception):
    message = "Hay más de una bola en una ronda abierta"

class SignoStrikeMalUsado(Exception):
    message = "No es un strike válido, esto es un spare"

class RondaStrikeInvalida(Exception):
    message = "Exceso de bolas y colocado en una posición inválida"

class SignoSpareMalUsado(Exception):
    message = "No puede haber un spare en la primera posición de la ronda"

class SignoSpareMalUsado2(Exception):
    message = "No es un spare válido, esto es un strike"

class SumaRondaMasDeDiez(Exception):
    message = "Las bolas de una ronda no pueden sumar más de diez"

class NumeroRondasDistintoDiez(Exception):
    message = "Número de rondas no válido"

class RondaSpareExcesoBolas(Exception):
    message = "Hay más de dos bolas en una ronda spare"    

class RondaNoDefinida(Exception):
    message = "Esta ronda no se corresponde con strike, spare o abierta"

class RondaUltimaStrikeNoValida(Exception):
    message = "Esta ronda última ronda strike no tiene el formato válido" 

class RondaUltimaSpareNoValida(Exception):
    message = "Esta ronda última ronda spare no tiene el formato válido"      

class Bolos: 
    rondas = []
    size = 0
    puntuacion = 0

    def calcularTamanno(self, partida):
        self.rondas = partida.split()
        self.size = len(self.rondas)
        return self.size
    
    def comprobarStrike(self, ronda):
        if (len(ronda)>1):
            if (ronda[0]=="X"):
                raise RondaStrikeExcesoBolas()
            elif (ronda[1]=="X"):
                raise SignoStrikeMalUsado()
            else:
                raise RondaStrikeInvalida()
        else: 
            return True

    def comprobarSpare(self, ronda):
        if (ronda[0]=="/" and len(ronda)>1):
            raise SignoSpareMalUsado()
        elif (ronda[0]=="/" and len(ronda)==1):
            raise SignoSpareMalUsado2()
        elif (len(ronda)!=2):
            raise RondaSpareExcesoBolas()
        else: 
            return True
    
    def comprobarRondaAbierta(self, ronda):
        if (len(ronda)!=2):
            raise RondaAbiertaExcesoBolas() 
        elif (int(ronda[0]) + int(ronda[1])>10):
            raise SumaRondaMasDeDiez()
        else: 
            return True

    def comprobarUltimoStrike(self, ronda):
        if (len(ronda)!=3 or ronda[1]=="/" or (ronda[1]=="X" and ronda[2]=="/")):
            raise RondaUltimaStrikeNoValida()
        else:
            return True

    def comprobarUltimoSpare(self, ronda):
        if (len(ronda)!=3 or ronda[2]=="/"):
            raise RondaUltimaSpareNoValida()
        else:
            return True

    def comprobarUltimaRonda(self, ronda):
        if ('X' in ronda and 'X' == ronda[0]):
            self.comprobarUltimoStrike(ronda)
        elif ('/' in ronda and '/' == ronda[1]):
            self.comprobarUltimoSpare(ronda)
        elif ('X' not in ronda and '/' not in ronda and ronda.isdigit()):
            self.comprobarRondaAbierta(ronda)
        else: 
            raise RondaNoDefinida()
    
    def comprobarRonda(self, indice, ronda):
        if (indice == 9):
            self.comprobarUltimaRonda(ronda)
        elif ('X' in ronda):
            self.comprobarStrike(ronda)
        elif ('/' in ronda):
            self.comprobarSpare(ronda)
        elif ('X' not in ronda and '/' not in ronda and ronda.isdigit()):
            self.comprobarRondaAbierta(ronda)
        else:   
            raise RondaNoDefinida()

    def __init__(self, partida):
        if (self.calcularTamanno(partida)==10):
            for indice, ronda in enumerate(self.rondas):
                self.comprobarRonda(indice, ronda)
        else:
            raise NumeroRondasDistintoDiez()

    def calcularPuntuacionStrike(self, indice):
        if (self.rondas[indice+1][0]=="X"):
            if (self.rondas[indice+2][0]=="X"):
                self.puntuacion += 30
            else: 
                self.puntuacion += 20 + int(self.rondas[indice+2][0])
        elif (self.rondas[indice+1][1]=="/"):
            self.puntuacion += 20
        else: 
            self.puntuacion += 10 + int(self.rondas[indice+1][0]) + int(self.rondas[indice+1][1])       
    
    def calcularPuntuacionStrikeUltimaRonda(self, ronda):
        if (ronda[1]=="X"):
            if (ronda[2]=="X"):
                self.puntuacion += 30
            else: 
                self.puntuacion += 20 + int(ronda[2])
        elif (ronda[2]=="/"):
            self.puntuacion += 20
        else:
            self.puntuacion += 10 + int(ronda[1]) + int(ronda[2])   
    
    def calcularPuntuacionSpare(self, index):
        if (self.rondas[index+1][0]=="X"):
            self.puntuacion += 20
        else:
            self.puntuacion += 10 + int(self.rondas[index+1][0])

    def calcularPuntuacionSpareUltimaRonda(self, ronda):
        if (ronda[2]=="X"):
            self.puntuacion += 20
        else:
            self.puntuacion += 10 + int(ronda[2])
    
    def calcularPuntuacionAbierta(self, ronda):
        self.puntuacion += int(ronda[0]) + int(ronda[1])     

    def calcularPuntuacionUltimaRonda(self, ronda):
        if (ronda[0]=="X"):
            self.calcularPuntuacionStrikeUltimaRonda(ronda)
        elif (ronda[1]=="/"):
            self.calcularPuntuacionSpareUltimaRonda(ronda)
        else: 
            self.calcularPuntuacionAbierta(ronda)

    def calcularPuntuacion(self):
        for index, ronda in enumerate(self.rondas):
            if (index == 9):
                self.calcularPuntuacionUltimaRonda(ronda)
            elif (ronda[0] == "X"):
                self.calcularPuntuacionStrike(index)
            elif (ronda[1]=="/"): 
                self.calcularPuntuacionSpare(index)
            else:
                self.calcularPuntuacionAbierta(ronda)
        return self.puntuacion  