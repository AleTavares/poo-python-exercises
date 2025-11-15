import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestExercicio03(unittest.TestCase):
    def setUp(self):
        try:
            import respExercicio03
            self.module = respExercicio03
        except ImportError:
            self.fail("Arquivo respExercicio03.py não encontrado")
    
    def test_professor_existe(self):
        self.assertTrue(hasattr(self.module, 'Professor'), "Classe Professor não encontrada")
    
    def test_salario_privado(self):
        prof = self.module.Professor("Dr. Silva", "Computação", 5000)
        self.assertTrue(hasattr(prof, '_salario'), "Atributo _salario não encontrado")
    
    def test_property_salario(self):
        prof = self.module.Professor("Dr. Silva", "Computação", 5000)
        self.assertEqual(prof._salario, 5000)
    
    def test_setter_salario_positivo(self):
        prof = self.module.Professor("Dr. Silva", "Computação", 5000)
        prof._salario = 6000
        self.assertEqual(prof._salario, 6000)

if __name__ == '__main__':
    unittest.main()