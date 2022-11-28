from distancias import Distancia
from arvore import Arvore
from estado import No
from cidades import Locais

def a_estrela(Arvore, base_distancias, inicio, fim, distancia_inicial):

    lista_abertos = []
    lista_fechados = []

    no_inicial = No(nome = inicio, h = distancia_inicial)
    no_final = No(nome = fim)

    lista_abertos.append(no_inicial)

    while len(lista_abertos) > 0:
        print(f'lista abertos: {lista_abertos}\n')

        # organizar a lista em ordem crescente de funcao e pegar o menor
        lista_abertos.sort()
        no_atual = lista_abertos.pop(0)

        # inserir no atual na lista_fechados
        lista_fechados.append(no_atual)
        print(f'lista fechados: {lista_fechados}\n')

        # verificar se chegou no destino
        if no_atual == no_final:
            caminho = []
            while no_atual != no_inicial:
                caminho.append(no_atual.nome + ': ' + str(no_atual.g))
                no_atual = no_atual.pai
            caminho.append(no_inicial.nome + ': ' + str(no_inicial.g))
            return caminho[::-1]

        # verificar vizinhos
        vizinhos = Arvore.get(no_atual.nome)
        print(f'nos vizinhos: {vizinhos}\n')

        # Loop entre vizinhos
        for chave in vizinhos.keys():
            vizinho = No(chave, no_atual)
            if(vizinho in lista_fechados):
                continue
            # calculo do custo acumulado e funcao
            vizinho.g = no_atual.g + Arvore.get(no_atual.nome, vizinho.nome)
            vizinho.h = base_distancias.get(vizinho.nome)
            vizinho.f = vizinho.g + vizinho.h if vizinho.h is not None else vizinho.g
            if(inserir_lista_abertos(lista_abertos, vizinho) == True):
                lista_abertos.append(vizinho)

    # caminho nao encontrado
    return None


# verificar se vizinho deve ser incluido em lista_abertos
def inserir_lista_abertos(lista_abertos, vizinho):
    for aberto in lista_abertos:
        # f do vizinho precisa ser menor
        if (vizinho == aberto and vizinho.f > aberto.f):
            return False
    return True



