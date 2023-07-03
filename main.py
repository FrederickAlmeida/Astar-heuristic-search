# b: blue, y: yellow, r: red, g: green
dist_real = {"e1b": {"e2b": 20},
             "e2b": {"e2y": 4, "e1b": 20, "e3b": 17},
             "e2y": {"e2b": 4, "e9y": 20, "e10y": 7},
             "e3b": {"e3r": 4, "e4b": 12.6},
             "e3r": {"e9r": 18.8, "e13r": 37.4, "e3b": 4},
             "e4b": {"e4g": 4, "e3b": 12.6, "e5b": 26},
             "e4g": {"e4b": 4, "e13g": 25.6, "e8g": 30.6},
             "e5b": {"e5y": 4, "e4b": 26, "e6b": 6},
             "e5y": {"e5b": 4, "e7y": 4.8, "e8y": 60},
             "e6b": {"e5b": 6},
             "e7y": {"e5y": 4.8},
             "e8y": {"e9y": 19.2, "e5y": 60, "e8g": 4},
             "e8g": {"e12g": 12.8, "e4g": 30.6, "e8y": 4},
             "e9y": {"e2y": 20, "e8y": 19.2, "e9r": 4},
             "e9r": {"e9y": 4, "e11r": 24.4, "e3r": 18.8},
             "e10y": {"e2y": 7},
             "e11r": {"e9r": 24.4},
             "e12g": {"e8g": 12.8},
             "e13g": {"e13r": 4, "e4g": 25.6, "e14g": 10.2},
             "e13r": {"e13g": 4, "e3r": 37.4},
             "e14g": {"e13g": 10.2}
             }

dist_direta = {
    'e1': {'e1': 0, 'e2': 20, 'e3': 37.0, 'e4': 49.6, 'e5': 72.8, 'e6': 77.6, 'e7': 71.6, 'e8': 50.8, 'e9': 35.2,
           'e10': 18.2, 'e11': 33.4, 'e12': 54.6, 'e13': 55.2, 'e14': 59.6},
    'e2': {'e1': 20, 'e2': 0, 'e3': 17.0, 'e4': 29.6, 'e5': 53.2, 'e6': 58.2, 'e7': 52.2, 'e8': 34.6, 'e9': 20.0,
           'e10': 7.0, 'e11': 31.0, 'e12': 41.8, 'e13': 38.2, 'e14': 43.6},
    'e3': {'e1': 37.0, 'e2': 17.0, 'e3': 0, 'e4': 12.6, 'e5': 36.4, 'e6': 41.2, 'e7': 35.2, 'e8': 27.2, 'e9': 18.8,
           'e10': 20.6, 'e11': 39.0, 'e12': 38.2, 'e13': 24.2, 'e14': 33.2},
    'e4': {'e1': 49.6, 'e2': 29.6, 'e3': 12.6, 'e4': 0, 'e5': 24, 'e6': 28.8, 'e7': 23.0, 'e8': 24.8, 'e9': 25.2,
           'e10': 33.4, 'e11': 47.2, 'e12': 37.2, 'e13': 21.2, 'e14': 30.8},
    'e5': {'e1': 72.8, 'e2': 53.2, 'e3': 36.4, 'e4': 24, 'e5': 0, 'e6': 6, 'e7': 4.8, 'e8': 38.8, 'e9': 46.6,
           'e10': 56.4, 'e11': 68.4, 'e12': 49.6, 'e13': 29.0, 'e14': 35.8},
    'e6': {'e1': 77.6, 'e2': 58.2, 'e3': 41.2, 'e4': 28.8, 'e5': 6, 'e6': 0, 'e7': 6.6, 'e8': 44.6, 'e9': 51.4,
           'e10': 60.6, 'e11': 73.4, 'e12': 55.2, 'e13': 30.4, 'e14': 36.4},
    'e7': {'e1': 71.6, 'e2': 52.2, 'e3': 35.2, 'e4': 23.0, 'e5': 4.8, 'e6': 6.6, 'e7': 0, 'e8': 40, 'e9': 46,
           'e10': 54.6, 'e11': 68.4, 'e12': 51.4, 'e13': 24.8, 'e14': 31.2},
    'e8': {'e1': 50.8, 'e2': 34.6, 'e3': 27.2, 'e4': 24.8, 'e5': 38.8, 'e6': 44.6, 'e7': 40, 'e8': 0, 'e9': 16.4,
           'e10': 40.6, 'e11': 32.2, 'e12': 12.8, 'e13': 45.4, 'e14': 55.2},
    'e9': {'e1': 35.2, 'e2': 20.0, 'e3': 18.8, 'e4': 25.2, 'e5': 46.6, 'e6': 51.4, 'e7': 46, 'e8': 16.4, 'e9': 0,
           'e10': 27.0, 'e11': 22.4, 'e12': 21.8, 'e13': 42.4, 'e14': 53.2},
    'e10': {'e1': 18.2, 'e2': 7.0, 'e3': 20.6, 'e4': 33.4, 'e5': 56.4, 'e6': 60.6, 'e7': 54.6, 'e8': 40.6, 'e9': 27.0,
            'e10': 0, 'e11': 35.2, 'e12': 48.4, 'e13': 37.4, 'e14': 42.4},
    'e11': {'e1': 33.4, 'e2': 31.0, 'e3': 39.0, 'e4': 47.2, 'e5': 68.4, 'e6': 73.4, 'e7': 68.4, 'e8': 32.2, 'e9': 22.4,
            'e10': 35.2, 'e11': 0, 'e12': 28.4, 'e13': 63.0, 'e14': 71.0},
    'e12': {'e1': 54.6, 'e2': 41.8, 'e3': 38.2, 'e4': 37.2, 'e5': 49.6, 'e6': 55.2, 'e7': 51.4, 'e8': 12.8, 'e9': 21.8,
            'e10': 48.4, 'e11': 28.4, 'e12': 0, 'e13': 57.6, 'e14': 67.2},
    'e13': {'e1': 55.2, 'e2': 38.2, 'e3': 24.2, 'e4': 21.2, 'e5': 29.0, 'e6': 30.4, 'e7': 24.8, 'e8': 45.4, 'e9': 42.4,
            'e10': 37.4, 'e11': 63.0, 'e12': 57.6, 'e13': 0, 'e14': 10.2},
    'e14': {'e1': 59.6, 'e2': 43.6, 'e3': 33.2, 'e4': 30.8, 'e5': 35.8, 'e6': 36.4, 'e7': 31.2, 'e8': 55.2, 'e9': 53.2,
            'e10': 42.4, 'e11': 71.0, 'e12': 67.2, 'e13': 10.2, 'e14': 0}
}

