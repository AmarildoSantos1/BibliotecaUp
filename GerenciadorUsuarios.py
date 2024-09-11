class GerenciadorUsuarios:
    def __init__(self):
        self.usuarios = []

    def cadastrar_usuario(self, username, senha):
        for usuario in self.usuarios:
            if usuario.username == username:
                raise UsuarioJaExisteException(username)
        novo_usuario = Usuario(username, senha)
        self.usuarios.append(novo_usuario)
        print(f"Usuário {username} cadastrado com sucesso!")

    def fazer_login(self, username, senha):
        for usuario in self.usuarios:
            if usuario.username == username and usuario.senha == senha:
                print(f"Bem-vindo(a), {username}!")
                return True
        raise UsuarioNaoEncontradoException()
