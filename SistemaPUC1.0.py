'''
Atividade Somativa 01 - Módulo Verão 2023
Aluno: Nicolas Marques de Gouvea
Curso: Análise e Desenvolvimento de Sistemas

'''
# Projeto Sistema PUC - versão 1.0


class Estudante: # Definindo Classe Estudante.
  def __init__(self, matricula, nome, idade, curso): # Foi utilizado o método construtor __init__ com quatro parâmetros para adicionar os atributos toda vez que um novo objeto da classe estudante for criado ao longo do código, sendo referenciados com a palavra chave self.
    self.matricula = matricula
    self.nome = nome
    self.idade = idade
    self.curso = curso

# Lista para armazenar os estudantes: deixei salvo um exemplo base.

lista_estudantes = [Estudante('0123', 'Nicolas', '25', 'ads')]

# Funções do menu gerenciar estudantes.

def criar_estudante():
    print('\nCriar registro de estudante: \n')
    matricula = input('Matrícula: ')
    nome = input('Nome: ')
    idade = input('Idade: ')
    curso = input('Curso: ')
    estudante = Estudante(matricula, nome, idade, curso) # Variável estudante = classe estudante
    lista_estudantes.append(estudante) # Adicionando estudante na lista lista_estudantes atraves do método .append
    print('\nEstudante criado!\n')

def atualizar_estudante():
    print('\nAtualizar registro de estudante:\n ')
    matricula = (input('Digite a matrícula do estudante para atualizar os dados: '))
    for estudante in lista_estudantes: # Iniciado um loop finito  percorrendo pelos estudantes da lista_estudantes.
        if estudante.matricula == matricula: # Condição imposta: se o atributo matrícula do objeto estudante for igual a variável matrícula que solicitamos ao usuário, o bloco de ações abaixo ira ocorrer.
            print('Atualize as informações do estudante:\n')
            novo_nome = input('Nome: ')    
            novo_idade = input('Idade: ') 
            novo_curso = input('Curso: ')
            estudante.nome = novo_nome  
            estudante.idade = novo_idade 
            estudante.curso = novo_curso 
            print('\nEstudante atualizado!\n') # As novas variáveis solicitadas ao usuário vão substituir os respectivos atributos do objeto dentro da lista. 
        else :
            print('\nEstudante não encontrado.\n')

def excluir_estudante():
    print('\nExcluir registro de estudante.\n')
    matricula = input('Digite a matrícula do estudante que deseja excluir: ')
    for estudante in lista_estudantes : # Iniciado um loop finito  percorrendo os objetos da lista.
        if estudante.matricula == matricula :
            print('Estudante encontrado.')
            confirmacao = input('Você deseja excluir o estudante(sim / nao) ? ')
            if confirmacao == 'sim' : # Condição composta: SE a matrícula for igual a de um objeto da lista e ainda SE usuário digitar sim para confirmação, o bloco abaixo será executado.
                lista_estudantes.remove(estudante) # Objeto estudante removido atravas do método remove.
                print('Estudante excluído.\n')
                break
        else:
            print('Matrícula inválida.\n')

def listar_estudante():
    print('\nLista de estudantes:\n')
    for estudante in lista_estudantes: # loop percorrendo os objetos da lista.
        print(f'Matrícula: {estudante.matricula}') # É impresso na tela todos os objetos e seus parâmetros da classe estudante.
        print(f'Nome: {estudante.nome}')
        print(f'Idade: {estudante.idade}')
        print(f'Curso: {estudante.curso}\n')

def buscar_estudante():
    print('\nBuscar estudante: \n')
    matricula = input('Digite a matrícula do estudante: ')
    for estudante in lista_estudantes : # Iniciado loop finito percorrendo os objetos da lista.
        if estudante.matricula == matricula : # Condição imposta: diferente da função listar_estudante aqui só vai listar o objeto que possuí o mesmo parâmetro, no caso a matrícula solicitada.
            print('\nEstudante encontrado:\n')
            print(f'Nome: {estudante.nome}')
            print(f'Idade: {estudante.idade}')
            print(f'Curso: {estudante.curso}\n')
        else : # Se nenhuma matrícula corresponder a um objeto da lista_estudantes o bloco abaixo será executado.
            print('Estudante não encontrado.')

# Funções do menu principal :

def gerenciar_estudantes():
    while True: # Loop é iniciado.
        print('\nGerenciar Estudantes')
        print('Selecione uma opção:\n')      
        print('1. Criar.')
        print('2. Atualizar.')
        print('3. Excluir.')
        print('4. Listar.')
        print('5. Buscar.')
        print('6. Voltar ao menu principal.\n')
        
        opcao_2 = int(input('')) # Variável para armazernar a opção solicitada ao usuário, cada opção que escolher irá executar uma função diferente.

        if opcao_2 == 1 :
            criar_estudante()
            
        elif opcao_2 == 2:
            atualizar_estudante()
            
        elif opcao_2 == 3:
            excluir_estudante()
 
        elif opcao_2 == 4:
            listar_estudante()
        
        elif opcao_2 == 5:
            buscar_estudante()

        elif opcao_2 == 6: # Opcão para voltar ao menu principal.
            break

# Funções do menu principal em desenvolvimento.

def gerenciar_professores():
    print('\nEm desenvolvimento.\n')

def gerenciar_disciplinas():
    print('\nEm desenvolvimento.\n')
  
def gerenciar_turmas():
    print('\nEm desenvolvimento.\n')
  
def gerenciar_matriculas():
    print('\nEm desenvolvimento.\n')


# Menu principal do programa.

while True: # Loop infinito é iniciado.
    print('\nSistema PUC - versão 1.0')
    print('Seja bem-vindo.')
    print('Selecione uma opção:\n')
    print('1. Gerenciar estudantes.')
    print('2. Gerenciar professores.')
    print('3. Gerenciar disciplinas.')
    print('4. Gerenciar turmas.')
    print('5. Gerenciar matrículas.')
    print('6. Sair.\n')

    opcao = (input()) # Variável para armazernar a opção solicitada ao usuário, cada opção que escolher irá executar a função respectiva.

    if opcao == '1':
        gerenciar_estudantes()
    elif opcao == '2':
        gerenciar_professores()
    elif opcao == '3':
        gerenciar_disciplinas()
    elif opcao == '4':
        gerenciar_turmas()
    elif opcao == '5':
        gerenciar_matriculas()
    elif opcao == '6':
        print('\nPrograma encerrado.\n')
        break
    else:
        print('\nOpção inválida.\n')

