dic = {}
while True:
    chave = input('Matricula: ')
    nome = input('Nome: ')
    idade = input('Idade: ')
    rg = int(input('RG: '))

    dic[chave] = nome,idade,rg 
    
    deseja = input('Deseja Cadastrar Mais (S/N): ').upper()
    if deseja == 'N':
        print('Obrigao por Usar Nosso Sistema!!!')
        break

print(dic)