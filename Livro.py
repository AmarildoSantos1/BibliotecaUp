class Livro:
    def __init__(self, titulo, autor, ano, temas=None):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.temas = temas if temas else []

    def __repr__(self):
        return f"{self.titulo} por {self.autor} ({self.ano})"
