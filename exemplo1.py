executa = input('Executar o bloco: ')
contador = 0
while executa == 'sim' or executa == 's':
    contador += 1
    executa = input('Executar o bloco: ')
print(f'O bloco foi executado {contador} vezes')