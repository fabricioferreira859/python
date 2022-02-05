meses = ["JANEIRO","FEVEREIRO","MARÇO","ABRIL","MAIO","JUNHO","JULHO","AGOSTO"
         ,"SETEMBRO","OUTUBRO","NOVEMBRO","DEZEMBRO"]

temperatura = []
cont = 0

for p in range(0,len(meses)):
    temperatura.append(int(input(f'Digite a temperatura do mês de {meses[p]}: ')))
    print()
    cont += temperatura[p]

media = cont/12

print('')
print('='*50)
print(f'Média anual das temperaturas: {media:.2f}ºC\n')

print('Meses com temperatura acima da média:\n')
for p in range(0,len(meses)):
    if temperatura[p] > media:
        print(f'{p+1} - {meses[p]}')
print('='*50)
print('\n\n')
