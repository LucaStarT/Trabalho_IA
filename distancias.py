class Distancia:
    distancias_admissivel = {                 
        'Estádio_Al_Thumama':                                                   {'Estádio_Al_Thumama': (0,0), 'Estádio_Internacional_Khalifa': (9,13), 'Estádio_Cidade_da_Educação': (14,15), 'Estádio_974': (7,17), 'Westin_Hotel_Doha': (5,9), 'Universidade_Doha': (15,21),  'Al_Messila_Resort': (9,13), 'Fan_Fest_Doha_Park_Al_Bidda': (7,16), 'Ticketing_Centre_FWC2022': (6,8), 'Al_Waab_QLM': (7,12), 'Rayyan_Family_Park_1': (12,17), 'Al_Gharrafa_Park': (16,20)}, 
        'Estádio_Internacional_Khalifa':                                        {'Estádio_Al_Thumama': (9,13), 'Estádio_Internacional_Khalifa': (0,0), 'Estádio_Cidade_da_Educação': (6,8), 'Estádio_974': (12,24), 'Westin_Hotel_Doha': (7,8), 'Universidade_Doha': (11,15),  'Al_Messila_Resort': (5,10), 'Fan_Fest_Doha_Park_Al_Bidda': (8,11), 'Ticketing_Centre_FWC2022': (4,6), 'Al_Waab_QLM': (2,3), 'Rayyan_Family_Park_1': (4,5), 'Al_Gharrafa_Park': (9,14)},  
        'Estádio_Cidade_da_Educação':                                           {'Estádio_Al_Thumama': (14,15), 'Estádio_Internacional_Khalifa': (6,8), 'Estádio_Cidade_da_Educação': (0,0), 'Estádio_974': (14,18), 'Westin_Hotel_Doha': (10,14), 'Universidade_Doha': (8,8),  'Al_Messila_Resort': (5,10), 'Fan_Fest_Doha_Park_Al_Bidda': (10,10), 'Ticketing_Centre_FWC2022': (8,8), 'Al_Waab_QLM': (7,9), 'Rayyan_Family_Park_1': (2,5), 'Al_Gharrafa_Park': (4,6)},
        'Estádio_974':                                                          {'Estádio_Al_Thumama': (7,17), 'Estádio_Internacional_Khalifa': (12,24), 'Estádio_Cidade_da_Educação': (14,18), 'Estádio_974': (0,0), 'Westin_Hotel_Doha': (6,6), 'Universidade_Doha': (12,22),  'Al_Messila_Resort': (9,12), 'Fan_Fest_Doha_Park_Al_Bidda': (5,11), 'Ticketing_Centre_FWC2022': (8,13), 'Al_Waab_QLM': (10,16), 'Rayyan_Family_Park_1': (14,17), 'Al_Gharrafa_Park': (15,27)},
        'Westin_Hotel_Doha':                                                    {'Estádio_Al_Thumama': (5,9), 'Estádio_Internacional_Khalifa': (7,8), 'Estádio_Cidade_da_Educação': (10,14), 'Estádio_974': (6,6), 'Westin_Hotel_Doha': (0,0), 'Universidade_Doha': (10,16),  'Al_Messila_Resort': (5,7), 'Fan_Fest_Doha_Park_Al_Bidda': (3,6), 'Ticketing_Centre_FWC2022': (2,5), 'Al_Waab_QLM': (5,9), 'Rayyan_Family_Park_1': (9,12), 'Al_Gharrafa_Park': (11,16)},
        'Universidade_Doha':                                                    {'Estádio_Al_Thumama': (15,21), 'Estádio_Internacional_Khalifa': (11,15), 'Estádio_Cidade_da_Educação': (8,8), 'Estádio_974': (12,22), 'Westin_Hotel_Doha': (10,16), 'Universidade_Doha': (0,0),  'Al_Messila_Resort': (5,10), 'Fan_Fest_Doha_Park_Al_Bidda': (8,13), 'Ticketing_Centre_FWC2022': (10,17), 'Al_Waab_QLM': (10,17), 'Rayyan_Family_Park_1': (9,15), 'Al_Gharrafa_Park': (5,10)},
        'Al_Messila_Resort':                                                    {'Estádio_Al_Thumama': (9,13), 'Estádio_Internacional_Khalifa': (5,10), 'Estádio_Cidade_da_Educação': (5,10), 'Estádio_974': (9,12), 'Westin_Hotel_Doha': (5,7), 'Universidade_Doha': (5,10),  'Al_Messila_Resort': (0,0), 'Fan_Fest_Doha_Park_Al_Bidda': (4,6), 'Ticketing_Centre_FWC2022': (4,6), 'Al_Waab_QLM': (4,7), 'Rayyan_Family_Park_1': (5,7), 'Al_Gharrafa_Park': (6,11)},
        'Fan_Fest_Doha_Park_Al_Bidda':                                          {'Estádio_Al_Thumama': (7,16), 'Estádio_Internacional_Khalifa': (8,11), 'Estádio_Cidade_da_Educação': (10,10), 'Estádio_974': (5,11), 'Westin_Hotel_Doha': (3,6), 'Universidade_Doha': (8,13),  'Al_Messila_Resort': (4,6), 'Fan_Fest_Doha_Park_Al_Bidda': (0,0), 'Ticketing_Centre_FWC2022': (4,6), 'Al_Waab_QLM': (6,9), 'Rayyan_Family_Park_1': (9,11), 'Al_Gharrafa_Park': (10,14)},  
        'Ticketing_Centre_FWC2022':                                             {'Estádio_Al_Thumama': (6,8), 'Estádio_Internacional_Khalifa': (4,6), 'Estádio_Cidade_da_Educação': (8,8), 'Estádio_974': (8,13), 'Westin_Hotel_Doha': (2,5), 'Universidade_Doha': (10,17),  'Al_Messila_Resort': (4,6), 'Fan_Fest_Doha_Park_Al_Bidda': (4,6), 'Ticketing_Centre_FWC2022': (0,0), 'Al_Waab_QLM': (2,4), 'Rayyan_Family_Park_1': (7,10), 'Al_Gharrafa_Park': (10,14)},
        'Al_Waab_QLM':                                                          {'Estádio_Al_Thumama': (7,12), 'Estádio_Internacional_Khalifa': (2,3), 'Estádio_Cidade_da_Educação': (7,9), 'Estádio_974': (10,16), 'Westin_Hotel_Doha': (5,9), 'Universidade_Doha': (10,17),  'Al_Messila_Resort': (4,7), 'Fan_Fest_Doha_Park_Al_Bidda': (6,9), 'Ticketing_Centre_FWC2022': (2,4), 'Al_Waab_QLM': (0,0), 'Rayyan_Family_Park_1': (5,7), 'Al_Gharrafa_Park': (10,13)},         
        'Rayyan_Family_Park_1':                                                 {'Estádio_Al_Thumama': (12,17), 'Estádio_Internacional_Khalifa': (4,5), 'Estádio_Cidade_da_Educação': (2,5), 'Estádio_974': (14,17), 'Westin_Hotel_Doha': (9,12), 'Universidade_Doha': (9,15),  'Al_Messila_Resort': (5,7), 'Fan_Fest_Doha_Park_Al_Bidda': (9,11), 'Ticketing_Centre_FWC2022': (7,10), 'Al_Waab_QLM': (5,7), 'Rayyan_Family_Park_1': (0,0), 'Al_Gharrafa_Park': (6,11)},   
        'Al_Gharrafa_Park':                                                     {'Estádio_Al_Thumama': (16,20), 'Estádio_Internacional_Khalifa': (9,14), 'Estádio_Cidade_da_Educação': (4,6), 'Estádio_974': (15,27), 'Westin_Hotel_Doha': (11,16), 'Universidade_Doha': (5,10),  'Al_Messila_Resort': (6,11), 'Fan_Fest_Doha_Park_Al_Bidda': (10,14), 'Ticketing_Centre_FWC2022': (10,14), 'Al_Waab_QLM': (10,13), 'Rayyan_Family_Park_1': (6,11), 'Al_Gharrafa_Park': (0,0)},   
    }

    distancias_inadmissivel = {                 
        'Estádio_Al_Thumama':                                                   {'Estádio_Al_Thumama': (0,0), 'Estádio_Internacional_Khalifa': (9,26), 'Estádio_Cidade_da_Educação': (14,30), 'Estádio_974': (7,34), 'Westin_Hotel_Doha': (5,18), 'Universidade_Doha': (15,42),  'Al_Messila_Resort': (9,26), 'Fan_Fest_Doha_Park_Al_Bidda': (7,32), 'Ticketing_Centre_FWC2022': (6,16), 'Al_Waab_QLM': (7,24), 'Rayyan_Family_Park_1': (12,34), 'Al_Gharrafa_Park': (16,40)}, 
        'Estádio_Internacional_Khalifa':                                        {'Estádio_Al_Thumama': (9,26), 'Estádio_Internacional_Khalifa': (0,0), 'Estádio_Cidade_da_Educação': (6,16), 'Estádio_974': (12,48), 'Westin_Hotel_Doha': (7,16), 'Universidade_Doha': (11,30),  'Al_Messila_Resort': (5,20), 'Fan_Fest_Doha_Park_Al_Bidda': (8,22), 'Ticketing_Centre_FWC2022': (4,12), 'Al_Waab_QLM': (2,6), 'Rayyan_Family_Park_1': (4,10), 'Al_Gharrafa_Park': (9,28)},  
        'Estádio_Cidade_da_Educação':                                           {'Estádio_Al_Thumama': (14,30), 'Estádio_Internacional_Khalifa': (6,16), 'Estádio_Cidade_da_Educação': (0,0), 'Estádio_974': (14,36), 'Westin_Hotel_Doha': (10,28), 'Universidade_Doha': (8,16),  'Al_Messila_Resort': (5,20), 'Fan_Fest_Doha_Park_Al_Bidda': (10,20), 'Ticketing_Centre_FWC2022': (8,16), 'Al_Waab_QLM': (7,18), 'Rayyan_Family_Park_1': (2,10), 'Al_Gharrafa_Park': (4,12)},
        'Estádio_974':                                                          {'Estádio_Al_Thumama': (7,34), 'Estádio_Internacional_Khalifa': (12,48), 'Estádio_Cidade_da_Educação': (14,36), 'Estádio_974': (0,0), 'Westin_Hotel_Doha': (6,12), 'Universidade_Doha': (12,44),  'Al_Messila_Resort': (9,24), 'Fan_Fest_Doha_Park_Al_Bidda': (5,22), 'Ticketing_Centre_FWC2022': (8,26), 'Al_Waab_QLM': (10,32), 'Rayyan_Family_Park_1': (14,34), 'Al_Gharrafa_Park': (15,54)},
        'Westin_Hotel_Doha':                                                    {'Estádio_Al_Thumama': (5,18), 'Estádio_Internacional_Khalifa': (7,16), 'Estádio_Cidade_da_Educação': (10,28), 'Estádio_974': (6,12), 'Westin_Hotel_Doha': (0,0), 'Universidade_Doha': (10,32),  'Al_Messila_Resort': (5,14), 'Fan_Fest_Doha_Park_Al_Bidda': (3,12), 'Ticketing_Centre_FWC2022': (2,10), 'Al_Waab_QLM': (5,18), 'Rayyan_Family_Park_1': (9,24), 'Al_Gharrafa_Park': (11,32)},
        'Universidade_Doha':                                                    {'Estádio_Al_Thumama': (15,42), 'Estádio_Internacional_Khalifa': (11,30), 'Estádio_Cidade_da_Educação': (8,16), 'Estádio_974': (12,44), 'Westin_Hotel_Doha': (10,32), 'Universidade_Doha': (0,0),  'Al_Messila_Resort': (5,20), 'Fan_Fest_Doha_Park_Al_Bidda': (8,26), 'Ticketing_Centre_FWC2022': (10,34), 'Al_Waab_QLM': (10,34), 'Rayyan_Family_Park_1': (9,30), 'Al_Gharrafa_Park': (5,20)},
        'Al_Messila_Resort':                                                    {'Estádio_Al_Thumama': (9,26), 'Estádio_Internacional_Khalifa': (5,20), 'Estádio_Cidade_da_Educação': (5,20), 'Estádio_974': (9,24), 'Westin_Hotel_Doha': (5,14), 'Universidade_Doha': (5,20),  'Al_Messila_Resort': (0,0), 'Fan_Fest_Doha_Park_Al_Bidda': (4,12), 'Ticketing_Centre_FWC2022': (4,12), 'Al_Waab_QLM': (4,14), 'Rayyan_Family_Park_1': (5,14), 'Al_Gharrafa_Park': (6,22)},
        'Fan_Fest_Doha_Park_Al_Bidda':                                          {'Estádio_Al_Thumama': (7,32), 'Estádio_Internacional_Khalifa': (8,22), 'Estádio_Cidade_da_Educação': (10,20), 'Estádio_974': (5,22), 'Westin_Hotel_Doha': (3,12), 'Universidade_Doha': (8,26),  'Al_Messila_Resort': (4,12), 'Fan_Fest_Doha_Park_Al_Bidda': (0,0), 'Ticketing_Centre_FWC2022': (4,12), 'Al_Waab_QLM': (6,18), 'Rayyan_Family_Park_1': (9,22), 'Al_Gharrafa_Park': (10,28)},  
        'Ticketing_Centre_FWC2022':                                             {'Estádio_Al_Thumama': (6,16), 'Estádio_Internacional_Khalifa': (4,12), 'Estádio_Cidade_da_Educação': (8,16), 'Estádio_974': (8,26), 'Westin_Hotel_Doha': (2,10), 'Universidade_Doha': (10,34),  'Al_Messila_Resort': (4,12), 'Fan_Fest_Doha_Park_Al_Bidda': (4,12), 'Ticketing_Centre_FWC2022': (0,0), 'Al_Waab_QLM': (2,8), 'Rayyan_Family_Park_1': (7,20), 'Al_Gharrafa_Park': (10,28)},
        'Al_Waab_QLM':                                                          {'Estádio_Al_Thumama': (7,24), 'Estádio_Internacional_Khalifa': (2,6), 'Estádio_Cidade_da_Educação': (7,18), 'Estádio_974': (10,32), 'Westin_Hotel_Doha': (5,18), 'Universidade_Doha': (10,34),  'Al_Messila_Resort': (4,14), 'Fan_Fest_Doha_Park_Al_Bidda': (6,18), 'Ticketing_Centre_FWC2022': (2,8), 'Al_Waab_QLM': (0,0), 'Rayyan_Family_Park_1': (5,14), 'Al_Gharrafa_Park': (10,26)},         
        'Rayyan_Family_Park_1':                                                 {'Estádio_Al_Thumama': (12,34), 'Estádio_Internacional_Khalifa': (4,10), 'Estádio_Cidade_da_Educação': (2,10), 'Estádio_974': (14,34), 'Westin_Hotel_Doha': (9,24), 'Universidade_Doha': (9,30),  'Al_Messila_Resort': (5,14), 'Fan_Fest_Doha_Park_Al_Bidda': (9,22), 'Ticketing_Centre_FWC2022': (7,20), 'Al_Waab_QLM': (5,14), 'Rayyan_Family_Park_1': (0,0), 'Al_Gharrafa_Park': (6,22)},   
        'Al_Gharrafa_Park':                                                     {'Estádio_Al_Thumama': (16,40), 'Estádio_Internacional_Khalifa': (9,28), 'Estádio_Cidade_da_Educação': (4,12), 'Estádio_974': (15,54), 'Westin_Hotel_Doha': (11,32), 'Universidade_Doha': (5,20),  'Al_Messila_Resort': (6,22), 'Fan_Fest_Doha_Park_Al_Bidda': (10,28), 'Ticketing_Centre_FWC2022': (10,28), 'Al_Waab_QLM': (10,26), 'Rayyan_Family_Park_1': (6,22), 'Al_Gharrafa_Park': (0,0)},   
    }