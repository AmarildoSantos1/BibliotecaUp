class GrafoAutores:
    def __init__(self):
        self.grafo = {}

    def adicionar_livro(self, livro):
        if livro.autor not in self.grafo:
            self.grafo[livro.autor] = set()
        
        for outro_autor in self.grafo:
            if livro.autor != outro_autor:
                # Supondo que livros com o mesmo tema estão relacionados
                if livro.tema in livro.temas:
                    self.grafo[livro.autor].add(outro_autor)
                    self.grafo[outro_autor].add(livro.autor)

    def buscar_relacoes(self, autor):
        if autor in self.grafo:
            return self.grafo[autor]
        return set()

    def listar_autores(self):
        return list(self.grafo.keys())
