'''
Análise de Paciente com COVID-19.
'''
from time import sleep
from datetime import date

def espaco():
    print('\n\n')

def dados_adicionais():
    print('-=-' * 30)
    titulo = 'ADADOS ADICIONAIS'
    print(titulo.center(85))
    print('-=-' * 30)

def orientacoes():
    print('-=-' * 30)
    titulo = 'ORIENTAÇÕES PARA EVITAR A DISSEMINAÇÃO DO CORONAVÍRUS'
    print(titulo.center(85))
    print('-=-' * 30)

def contato_colegas():
    espaco()
    print('CONTATO DE DUAS PESSOAS COM QUE TEVE CONTATO')
    espaco()

def cadastro_de_pacientes():
    print('-=-' * 30)
    titulo = 'CADASTRO DE PACIENTES'
    print(titulo.center(85))
    print('-=-' * 30)

    dados_pacientes = dict()

    dados_pacientes['nome'] = str(input('Qual seu nome: ')).upper().strip()
    nasc = int(input('Qual o ano de nascimento: '))
    atual = date.today().year
    dados_pacientes['idade'] = atual - nasc
    print('Idade: {} anos'.format(dados_pacientes['idade']))


    if dados_pacientes['idade'] < 18:
        dados_pacientes['responsavel'] = str(input('Nome do responsavel: '))
        dados_pacientes['telefone_responsavel'] = int(input('Telefone RESPONSAVEL com DDD: '))
        dados_pacientes['parentesco'] = str(input('Grau de parentesco: '))
    else:
        dados_pacientes['telefone'] = int(input('Telefone com DDD: '))
        dados_pacientes['responsavel'] = str(input('Nome do parente: '))
        dados_pacientes['telefone_responsavel'] = int(input('Telefone PARENTE com DDD: '))
        dados_pacientes['parentesco'] = str(input('Grau de parentesco: '))

    dados_adicionais()

    dados_pacientes['viagem'] = str(input('Viajou para algum lugar nos ultimos 10  dias? [SIM/NÃO]: ')).upper().strip()[0]
    if dados_pacientes['viagem'] in 'S':
        dados_pacientes['cidade'] = str(input('Qual cidade? ')).upper().strip()
        dados_pacientes['estado'] = str(input('Qual estado? ')).upper().strip()
        dados_pacientes['pais'] = str(input('Qual pais? ')).upper().strip()
        dados_pacientes['suspeita_viagem'] = str(input('Ouve alguma casos suspeitor no {}? [SIM/NÃO]: '.format(dados_pacientes['nome']))).upper().strip()[0]
        if dados_pacientes['suspeita_viagem'] == 'S':
            dados_pacientes['contato'] = str(input('Esteve algum contato com as pessoas infectadas? [SIM/NÃO]: ')).strip().upper()[0]
            if dados_pacientes['contato'] == 'S':
                print('\nInforme o DADOS para contato..\n')

                x = 1
                while x <= 2:
                    dados_pacientes['pessoa'] = str(input('Nome da {}º pessoa:  '.format(x)))
                    dados_pacientes['Telefone'] = str(input('Telefone da {}º pessoa: '.format(x)))
                    x += 1

                sleep(2)
                print('Enviando dados das pessoas do(a) {} para os AGENTES DE SAÚDE. \nAGUARDE...'.format(dados_pacientes['nome']))
                sleep(2)
                print('Enviando dados das pessoas do(a) {} para os AGENTES DE EPIDEMIA NO LOCAL. \nAGUARDE...'.format(dados_pacientes['nome']))
                sleep(2)
                print('Enviando dados das pessoas do(a) {} para POLÍCIA CIVIL E MILITAR. \nAGUARDE...'.format(dados_pacientes['nome']))
                sleep(2)
                print('\033[32mDADOS ENVIADOS AOS DEPARTAMENTOS DE PANDEMIA DO COVID-19')
                sleep(1)
                print('Os contatos de {} serão localizados e mapeados'.format(dados_pacientes['nome']))

                print('Seguir com o diagnostico')

                dados_pacientes['doentes'] = str(input('Esteve ou esta se sentindo mal? [SIM/NÃO]: ')).strip().upper()[0]
                if dados_pacientes['doentes'] == 'S':
                    dados_pacientes['tempo_doentes'] = int(input('Quanto tempo? '))
                    if dados_pacientes['tempo_doentes'] > 8:
                        print('\033[33mAtenção')

                else:
                    dados_pacientes['doenca_gripe'] = str(input('Teve grip nos ultimos 3 mêses? [SIM/NÃO]: ')).upper().strip()[0]
                    if dados_pacientes['doenca_gripe'] == 'S':
                        dados_pacientes['febre'] = str(input('Esta com FEBRE? [SIM/NÃO]: ')).strip().upper()[0]
                        dados_pacientes['temperatura_febre'] = int(input('Qual a temperatura da febre ºC: '))
                        dados_pacientes['tosse'] = str(input('Esta com TOSSE? [SIM/NÃO]: ')).strip().upper()[0]
                        dados_pacientes['dor_de_garganta'] = str(input('Teve DOR DE GARGANTA? [SIM/NÃO]: ')).strip().upper()[0]

                        if dados_pacientes['febre'] == 'S' and dados_pacientes['tosse'] == 'S' and dados_pacientes['dor_de_garganta'] == 'S':
                            espaco()
                            sleep(2)
                            print('\033[33mRealizando pré-diagnóstico  AGUARDE...............')
                            sleep(2)
                            print('Mais uma pergunta..')
                            dados_pacientes['respiracao'] = str(input('Tem DIFICULDADE DE RESPIRAR? [SIM/NÃO]: ')).strip().upper()[0]
                            if dados_pacientes['respiracao'] == 'S' and dados_pacientes['temperatura_febre'] >= 39:
                                print('Realizando a notificação o PARENTE DO PACIENTE AGUARDE.....')

                                sleep(2)
                                print('Realizar exames...')
                                sleep(2)
                                print('\033[31mO SISTEMA INDENTIFICOU SUSPEITA DE COVID-19')
                                print('\033[33mO paciente deve entrar em quarentena')
                                sleep(2)
                                print('\033[33mAcionando a equipe..\nAGUARDE...')

                                print('A(o) {} do paciente {}'.format(dados_pacientes['responsavel'], dados_pacientes['nome']))
                                print('Pelo telefone {}.'.format(dados_pacientes['telefone_responsavel']))
                                print('Data da notificação {}'.format(date.today()))


                                if (dados_pacientes['idade'] >= 60) and (dados_pacientes['idade'] <= 10):
                                    print('\033[31m Obs.: Paciente FAZ parte do GRUPO DE RISCO.')
                                    sleep(1)
                                    opcao = str(input('Possui plano de saúde? [ 1 ] SIM e [ 2 ] Não: '))

                                    if opcao == 1:
                                        print(
                                            '\033[33m Realizando busca do prontuário do(a) paciente {} encontado na base de dados do SUS.'
                                            .format(dados_pacientes['nome']))
                                        sleep(1)
                                        print('Dados encontrado')
                                        sleep(1)
                                    else:
                                        dados_pacientes['plano'] = str(
                                            input('Qual o seu plano {}:'.format(dados_pacientes['nome'])))
                                        print(
                                            '\033[33m Realizando busca do prontuário do(a) paciente {} encontado base de dados do plano de saúde {}.'
                                            .format(dados_pacientes['nome'], dados_pacientes['plano']))
                                        sleep(1)
                                        print('Dados encontrado')
                                    print('')
                                else:
                                    print('\033[32m Obs.: Paciente FORA do GRUPO DE RISCO.')

                                    sleep(1)

                                    print('Realizando a notificação o PARENTE DO PACIENTE AGUARDE.....')

                                    sleep(2)
                                    print('Realizar exames...')
                                    sleep(2)
                                    print('\033[31mO SISTEMA INDENTIFICOU SUSPEITA DE COVID-19')
                                    print('\033[33mO paciente deve entrar em quarentena')
                                    sleep(2)
                                    print('\033[33mAcionando a equipe..\nAGUARDE...')

                                    print('\033[32mA(o) {} do paciente {}'.format(dados_pacientes['responsavel'],
                                                                          dados_pacientes['nome']))
                                    print('\033[32mPelo telefone {}.'.format(dados_pacientes['telefone_responsavel']))
                                    print('\033[32mData da notificação {}'.format(date.today()))

                                    opcao = str(input('Possui plano de saúde? [ 1 ] SIM e [ 2 ] Não: '))

                                    if opcao == 1:
                                        print(
                                            '\033[33m Realizando busca do prontuário do(a) paciente {} encontado na base de dados do SUS.'
                                            .format(dados_pacientes['nome']))
                                        sleep(1)
                                        print('Dados encontrado')
                                    else:
                                        dados_pacientes['plano'] = str(
                                            input('Qual o seu plano {}:'.format(dados_pacientes['nome'])))
                                        print(
                                            '\033[33m Realizando busca do prontuário do(a) paciente {} encontado base de dados do plano de saúde {}.'
                                            .format(dados_pacientes['nome'], dados_pacientes['plano']))
                                        sleep(1)
                                        print('Dados encontrado')

                            else:

                                print('\033[32mO recomendado é ficar em casa sem contato com outras pessoas.')
                                sleep(3)
                                print('Realizando a notificação o PARENTE DO PACIENTE AGUARDE.....')
                                sleep(3)
                                print('\033[32mA(o) {} do paciente {}'.format(dados_pacientes['responsavel'],
                                                                      dados_pacientes['nome']))
                                print('\033[32mPelo telefone {}.'.format(dados_pacientes['telefone_responsavel']))
                                print('\033[32mData da notificação {}'.format(date.today()))
                        else:
                            espaco()
                            sleep(2)
                            print('\033[33mRealizando pré-diagnóstico  AGUARDE...............')
                            sleep(2)
                            print('Encaminhando o paciente {} para casa'.format(dados_pacientes['nome']))
                            espaco()
                            print('\33[33mPré-diagnostico identificado com os sintomas com GRIPE tipo A')
                            print('\33[33mTRATAMENTO INDICADO: Vacina tetravalente')
            else:
                espaco()
                orientacoes()

                print('\033[32mMedidas do dia a dia')
                print(' * Lavar as mãos (dedos, unhas, punho, palma e dorso) com água e sabão, e, de preferência, utilizar toalhas de papel para secá-las;')
                print(' * Utilizar nas mãos é o álcool gel;')
                print(' * Utilizar lenço descartável para higiene nasal;')
                print(' * Evitar aglomerações;')
                print(' * etc..')
        else:
            espaco()
            orientacoes()

            print('\033[32mMedidas do dia a dia')
            print(
                ' * Lavar as mãos (dedos, unhas, punho, palma e dorso) com água e sabão, e, de preferência, utilizar toalhas de papel para secá-las;')
            print(' * Utilizar nas mãos é o álcool gel;')
            print(' * Utilizar lenço descartável para higiene nasal;')
            print(' * Evitar aglomerações;')
            print(' * etc..')
    else:
        dados_pacientes['contato'] = \
        str(input('Esteve algum contato com as pessoas infectadas? [SIM/NÃO]: ')).strip().upper()[0]
        if dados_pacientes['contato'] == 'S':
            print('\nInforme o DADOS para contato..\n')

            x = 1
            while x <= 2:
                dados_pacientes['pessoa'] = str(input('Nome da {}º pessoa:  '.format(x)))
                dados_pacientes['Telefone'] = str(input('Telefone da {}º pessoa: '.format(x)))
                x += 1

            sleep(2)
            print('Enviando dados das pessoas do(a) {} para os AGENTES DE SAÚDE. \nAGUARDE...'.format(
                dados_pacientes['nome']))
            sleep(2)
            print('Enviando dados das pessoas do(a) {} para os AGENTES DE EPIDEMIA NO LOCAL. \nAGUARDE...'.format(
                dados_pacientes['nome']))
            sleep(2)
            print('Enviando dados das pessoas do(a) {} para POLÍCIA CIVIL E MILITAR. \nAGUARDE...'.format(
                dados_pacientes['nome']))
            sleep(2)
            print('\033[32mDADOS ENVIADOS AOS DEPARTAMENTOS DE PANDEMIA DO COVID-19')
            sleep(1)
            print('Os contatos de {} serão localizados e mapeados'.format(dados_pacientes['nome']))

            print('Seguir com o diagnostico')

            dados_pacientes['doentes'] = str(input('Esteve ou esta se sentindo mal? [SIM/NÃO]: ')).strip().upper()[0]
            if dados_pacientes['doentes'] == 'S':
                dados_pacientes['tempo_doentes'] = int(input('Quanto tempo? '))
                if dados_pacientes['tempo_doentes'] > 8:
                    print('\033[33mAtenção')

            else:
                dados_pacientes['doenca_gripe'] = \
                str(input('Teve grip nos ultimos 3 mêses? [SIM/NÃO]: ')).upper().strip()[0]
                if dados_pacientes['doenca_gripe'] == 'S':
                    dados_pacientes['febre'] = str(input('Esta com FEBRE? [SIM/NÃO]: ')).strip().upper()[0]
                    dados_pacientes['temperatura_febre'] = int(input('Qual a temperatura da febre ºC: '))
                    dados_pacientes['tosse'] = str(input('Esta com TOSSE? [SIM/NÃO]: ')).strip().upper()[0]
                    dados_pacientes['dor_de_garganta'] = \
                    str(input('Teve DOR DE GARGANTA? [SIM/NÃO]: ')).strip().upper()[0]

                    if dados_pacientes['febre'] == 'S' and dados_pacientes['tosse'] == 'S' and dados_pacientes[
                        'dor_de_garganta'] == 'S':
                        espaco()
                        sleep(2)
                        print('\033[33mRealizando pré-diagnóstico  AGUARDE...............')
                        sleep(2)
                        print('Mais uma pergunta..')
                        dados_pacientes['respiracao'] = \
                        str(input('Tem DIFICULDADE DE RESPIRAR? [SIM/NÃO]: ')).strip().upper()[0]
                        if dados_pacientes['respiracao'] == 'S' and dados_pacientes['temperatura_febre'] >= 39:
                            print('Realizando a notificação o PARENTE DO PACIENTE AGUARDE.....')

                            sleep(2)
                            print('Realizar exames...')
                            sleep(2)
                            print('\033[31mO SISTEMA INDENTIFICOU SUSPEITA DE COVID-19')
                            print('\033[33mO paciente deve entrar em quarentena')
                            sleep(2)
                            print('\033[33mAcionando a equipe..\nAGUARDE...')

                            print('A(o) {} do paciente {}'.format(dados_pacientes['responsavel'],
                                                                  dados_pacientes['nome']))
                            print('Pelo telefone {}.'.format(dados_pacientes['telefone_responsavel']))
                            print('Data da notificação {}'.format(date.today()))

                            if (dados_pacientes['idade'] >= 60) and (dados_pacientes['idade'] <= 10):
                                print('\033[31m Obs.: Paciente FAZ parte do GRUPO DE RISCO.')
                                sleep(1)
                                opcao = str(input('Possui plano de saúde? [ 1 ] SIM e [ 2 ] Não: '))

                                if opcao == 1:
                                    print(
                                        '\033[33m Realizando busca do prontuário do(a) paciente {} encontado na base de dados do SUS.'
                                            .format(dados_pacientes['nome']))
                                    sleep(1)
                                    print('Dados encontrado')
                                    sleep(1)
                                else:
                                    dados_pacientes['plano'] = str(
                                        input('Qual o seu plano {}:'.format(dados_pacientes['nome'])))
                                    print(
                                        '\033[33m Realizando busca do prontuário do(a) paciente {} encontado base de dados do plano de saúde {}.'
                                            .format(dados_pacientes['nome'], dados_pacientes['plano']))
                                    sleep(1)
                                    print('Dados encontrado')
                                print('')
                            else:
                                print('\033[32m Obs.: Paciente FORA do GRUPO DE RISCO.')

                                sleep(1)

                                print('Realizando a notificação o PARENTE DO PACIENTE AGUARDE.....')

                                sleep(2)
                                print('Realizar exames...')
                                sleep(2)
                                print('\033[31mO SISTEMA INDENTIFICOU SUSPEITA DE COVID-19')
                                print('\033[33mO paciente deve entrar em quarentena')
                                sleep(2)
                                print('\033[33mAcionando a equipe..\nAGUARDE...')

                                print('\033[32mA(o) {} do paciente {}'.format(dados_pacientes['responsavel'],
                                                                              dados_pacientes['nome']))
                                print('\033[32mPelo telefone {}.'.format(dados_pacientes['telefone_responsavel']))
                                print('\033[32mData da notificação {}'.format(date.today()))

                                opcao = str(input('Possui plano de saúde? [ 1 ] SIM e [ 2 ] Não: '))

                                if opcao == 1:
                                    print(
                                        '\033[33m Realizando busca do prontuário do(a) paciente {} encontado na base de dados do SUS.'
                                            .format(dados_pacientes['nome']))
                                    sleep(1)
                                    print('Dados encontrado')
                                else:
                                    dados_pacientes['plano'] = str(
                                        input('Qual o seu plano {}:'.format(dados_pacientes['nome'])))
                                    print(
                                        '\033[33m Realizando busca do prontuário do(a) paciente {} encontado base de dados do plano de saúde {}.'
                                            .format(dados_pacientes['nome'], dados_pacientes['plano']))
                                    sleep(1)
                                    print('Dados encontrado')

                        else:

                            print('\033[32mO recomendado é ficar em casa sem contato com outras pessoas.')
                            sleep(3)
                            print('Realizando a notificação o PARENTE DO PACIENTE AGUARDE.....')
                            sleep(3)
                            print('\033[32mA(o) {} do paciente {}'.format(dados_pacientes['responsavel'],
                                                                          dados_pacientes['nome']))
                            print('\033[32mPelo telefone {}.'.format(dados_pacientes['telefone_responsavel']))
                            print('\033[32mData da notificação {}'.format(date.today()))
                    else:
                        espaco()
                        sleep(2)
                        print('\033[33mRealizando pré-diagnóstico  AGUARDE...............')
                        sleep(2)
                        print('Encaminhando o paciente {} para casa'.format(dados_pacientes['nome']))
                        espaco()
                        print('\33[33mPré-diagnostico identificado com os sintomas com GRIPE tipo A')
                        print('\33[33mTRATAMENTO INDICADO: Vacina tetravalente')
        else:
            espaco()
            orientacoes()

            print('\033[32mMedidas do dia a dia')
            print(
                ' * Lavar as mãos (dedos, unhas, punho, palma e dorso) com água e sabão, e, de preferência, utilizar toalhas de papel para secá-las;')
            print(' * Utilizar nas mãos é o álcool gel;')
            print(' * Utilizar lenço descartável para higiene nasal;')
            print(' * Evitar aglomerações;')
            print(' * etc..')



if __name__ == '__main__':

    cadastro_de_pacientes()

