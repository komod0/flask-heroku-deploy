
def prueba_re_piola(x):
    return 2 * x

class TestMultiplicar:
    def test_multiplicar(self):
        assert prueba_re_piola(3) == 6

    def test_que_ahora_anda(self):
        assert prueba_re_piola(2) == 4
