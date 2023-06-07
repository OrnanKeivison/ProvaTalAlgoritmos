def registrar_leitura(titulo, total, lidos):
    print(f'Você está lendo o livro {titulo}')
    print(f'O livro {titulo} tem {total} páginas!')
    print(f'Você já leu {lidos} páginas')
    print(f'Seu progresso de leitura foi de {((100*lidos)//total)}% do livro')


a = input()
b = int(input())
c = int(input())

registrar_leitura(a, b, c)