# No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade 
# para obter a lista de livros disponíveis publicados em um ano específico.


from atividades import Livro

livro1 = Livro("Dom Quixote", "Miguel de Cervantes", 1605)
livro2 = Livro("O Grande Gatsby", "F. Scott Fitzgerald", 1925)
livro3 = Livro("1984", "George Orwell", 1949)
livro4 = Livro("Cem Anos de Solidão", "Gabriel García Márquez", 1967)
livro5 = Livro("O Sol é Para Todos", "Harper Lee", 1960)
livro6 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)
livro7 = Livro("O Hobbit", "J.R.R. Tolkien", 1937)
livro8 = Livro("Admirável Mundo Novo", "Aldous Huxley", 1932)

Livro.verificar_disponibilidade(1605)