def main():
    distancia_padrao = Distancia()
    arvore = Arvore()

    lista_locais = (Locais()).lista_locais
    locais = (Locais()).locais_string

    # interacao com user
    opcao_origem = input(f'{locais}Insira o código do local de origem: ')
    opcao_origem = lista_locais[int(opcao_origem) - 1]
    opcao_destino = input(f'{locais}Insira o código do destino desejado: ')
    opcao_destino = lista_locais[int(opcao_destino) - 1]
    origem = opcao_origem
    destino = opcao_destino

    # pegando distancias ja configuradas pra montar lista personalizada
    lista_destino = {}
    for item in distancia_padrao.distancias_admissivel:
        lista_destino[item] = distancia_padrao.distancias_admissivel[item][destino][0]

    # "criar" grafo de conexoes entre estadios
    arvore.ligar('Estádio_Al_Thumama', 'Ticketing_Centre_FWC2022', distancia_padrao.distancias_admissivel['Estádio_Al_Thumama']['Ticketing_Centre_FWC2022'][1] )
    arvore.ligar('Estádio_Al_Thumama', 'Estádio_Internacional_Khalifa', distancia_padrao.distancias_admissivel['Estádio_Al_Thumama']['Estádio_Internacional_Khalifa'][1] )
    arvore.ligar('Estádio_Al_Thumama', 'Estádio_974', distancia_padrao.distancias_admissivel['Estádio_Al_Thumama']['Estádio_974'][1] )
    arvore.ligar('Estádio_Internacional_Khalifa', 'Al_Waab_QLM', distancia_padrao.distancias_admissivel['Estádio_Internacional_Khalifa']['Al_Waab_QLM'][1] )
    arvore.ligar('Estádio_Internacional_Khalifa', 'Rayyan_Family_Park_1', distancia_padrao.distancias_admissivel['Estádio_Internacional_Khalifa']['Rayyan_Family_Park_1'][1] )
    arvore.ligar('Estádio_Internacional_Khalifa', 'Estádio_Al_Thumama', distancia_padrao.distancias_admissivel['Estádio_Internacional_Khalifa']['Estádio_Al_Thumama'][1] )
    arvore.ligar('Estádio_Cidade_da_Educação', 'Rayyan_Family_Park_1', distancia_padrao.distancias_admissivel['Estádio_Cidade_da_Educação']['Rayyan_Family_Park_1'][1] )
    arvore.ligar('Estádio_Cidade_da_Educação', 'Al_Gharrafa_Park', distancia_padrao.distancias_admissivel['Estádio_Cidade_da_Educação']['Al_Gharrafa_Park'][1] )
    arvore.ligar('Estádio_Cidade_da_Educação', 'Al_Messila_Resort', distancia_padrao.distancias_admissivel['Estádio_Cidade_da_Educação']['Al_Messila_Resort'][1] )
    arvore.ligar('Estádio_974', 'Westin_Hotel_Doha', distancia_padrao.distancias_admissivel['Estádio_974']['Westin_Hotel_Doha'][1] )
    arvore.ligar('Estádio_974', 'Fan_Fest_Doha_Park_Al_Bidda', distancia_padrao.distancias_admissivel['Estádio_974']['Fan_Fest_Doha_Park_Al_Bidda'][1] )
    arvore.ligar('Estádio_974', 'Estádio_Al_Thumama', distancia_padrao.distancias_admissivel['Estádio_974']['Estádio_Al_Thumama'][1] )
    arvore.ligar('Westin_Hotel_Doha', 'Ticketing_Centre_FWC2022', distancia_padrao.distancias_admissivel['Westin_Hotel_Doha']['Ticketing_Centre_FWC2022'][1] )
    arvore.ligar('Westin_Hotel_Doha', 'Estádio_974', distancia_padrao.distancias_admissivel['Westin_Hotel_Doha']['Estádio_974'][1] )
    arvore.ligar('Westin_Hotel_Doha', 'Fan_Fest_Doha_Park_Al_Bidda', distancia_padrao.distancias_admissivel['Westin_Hotel_Doha']['Fan_Fest_Doha_Park_Al_Bidda'][1] )
    arvore.ligar('Westin_Hotel_Doha', 'Al_Messila_Resort', distancia_padrao.distancias_admissivel['Westin_Hotel_Doha']['Al_Messila_Resort'][1] )
    arvore.ligar('Universidade_Doha', 'Al_Messila_Resort', distancia_padrao.distancias_admissivel['Universidade_Doha']['Al_Messila_Resort'][1] )
    arvore.ligar('Universidade_Doha', 'Al_Gharrafa_Park', distancia_padrao.distancias_admissivel['Universidade_Doha']['Al_Gharrafa_Park'][1] )
    arvore.ligar('Universidade_Doha', 'Fan_Fest_Doha_Park_Al_Bidda', distancia_padrao.distancias_admissivel['Universidade_Doha']['Fan_Fest_Doha_Park_Al_Bidda'][1] )
    arvore.ligar('Al_Messila_Resort', 'Ticketing_Centre_FWC2022', distancia_padrao.distancias_admissivel['Al_Messila_Resort']['Ticketing_Centre_FWC2022'][1] )
    arvore.ligar('Al_Messila_Resort', 'Fan_Fest_Doha_Park_Al_Bidda', distancia_padrao.distancias_admissivel['Al_Messila_Resort']['Fan_Fest_Doha_Park_Al_Bidda'][1] )
    arvore.ligar('Al_Messila_Resort', 'Westin_Hotel_Doha', distancia_padrao.distancias_admissivel['Al_Messila_Resort']['Westin_Hotel_Doha'][1] )
    arvore.ligar('Al_Messila_Resort', 'Al_Waab_QLM', distancia_padrao.distancias_admissivel['Al_Messila_Resort']['Al_Waab_QLM'][1] )
    arvore.ligar('Al_Messila_Resort', 'Universidade_Doha', distancia_padrao.distancias_admissivel['Al_Messila_Resort']['Universidade_Doha'][1] )
    arvore.ligar('Al_Messila_Resort', 'Estádio_Cidade_da_Educação', distancia_padrao.distancias_admissivel['Al_Messila_Resort']['Estádio_Cidade_da_Educação'][1] )
    arvore.ligar('Al_Messila_Resort', 'Al_Gharrafa_Park', distancia_padrao.distancias_admissivel['Al_Messila_Resort']['Al_Gharrafa_Park'][1] )
    arvore.ligar('Fan_Fest_Doha_Park_Al_Bidda', 'Westin_Hotel_Doha', distancia_padrao.distancias_admissivel['Fan_Fest_Doha_Park_Al_Bidda']['Westin_Hotel_Doha'][1] )
    arvore.ligar('Fan_Fest_Doha_Park_Al_Bidda', 'Al_Messila_Resort', distancia_padrao.distancias_admissivel['Fan_Fest_Doha_Park_Al_Bidda']['Al_Messila_Resort'][1] )
    arvore.ligar('Fan_Fest_Doha_Park_Al_Bidda', 'Estádio_974', distancia_padrao.distancias_admissivel['Fan_Fest_Doha_Park_Al_Bidda']['Estádio_974'][1] )
    arvore.ligar('Fan_Fest_Doha_Park_Al_Bidda', 'Universidade_Doha', distancia_padrao.distancias_admissivel['Fan_Fest_Doha_Park_Al_Bidda']['Universidade_Doha'][1] )
    arvore.ligar('Ticketing_Centre_FWC2022', 'Al_Waab_QLM', distancia_padrao.distancias_admissivel['Ticketing_Centre_FWC2022']['Al_Waab_QLM'][1] )
    arvore.ligar('Ticketing_Centre_FWC2022', 'Westin_Hotel_Doha', distancia_padrao.distancias_admissivel['Ticketing_Centre_FWC2022']['Westin_Hotel_Doha'][1] )
    arvore.ligar('Ticketing_Centre_FWC2022', 'Al_Messila_Resort', distancia_padrao.distancias_admissivel['Ticketing_Centre_FWC2022']['Al_Messila_Resort'][1] )
    arvore.ligar('Ticketing_Centre_FWC2022', 'Estádio_Al_Thumama', distancia_padrao.distancias_admissivel['Ticketing_Centre_FWC2022']['Estádio_Al_Thumama'][1] )
    arvore.ligar('Al_Waab_QLM', 'Estádio_Internacional_Khalifa', distancia_padrao.distancias_admissivel['Al_Waab_QLM']['Estádio_Internacional_Khalifa'][1] )
    arvore.ligar('Al_Waab_QLM', 'Ticketing_Centre_FWC2022', distancia_padrao.distancias_admissivel['Al_Waab_QLM']['Ticketing_Centre_FWC2022'][1] )
    arvore.ligar('Al_Waab_QLM', 'Rayyan_Family_Park_1', distancia_padrao.distancias_admissivel['Al_Waab_QLM']['Rayyan_Family_Park_1'][1] )
    arvore.ligar('Al_Waab_QLM', 'Al_Messila_Resort', distancia_padrao.distancias_admissivel['Al_Waab_QLM']['Al_Messila_Resort'][1] )
    arvore.ligar('Rayyan_Family_Park_1', 'Estádio_Internacional_Khalifa', distancia_padrao.distancias_admissivel['Rayyan_Family_Park_1']['Estádio_Internacional_Khalifa'][1] )
    arvore.ligar('Rayyan_Family_Park_1', 'Estádio_Cidade_da_Educação', distancia_padrao.distancias_admissivel['Rayyan_Family_Park_1']['Estádio_Cidade_da_Educação'][1] )
    arvore.ligar('Rayyan_Family_Park_1', 'Al_Waab_QLM', distancia_padrao.distancias_admissivel['Rayyan_Family_Park_1']['Al_Waab_QLM'][1] )
    arvore.ligar('Al_Gharrafa_Park', 'Estádio_Cidade_da_Educação', distancia_padrao.distancias_admissivel['Al_Gharrafa_Park']['Estádio_Cidade_da_Educação'][1] )
    arvore.ligar('Al_Gharrafa_Park', 'Universidade_Doha', distancia_padrao.distancias_admissivel['Al_Gharrafa_Park']['Universidade_Doha'][1] )
    arvore.ligar('Al_Gharrafa_Park', 'Al_Messila_Resort', distancia_padrao.distancias_admissivel['Al_Gharrafa_Park']['Al_Messila_Resort'][1] )
    
    # tornam arvore nao dirigida, criar ligacoes simetricas
    arvore.nao_dirigida()
    caminho = a_estrela(arvore, lista_destino, origem, destino, distancia_padrao.distancias_admissivel[origem][destino][0])
    print(caminho)

if __name__ == "__main__": main()