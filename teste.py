dic = {}
while True:
    chave = input('Matricula: ')
    nome = input('Nome: ')
    idade = input('Idade: ')

    dic[chave] = nome,idade 
    
    deseja = input('Deseja Cadastrar Mais (S/N): ').upper()
    if deseja == 'N':
        print('Obrigao por Usar Nosso Sistema!!!')
        break

print(dic)