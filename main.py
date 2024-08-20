import cinematica as cn# estou importanto a funcao criada - mesmo estando na mesma pasta devemos importar no main

# mostra o menu na tela
while True:
    cn.mostrar_menu()
    opcao = input ('Opcao do usuario: ')

    match opcao:
        case '1':
            m = float(input('Informe a massa em kg: ').replace(',', '.'))
            h = float(input('Informe a altura em metros: ').replace(',', '.'))
            print(f'Energia potencia: {cn.calcular_ep(m,h):,.2f} J.')
            continue

        case '2':
            m = float(input('Informe a massa em kg: ').replace(',', '.'))
            v = float(input('Informe a velocidade em m/s: ').replace(',', '.'))
            print(f'Energia cinetica: {cn.calcular_ec(m,v):,.2f} J.')
            continue

        case '3':
            print('Programa encerrado.')
            break
        case _:
            print('Opçao inválida.')
            continue
        
