#coding=utf-8
import unittest
from Bolos import *

class TestBolos(unittest.TestCase):
    def test_diez_rondas(self):
        partida = Bolos("00 00 00 00 00 00 00 00 00 00")
        self.assertEquals(10, partida.size, "No coincide el número de rondas")
    
    def test_nueve_rondas(self):
        with self.assertRaises(NumeroRondasDistintoDiez): 
            partida = Bolos("00 00 00 00 00 00 00 00 00")

    def test_doce_rondas(self):
        with self.assertRaises(NumeroRondasDistintoDiez): 
            partida = Bolos("00 00 00 00 00 00 00 00 00 00 00 00")
    
    def test_ronda_numerica(self):
        partida = Bolos("14 00 00 00 00 00 00 00 00 00")
        self.assertEqual(5, partida.calcularPuntuacion(), "La puntuación no coincide")

    def test_ronda_numerica_2(self):
        partida = Bolos("25 00 00 00 00 00 00 00 00 00")
        self.assertEqual(7, partida.calcularPuntuacion(), "La puntuación no coincide")

    def test_ronda_numerica_3(self):
        partida = Bolos("25 43 00 00 00 00 00 00 00 00")
        self.assertEqual(14, partida.calcularPuntuacion(), "La puntuación no coincide")

    def test_ronda_numerica_4(self):
        partida = Bolos("25 43 21 71 00 00 00 00 00 00")
        self.assertEqual(25, partida.calcularPuntuacion(), "La puntuación no coincide")
    
    def test_ronda_numerica_completa(self):
        partida = Bolos("32 43 62 54 34 23 14 61 43 70")
        self.assertEqual(67, partida.calcularPuntuacion(), "La puntuación no coincide")
    
    def test_ronda_strike(self):
        partida = Bolos("X 00 00 00 00 00 00 00 00 00")
        self.assertEqual(10, partida.calcularPuntuacion(), "La puntuación no coincide")

    def test_ronda_strike_2(self):
        partida = Bolos("X 12 00 00 00 00 00 00 00 00")
        self.assertEqual(16, partida.calcularPuntuacion(), "La puntuación no coincide")

    def test_ronda_strike_invalido(self):
        with self.assertRaises(RondaStrikeExcesoBolas):
            partida = Bolos("X7 12 00 00 00 00 00 00 00 00")
    
    def test_ronda_strike_invalido_2(self):
        with self.assertRaises(SignoStrikeMalUsado):
            partida = Bolos("7X 12 00 00 00 00 00 00 00 00")
    
    def test_ronda_strike_invalido_3(self):
        with self.assertRaises(RondaStrikeExcesoBolas):
            partida = Bolos("72 12 X3 00 00 00 00 00 00 00")

    def test_ronda_strike_invalido_4(self):
        with self.assertRaises(SignoStrikeMalUsado):
            partida = Bolos("72 12 7X 00 00 00 00 00 00 00")
    
    def test_ronda_strike_invalido_5(self):
        with self.assertRaises(RondaStrikeInvalida):
            partida = Bolos("72 12 73X 00 00 00 00 00 00 00")

    def test_ronda_strike_3(self):
        partida = Bolos("X 63 00 00 00 00 00 00 00 00")
        self.assertEqual(28, partida.calcularPuntuacion(), "La puntuación no coincide")

    def test_dos_strike_seguidos(self):
        partida = Bolos("X X 54 00 00 00 00 00 00 00")
        self.assertEqual(53, partida.calcularPuntuacion(), "La puntuación no coincide")

    def test_tres_strike_seguidos(self):
        partida = Bolos("X X X 24 00 00 00 00 00 00")
        self.assertEqual(74, partida.calcularPuntuacion(), "La puntuación no coincide")
    
    def test_cinco_strike_seguidos(self):
        partida = Bolos("X X X X X 54 00 00 00 00")
        self.assertEqual(143, partida.calcularPuntuacion(), "La puntuación no coincide")

    def test_strike_aleatorios(self):
        partida = Bolos("X X 30 X X X 02 X 43 21")
        self.assertEqual(130, partida.calcularPuntuacion(), "La puntuación no coincide")
    
    def test_ronda_spare(self):
        partida = Bolos("9/ 63 00 00 00 00 00 00 00 00")
        self.assertEqual(25, partida.calcularPuntuacion(), "La puntuación no coincide")
    
    def test_ronda_spare_2(self):
        partida = Bolos("4/ 31 00 00 00 00 00 00 00 00")
        self.assertEqual(17, partida.calcularPuntuacion(), "La puntuación no coincide")
    
    def test_spare_strike(self):
        partida = Bolos("4/ X 12 00 00 00 00 00 00 00")
        self.assertEqual(36, partida.calcularPuntuacion(), "La puntuación no coincide")
    
    def test_dos_spare(self):
        partida = Bolos("4/ 7/ 42 00 00 00 00 00 00 00")
        self.assertEqual(37, partida.calcularPuntuacion(), "La puntuación no coincide")
    
    def test_strike_spare(self):
        partida = Bolos("X 7/ 42 00 00 00 00 00 00 00")
        self.assertEqual(40, partida.calcularPuntuacion(), "La puntuación no coincide")
    
    def test_dos_strike_spare(self):
        partida = Bolos("X X 2/ 43 00 00 00 00 00 00")
        self.assertEqual(63, partida.calcularPuntuacion(), "La puntuación no coincide")
    
    def test_tres_strike_spare(self):
        partida = Bolos("X X X 2/ 43 00 00 00 00 00")
        self.assertEqual(93, partida.calcularPuntuacion(), "La puntuación no coincide")
    
    def test_strike_spare_mezclados(self):
        partida = Bolos("X X X 2/ X 9/ 32 00 00 00")
        self.assertEqual(130, partida.calcularPuntuacion(), "La puntuación no coincide")

    def test_strike_spare_mezclados_2(self):
        partida = Bolos("X X X 2/ X 9/ 32 X 2/ 00")
        self.assertEqual(160, partida.calcularPuntuacion(), "La puntuación no coincide")
    
    def test_ronda_spare_invalido(self):
        with self.assertRaises(SignoSpareMalUsado):
            partida = Bolos("61 42 23 /2 00 00 00 00 00 00")
    
    def test_ronda_spare_invalido_2(self):
        with self.assertRaises(SignoSpareMalUsado2):
            partida = Bolos("61 42 23 / 00 00 00 00 00 00")
    
    def test_ronda_spare_invalido_3(self):
        with self.assertRaises(RondaSpareExcesoBolas):
            partida = Bolos("61 42 23 2/3 00 00 00 00 00 00")
    
    def test_ronda_numerica_invalida(self):
        with self.assertRaises(SumaRondaMasDeDiez):
            partida = Bolos("61 42 23 78 00 00 00 00 00 00")
    
    def test_ronda_numerica_invalida_2(self):
        with self.assertRaises(RondaAbiertaExcesoBolas):
            partida = Bolos("61 42 23 123 00 00 00 00 00 00")

    '''def test_ronda_numerica_invalida_2(self):
        try:
            partida = Bolos("61 42 23 123 00 00 00 00 00 00")
        except RondaInvalida:
            pass
        else:
            self.fail("Hay más de dos bolas en una ronda")'''
    
    def test_ronda_numerica_invalida_3(self):
        with self.assertRaises(RondaAbiertaExcesoBolas):
            partida = Bolos("61 42 23 1 00 00 00 00 00 00")

    def test_ronda_letras_invalida(self):
        with self.assertRaises(RondaNoDefinida):
            partida = Bolos("at 42 i- +s 35 $% 67 X 3/ 00")  

    def test_ronda_letras_invalida_2(self):
        with self.assertRaises(NumeroRondasDistintoDiez):
            partida = Bolos("holasoyunstring")                

    def test_partida_sin_bonus(self):
        partida = Bolos("61 42 23 72 34 X 5/ 42 81 61")
        self.assertEqual(90, partida.calcularPuntuacion(), "La puntuación no coincide")

    def test_partida_bonus_spare(self):
        partida = Bolos("61 42 23 72 34 X 5/ 42 81 6/3")
        self.assertEqual(96, partida.calcularPuntuacion(), "La puntuación no coincide")

    def test_partida_bonus_spare_2(self):
        partida = Bolos("61 42 23 72 34 X 5/ 42 81 6/X")
        self.assertEqual(103, partida.calcularPuntuacion(), "La puntuación no coincide")

    def test_ultima_ronda_numerica_invalida(self):
        with self.assertRaises(RondaAbiertaExcesoBolas):
            partida = Bolos("61 42 23 72 34 X 5/ 42 81 612")
    
    def test_ultima_ronda_numerica_invalida_2(self):
        with self.assertRaises(RondaAbiertaExcesoBolas):
            partida = Bolos("61 42 23 72 34 X 5/ 42 81 6")
    
    def test_ultima_ronda_numerica_invalida_3(self):
        with self.assertRaises(SumaRondaMasDeDiez):
            partida = Bolos("61 42 23 72 34 X 5/ 42 81 67")

    def test_ultima_ronda_spare_invalida(self):
        with self.assertRaises(RondaUltimaSpareNoValida):
            partida = Bolos("61 42 23 72 34 X 5/ 42 81 6/88")

    def test_ultima_ronda_spare_invalida_2(self):
        with self.assertRaises(RondaUltimaSpareNoValida):
            partida = Bolos("61 42 23 72 34 X 5/ 42 81 6//")

    def test_ultima_ronda_strike(self):
        partida = Bolos("61 42 23 72 34 X 5/ 42 81 X43")
        self.assertEqual(100, partida.calcularPuntuacion(), "La puntuación no coincide")

    def test_ultima_ronda_strike_2(self):
        partida = Bolos("61 42 23 72 34 X 5/ 42 81 XX3")
        self.assertEqual(106, partida.calcularPuntuacion(), "La puntuación no coincide")
    
    def test_ultima_ronda_strike_3(self):
        partida = Bolos("61 42 23 72 34 X 5/ 42 81 XXX")
        self.assertEqual(113, partida.calcularPuntuacion(), "La puntuación no coincide")

    def test_ultima_ronda_strike_4(self):
        partida = Bolos("61 42 23 72 34 X 5/ 42 81 X4/")
        self.assertEqual(103, partida.calcularPuntuacion(), "La puntuación no coincide")

    def test_ultima_ronda_strike_invalida(self):
        with self.assertRaises(RondaUltimaStrikeNoValida):
            partida = Bolos("61 42 23 72 34 X 5/ 42 81 X6")
    
    def test_ultima_ronda_strike_invalida_2(self):
        with self.assertRaises(RondaUltimaStrikeNoValida):
            partida = Bolos("61 42 23 72 34 X 5/ 42 81 X/5")
    
    def test_ultima_ronda_strike_invalida_3(self):
        with self.assertRaises(RondaUltimaStrikeNoValida):
            partida = Bolos("61 42 23 72 34 X 5/ 42 81 XX/")

    def test_ultima_ronda_invalida(self):
        with self.assertRaises(RondaNoDefinida):
            partida = Bolos("61 42 23 72 34 X 5/ 42 81 abc")

    def test_partida_completa_final(self):
        partida = Bolos("45 X X 6/ 24 X 90 3/ 81 X7/")
        self.assertEqual(148, partida.calcularPuntuacion(), "La puntuación no coincide")
    
    def test_partida_completa_final_2(self):
        partida = Bolos("4/ X X X 71 30 00 54 3/ 9/3")
        self.assertEqual(147, partida.calcularPuntuacion(), "La puntuación no coincide")
    
    def test_partida_completa_final_3(self):
        partida = Bolos("X X X 54 6/ 8/ 60 35 X 72")
        self.assertEqual(159, partida.calcularPuntuacion(), "La puntuación no coincide")
    
    def test_partida_completa_final_4(self):
        partida = Bolos("70 35 8/ X X 72 61 X 9/ XX3")
        self.assertEqual(160, partida.calcularPuntuacion(), "La puntuación no coincide")

    def test_partida_completa_final_5(self):
        partida = Bolos("9/ 43 X X X 6/ 72 34 7/ 9/X")
        self.assertEqual(169, partida.calcularPuntuacion(), "La puntuación no coincide")

if __name__ == '__main__':
    unittest.main()