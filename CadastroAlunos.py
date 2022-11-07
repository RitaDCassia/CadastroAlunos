import time

# mensagem de bem vindo com um time para aparecer

print('-'*40)
time.sleep(1)
print('bem vindo!')
time.sleep(1)
print('Aqui você poderá salvar nome, curso, matricula, notas e media dos seus alunos '
      'em um novo arquivo de forma rápida e prática.')
time.sleep(2)
print('Basta informar os valores pedidos e ver a mágica acontecer. Bom trabalho!')
time.sleep(1)
print('-' * 40)
time.sleep(1)

# criando/abrindo o arquivo para escrever nele

with open('alunos.txt', 'w') as arquivo:
    contador = 0
    inicio = 0

    # final = numero de alunos que existem na sala.
    # esse numero de alunos entrará no for e decretará quantas vezes será pedidio informaçoes.

    # Maprovado, Mrecupera e Maprova é onde pede os valores para usar no if da média.

    try:
        final = int(input('informe quantos alunos existem na sua sala (valores inteiros ex: 1,2,3..): '))
        Mreprovado = float(input('Informe com base na média das notas com quanto o seu aluno ficaria reprovado'
                                 '(ex: se de 0 - 4.9 o aluno reprovaria, você deverá informar 4.9): '))
        Mrecupera = float(input('Informe com base na média das notas com quanto o seu aluno ficaria de recuperação'
                                 f'(ex: se de {(Mreprovado + 0.1)} - 5.9 o aluno ficaria de recuperação, você deverá informar 5.9): '))
        Maprova = float(input('Informe com base na média das notas com quanto o seu aluno estaria aprovado'
                                f'(ex: se de {(Mrecupera + 0.1)} - 10 o aluno ficaria aprovado, você deverá informar {(Mrecupera + 0.1)}: '))
        print('-'*40)
        print(f'Com base nas suas respostas sua sala tem {final} alunos.\n'
              f'A média da nota para os alunos:\n'
              f'Reprovados: 0 - {Mreprovado}\n'
              f'Recuperação: {(Mreprovado + 0.1)} - {Mrecupera}\n'
              f'Aprovado: {Maprova} - 10')
        print('-' * 40)
        pergunta = input('As informações estão corretas? (informe "s" para sim e "n" para não) [S/N]: ').upper()

        # se o usuário responder que os valores estão corretos o programa continuará e pedirá as informações
        # que serão escritas no arquivo "alunos.txt"

        if pergunta == 'S':
            for aluno in range(inicio, final):
                contador += 1
                nome = str(input('informe o nome do aluno: '))
                matricula = str(input('informe a matricula: '))
                curso = str(input('informe o curso: '))
                nota1 = float(input('informe a nota da AV1: '))
                nota2 = float(input('informe a nota da AV2: '))
                media = (nota1 + nota2) / 2
                escrever = arquivo.write(f'\n\nAluno({contador})\n\n'
                                         f'nome:{nome}\n' \
                                         f'matricula: {matricula}\n' \
                                         f'curso: {curso}\n' \
                                         f'nota AV1: {nota1}\n' \
                                         f'Nota AV2: {nota2}\n' \
                                         f'Média: {media}\n')

                # definindo conforme a media das notas se o aluno foi aprovado, reprovado ou está de recuperação.

                if media <= Mreprovado:
                    arquivo.write('status: Reprovado!')
                    print('status: reprovado!')
                elif (Mreprovado + 0.1) <= media <= Mrecupera:
                    print('status: recuperação')
                    arquivo.write('status: Recuperação!')
                else:
                    print('status: aprovado!')
                    arquivo.write('status: Aprovado!')
                print('-'*40)
            print('-'*40)
            time.sleep(1)
            print('Fim do programa!\n')
            time.sleep(1)
            print('Agora basta você procurar o documento com o nome "alunos.txt" no seu computador! '
                  'Volte sempre!')

        # se a resposta for nao (n) o programa não vai continuar.

        else:
            print('-' * 40)
            time.sleep(1)
            print('Poxa!\n'
                  'reinicie o programa para informar corretamente os valores!')

    # se o usuário informar um valor errado mostra essa mensagem

    except ValueError as erro:
        print('Ops! algo deu errado com o valor informado!\n'
              'Reinicie o programa e informe um valor correto!')