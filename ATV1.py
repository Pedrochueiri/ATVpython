total = 0
preco = float(input("Digite os preços do item: "))
while preco != -1:
    total += preco
    preco = float(input("valor do item: "))
   
print('total da compra: R$',str(total))