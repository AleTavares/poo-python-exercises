import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestExercicio02(unittest.TestCase):
    def setUp(self):
        try:
            import respostas.respExercicio02
            self.module = respostas.respExercicio02
        except ImportError:
            self.fail("Arquivo respExercicio02.py não encontrado")
    
    def test_aluno_tem_notas(self):
        aluno = self.module.Aluno("João", "123", "Engenharia")
        self.assertTrue(hasattr(aluno, 'notas'), "Atributo notas não encontrado")
        self.assertIsInstance(aluno.notas, list, "Notas deve ser uma lista")
    
    def test_adicionar_nota(self):
        aluno = self.module.Aluno("João", "123", "Engenharia")
        aluno.adicionar_nota(8.5)
        self.assertIn(8.5, aluno.notas)
    
    def test_calcular_media(self):
        aluno = self.module.Aluno("João", "123", "Engenharia")
        aluno.adicionar_nota(8.0)
        aluno.adicionar_nota(7.0)
        self.assertEqual(aluno.calcular_media(), 7.5)
    
    def test_status_method_exists(self):
        aluno = self.module.Aluno("João", "123", "Engenharia")
        self.assertTrue(hasattr(aluno, 'status'), "Método status não encontrado")

if __name__ == '__main__':
    unittest.main()