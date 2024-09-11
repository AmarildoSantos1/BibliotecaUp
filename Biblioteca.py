#  exceções
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

#  classes 
class Livro:
    def __init__(self, titulo, autor, ano, temas=None):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.temas = temas if temas else []

    def __repr__(self):
        return f"{self.titulo} por {self.autor} ({self.ano})"

class Usuario:
    def __init__(self, username, senha):
        self.username = username
        self.senha = senha

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
        livro = self._buscar(self.raiz, titulo)
        if livro is None:
            raise LivroNaoEncontradoException(titulo)
        return livro

    def _buscar(self, no_atual, titulo):
        if no_atual is None or no_atual.livro.titulo == titulo:
            return no_atual.livro if no_atual else None
        if titulo < no_atual.livro.titulo:
            return self._buscar(no_atual.esquerda, titulo)
        return self._buscar(no_atual.direita, titulo)

class GrafoAutores:
    def __init__(self):
        self.grafo = {}

    def adicionar_livro(self, livro):
        if livro.autor not in self.grafo:
            self.grafo[livro.autor] = set()
        
        for outro_autor in self.grafo:
            if livro.autor != outro_autor:
                #  livros com o mesmo tema estão relacionados
                if any(tema in livro.temas for tema in livro.temas):
                    self.grafo[livro.autor].add(outro_autor)
                    self.grafo[outro_autor].add(livro.autor)

    def buscar_relacoes(self, autor):
        if autor in self.grafo:
            return self.grafo[autor]
        return set()

    def listar_autores(self):
        return list(self.grafo.keys())

class RecomendacaoLivros:
    def recomendar_por_autor(self, arvore_livros, autor):
        livros = arvore_livros.listar_livros_em_ordem()
        return [livro for livro in livros if livro.autor == autor]

    def recomendar_por_tema(self, arvore_livros, tema):
        livros = arvore_livros.listar_livros_em_ordem()
        return [livro for livro in livros if tema in livro.temas]

class Biblioteca:
    def __init__(self):
        self.arvore_livros = ArvoreBinariaBusca()
        self.grafo_autores = GrafoAutores()
        self.recomendacao = RecomendacaoLivros()
        self.gerenciador_usuarios = GerenciadorUsuarios()
        self.usuario_logado = False

    def exibir_menu_principal(self):
        print("\nMenu Principal:")
        print("1. Login")
        print("2. Cadastro")
        print("3. Sair")

    def exibir_menu_biblioteca(self):
        print("\nMenu da Biblioteca:")
        print("1. Adicionar Livro")
        print("2. Listar Livros")
        print("3. Buscar Livro por Título")
        print("4. Recomendar Livros por Autor")
        print("5. Recomendar Livros por Tema")
        print("6. Ver Relações de Autores")
        print("7. Logout")

    def iniciar(self):
        while True:
            if not self.usuario_logado:
                self.exibir_menu_principal()
                try:
                    opcao = input("\nEscolha uma opção: ")

                    if opcao == "1":
                        username = input("Digite o nome de usuário: ")
                        senha = input("Digite a senha: ")
                        if self.gerenciador_usuarios.fazer_login(username, senha):
                            self.usuario_logado = True

                    elif opcao == "2":
                        username = input("Escolha um nome de usuário: ")
                        senha = input("Escolha uma senha: ")
                        self.gerenciador_usuarios.cadastrar_usuario(username, senha)

                    elif opcao == "3":
                        print("Saindo do sistema...")
                        break

                    else:
                        raise OpcaoInvalidaException()

                except (UsuarioJaExisteException, UsuarioNaoEncontradoException, OpcaoInvalidaException) as e:
                    print(e)

            else:
                self.exibir_menu_biblioteca()
                try:
                    escolha = input("\nEscolha uma opção: ")

                    if escolha == "1":
                        titulo = input("Digite o título do livro: ")
                        autor = input("Digite o autor do livro: ")
                        ano = input("Digite o ano de publicação: ")
                        temas = input("Digite os temas (separados por vírgula): ").split(',')
                        livro = Livro(titulo, autor, ano, [tema.strip() for tema in temas])
                        self.arvore_livros.adicionar_livro(livro)
                        self.grafo_autores.adicionar_livro(livro)
                        print("Livro adicionado com sucesso!")

                    elif escolha == "2":
                        livros = self.arvore_livros.listar_livros_em_ordem()
                        for livro in livros:
                            print(livro)

                    elif escolha == "3":
                        titulo = input("Digite o título do livro: ")
                        livro = self.arvore_livros.buscar_por_titulo(titulo)
                        print(f"Livro encontrado: {livro}")

                    elif escolha == "4":
                        autor = input("Digite o nome do autor: ")
                        recomendados = self.recomendacao.recomendar_por_autor(self.arvore_livros, autor)
                        if recomendados:
                            print("Livros recomendados:")
                            for livro in recomendados:
                                print(livro)
                        else:
                            print("Nenhum livro encontrado para esse autor.")

                    elif escolha == "5":
                        tema = input("Digite o tema: ")
                        recomendados = self.recomendacao.recomendar_por_tema(self.arvore_livros, tema)
                        if recomendados:
                            print("Livros recomendados:")
                            for livro in recomendados:
                                print(livro)
                        else:
                            print("Nenhum livro encontrado para esse tema.")

                    elif escolha == "6":
                        autor = input("Digite o nome do autor: ")
                        relacoes = self.grafo_autores.buscar_relacoes(autor)
                        if relacoes:
                            print(f"Autores relacionados com {autor}: {', '.join(relacoes)}")
                        else:
                            print(f"Nenhuma relação encontrada para o autor {autor}.")

                    elif escolha == "7":
                        self.usuario_logado = False
                        print("Logout realizado com sucesso!")

                    else:
                        raise OpcaoInvalidaException()

                except (LivroNaoEncontradoException, OpcaoInvalidaException) as e:
                    print(e)

# Inicializar 
biblioteca = Biblioteca()
biblioteca.iniciar()
