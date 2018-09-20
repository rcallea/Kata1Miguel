from unittest import TestCase
from Solver import Solver

class TestSolver(TestCase):

    def test_contar_cadena_vacia(self):
        s=Solver()
        self.assertEqual(s.tamano("")[0],0)

    def test_contar_cadena_un_elemento(self):
        s=Solver()
        self.assertEqual(s.tamano("1")[0],1)

    def test_contar_cadena_dos_numeros(self):
        s=Solver()
        self.assertEqual(s.tamano("2,5")[0],2)

    def test_contar_cadena_muchos_numeros(self):
        s=Solver()
        self.assertEqual(s.tamano("9,5,3,2,6,7,5,6,8,4,4,5")[0],12)

    def test_min_cadena_vacia(self):
        s=Solver()
        self.assertEqual(s.tamano("")[1],9999999999999)

    def test_min_cadena_un_elemento(self):
        s=Solver()
        self.assertEqual(s.tamano("55")[1],55)

    def test_min_cadena_dos_numeros(self):
        s=Solver()
        self.assertEqual(s.tamano("3,5")[1],3)

    def test_min_cadena_muchos_numeros(self):
        s=Solver()
        self.assertEqual(s.tamano("9,5,3,2,6,7,5,6,8,4,4,5")[1],2)

    def test_max_cadena_vacia(self):
        s=Solver()
        self.assertEqual(s.tamano("")[2],-9999999999999)

    def test_max_cadena_un_elemento(self):
        s=Solver()
        self.assertEqual(s.tamano("55")[2],55)

    def test_max_cadena_dos_numeros(self):
        s=Solver()
        self.assertEqual(s.tamano("3,5")[2],5)

    def test_max_cadena_muchos_numeros(self):
        s=Solver()
        self.assertEqual(s.tamano("9,5,3,2,6,7,5,63,8,4,4,5")[2],63)

    def test_avg_cadena_vacia(self):
        s=Solver()
        self.assertEqual(s.tamano("")[3],0)

    def test_avg_cadena_un_elemento(self):
        s=Solver()
        self.assertEqual(s.tamano("55")[3],55)

    def test_avg_cadena_dos_numeros(self):
        s=Solver()
        self.assertEqual(s.tamano("3,5")[3],4)

    def test_avg_cadena_muchos_numeros(self):
        s=Solver()
        self.assertEqual(s.tamano("9,5,3,2,6,7,5,63,8,4,4,5")[3],10.083333333333334)