pai = {"e1b": "",
       "e2b": "",
       "e2y": "",
       "e3b": "",
       "e3r": "",
       "e4b": "",
       "e4g": "",
       "e5b": "",
       "e5y": "",
       "e6b": "",
       "e7y": "",
       "e8y": "",
       "e8g": "",
       "e9y": "",
       "e9r": "",
       "e10y": "",
       "e11r": "",
       "e12g": "",
       "e13g": "",
       "e13r": "",
       "e14g": ""
       }


def obter_distancia_estimada(no1, no2) -> float:
    distancia = dist_real[no1][no2] + dist_direta[no2[:-1]][no_final[:-1]]
    return distancia


def expandir_fronteira(fronteira):
    visitados.append(fronteira[0][0])
    for estacao in dist_real[fronteira[0][0]].keys():
        if estacao not in visitados:
            novo_no = (estacao, fronteira[0][1] + dist_real[fronteira[0][0]][estacao])
            if not any(estacao == est_dist[0] and novo_no[1] >= est_dist[1] for est_dist in fronteira):
                pai[estacao] = fronteira[0][0]
            fronteira.append(novo_no)

    fronteira = fronteira[1:]
    return fronteira


def get_sequencia(pai, nextstr):
    lista_final = []
    lista_final.append(nextstr)

    while nextstr != "":
        lista_final.append(pai[nextstr])
        nextstr = pai[nextstr]

    return lista_final[-2::-1]


fim = False
visitados = []
no_inicial = input("Digite a estação de origem: ")
no_final = input("Digite a estação de destino: ")
fronteira = [(no_inicial, 0)]
# print(fronteira)


while not fim:
    if fronteira[0][0] == no_final:
        fim = True
        fronteira_heuristica = [(estacao[0], estacao[1] + dist_direta[estacao[0][:-1]][no_final[:-1]]) for estacao in fronteira]
        print(fronteira_heuristica)
    else:
        fronteira_heuristica = [(estacao[0], estacao[1] + dist_direta[estacao[0][:-1]][no_final[:-1]]) for estacao in fronteira]
        print(fronteira_heuristica)
        fronteira = expandir_fronteira(fronteira)
        fronteira = sorted(fronteira, key=lambda x: x[1] + dist_direta[x[0][:-1]][no_final[:-1]])

print(
    f"A sequência para alcançar mais rapidamente seu destino é: {get_sequencia(pai, no_final)}, com um custo de {fronteira[0][1]:.1f} minutos!")

print(
    f"A sequência para alcançar mais rapidamente seu destino é: {get_sequencia(pai, no_final)}, com um custo de {fronteira[0][1]:.1f} minutos!")
