import random

def movimiento_personaje(posicion_actual, x, y, bots):
    '''
    Recibe la posición actual del jugador y las coordenadas X e Y donde se ejecuta el clíck.
    Devuelve la nueva posición del jugador y si el jugador se mueva hacia donde hay una estructura,
    la desplaza una unidad en la dirección correspondiente.
    '''
    bot, colisiones = bots

    antes_de_mover = posicion_actual

    fila_actual, columna_actual = posicion_actual

    if x < columna_actual:
        posicion_actual = [fila_actual, columna_actual - 1]

    if x > columna_actual:
        posicion_actual = [fila_actual, columna_actual + 1]

    if y < fila_actual:
        posicion_actual = [fila_actual - 1, columna_actual]

    if y > fila_actual:
        posicion_actual = [fila_actual + 1, columna_actual]

    if y < fila_actual and x < columna_actual:
        posicion_actual = [fila_actual - 1, columna_actual - 1]

    if y < fila_actual and x > columna_actual:
        posicion_actual = [fila_actual - 1, columna_actual + 1]

    if y > fila_actual and x < columna_actual:
        posicion_actual = [fila_actual + 1, columna_actual - 1]

    if y > fila_actual and x > columna_actual:
        posicion_actual = [fila_actual + 1, columna_actual + 1]

    if tuple(posicion_actual) in colisiones:
        for i in range(len(colisiones)):
            if colisiones[i] == tuple(posicion_actual):
                fila_act_colision, columna_act_colision = (posicion_actual[0] + (posicion_actual[0] - antes_de_mover[0]), posicion_actual[1] + (posicion_actual[1] - antes_de_mover[1]))

                if 0 <= fila_act_colision <= 22 and 0 <= columna_act_colision <= 22 and not (fila_act_colision, columna_act_colision) in bot:
                    colisiones[i] = fila_act_colision, columna_act_colision

                else:
                    posicion_actual = antes_de_mover
    return posicion_actual, colisiones


def movimiento_bot(posiciones_bots, x, y):
    '''
    Recibe la posición actual de los bots y las colisiones además  de las coordenadas X e Y donde se ejecuta el clíck.
    Devuelve las nuevas posiciones de los bots y en caso de producirse una colisión, la lista de coordenadas donde hay colisiones.
    '''
    posiciones_actual_bots, colisiones = posiciones_bots

    nuevas_posicones_bot = []

    for posiciones in posiciones_actual_bots:
        fila_bot, columna_bot = posiciones

        if fila_bot == y and columna_bot < x:
            posiciones = fila_bot, columna_bot + 1

        if fila_bot == y and columna_bot > x:
            posiciones = fila_bot, columna_bot - 1

        if fila_bot > y and columna_bot == x:
            posiciones = fila_bot - 1, columna_bot

        if fila_bot < y and columna_bot == x:
            posiciones = fila_bot + 1, columna_bot

        if fila_bot < y and columna_bot < x:
            posiciones = fila_bot + 1, columna_bot + 1

        if fila_bot > y and columna_bot < x:
            posiciones = fila_bot - 1, columna_bot + 1

        if fila_bot > y and columna_bot > x:
            posiciones = fila_bot - 1, columna_bot - 1

        if fila_bot < y and columna_bot > x:
            posiciones = fila_bot + 1, columna_bot - 1

        if posiciones in colisiones:
            colisiones.append(posiciones)

        elif posiciones in nuevas_posicones_bot:
            colisiones.append(posiciones)
            i = nuevas_posicones_bot.index(posiciones)
            nuevas_posicones_bot.remove(nuevas_posicones_bot[i])
        else:
            nuevas_posicones_bot.append(posiciones)
    return [nuevas_posicones_bot, colisiones]


def posiciones_bots(nivel):
    '''
    Genera las posiciones aleatorias donde al comenzar el nivel, habran bots.
    '''
    bots = []
    while len(bots) < (4 * nivel):
        x = random.randint(0, 22)
        y = random.randint(0, 22)
        coordenadas = [y, x]

        if coordenadas not in bots and coordenadas != [11, 11]:
            bots.append(coordenadas)
    return sorted(bots)
