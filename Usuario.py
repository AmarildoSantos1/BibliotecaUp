class Usuario:
    def __init__(self, username, senha):
        self.username = username
        self.senha = senha

    def __str__(self):
        return f"Usuário: {self.username}"
