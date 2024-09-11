class RecomendacaoLivros:
    def recomendar_por_autor(self, arvore, autor):
        livros = arvore.listar_livros_em_ordem()
        recomendados = [livro for livro in livros if autor.lower() in livro.autor.lower()]
        return recomendados

    def recomendar_por_tema(self, arvore, tema):
        livros = arvore.listar_livros_em_ordem()
        recomendados = [livro for livro in livros if tema.lower() in livro.titulo.lower()]
        return recomendados
