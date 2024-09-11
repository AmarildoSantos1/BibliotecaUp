class NoArvore:
    def __init__(self, livro):
        self.livro = livro
        self.esquerda = None
        self.direita = None

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def adicionar_livro(self, livro):
        if self.raiz is None:
            self.raiz = NoArvore(livro)
        else:
            self._adicionar(self.raiz, livro)

    def _adicionar(self, no_atual, livro):
        if livro.titulo < no_atual.livro.titulo:
            if no_atual.esquerda is None:
                no_atual.esquerda = NoArvore(livro)
            else:
                self._adicionar(no_atual.esquerda, livro)
        else:
            if no_atual.direita is None:
                no_atual.direita = NoArvore(livro)
            else:
                self._adicionar(no_atual.direita, livro)

    def listar_livros_em_ordem(self):
        return self._em_ordem(self.raiz, [])

    def _em_ordem(self, no_atual, lista_livros):
        if no_atual:
            self._em_ordem(no_atual.esquerda, lista_livros)
            lista_livros.append(no_atual.livro)
            self._em_ordem(no_atual.direita, lista_livros)
        return lista_livros

    def buscar_por_titulo(self, titulo):
        return self._buscar(self.raiz, titulo)

    def _buscar(self, no_atual, titulo):
        if no_atual is None or no_atual.livro.titulo == titulo:
            return no_atual.livro if no_atual else None
        if titulo < no_atual.livro.titulo:
            return self._buscar(no_atual.esquerda, titulo)
        return self._buscar(no_atual.direita, titulo)
