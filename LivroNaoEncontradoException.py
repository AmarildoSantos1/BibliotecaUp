class LivroNaoEncontradoException(Exception):
    def __init__(self, titulo):
        super().__init__(f"Livro '{titulo}' não encontrado.")
