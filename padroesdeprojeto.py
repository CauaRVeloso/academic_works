# Interface comum para todas as formas
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def desenhar(self):
        pass

# Implementações concretas: Círculo e Retângulo
class Circulo(Forma):
    def desenhar(self):
        print("Desenhando um círculo")

class Retangulo(Forma):
    def desenhar(self):
        print("Desenhando um retângulo")

# Composite: Grupo de Formas
class GrupoFormas(Forma):
    def __init__(self):
        self._formas = []

    def adicionar(self, forma):
        self._formas.append(forma)

    def remover(self, forma):
        self._formas.remove(forma)

    def desenhar(self):
        print("Desenhando um grupo de formas:")
        for forma in self._formas:
            forma.desenhar()

# Decorator base
class FormaDecorator(Forma):
    def __init__(self, forma):
        self._forma = forma

    def desenhar(self):
        self._forma.desenhar()

# Decorator concreto: Borda
class FormaComBorda(FormaDecorator):
    def desenhar(self):
        self._forma.desenhar()
        print("-> Adicionando borda")

# Decorator concreto: Sombra
class FormaComSombra(FormaDecorator):
    def desenhar(self):
        self._forma.desenhar()
        print("-> Adicionando sombra")

# Simulação de biblioteca externa
class BibliotecaDesenhoExterna:
    def draw_shape(self):
        print("Desenho realizado pela API externa")

# Adapter
class FormaAdaptada(Forma):
    def __init__(self, adaptado):
        self._adaptado = adaptado

    def desenhar(self):
        self._adaptado.draw_shape()

# Exemplo de uso
if __name__ == "__main__":
    circulo = Circulo()
    retangulo = Retangulo()

    forma_com_borda = FormaComBorda(circulo)
    forma_com_sombra = FormaComSombra(retangulo)

    grupo = GrupoFormas()
    grupo.adicionar(forma_com_borda)
    grupo.adicionar(forma_com_sombra)

    forma_externa = FormaAdaptada(BibliotecaDesenhoExterna())
    grupo.adicionar(forma_externa)

    grupo.desenhar()