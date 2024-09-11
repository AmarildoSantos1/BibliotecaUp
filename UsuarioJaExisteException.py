class UsuarioJaExisteException(Exception):
    def __init__(self, username):
        super().__init__(f"O usuário '{username}' já existe.")

class UsuarioNaoEncontradoException(Exception):
    def __init__(self):
        super().__init__("Usuário ou senha incorretos.")

class LivroNaoEncontradoException(Exception):
    def __init__(self, titulo):
        super().__init__(f"Livro '{titulo}' não encontrado.")

class OpcaoInvalidaException(Exception):
    def __init__(self):
        super().__init__("Opção inválida. Por favor, tente novamente.")
