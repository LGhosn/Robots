import gamelib

ANCHO_ALTO_JUEGO = 690
ANCHO_ALTO_CELDA = 30
CENTRO_GRILLA = 11

def dibujar_grilla(nivel):
    '''
    Dibuja las líneas que representan la superficie/grilla del juego.
    '''
    gamelib.title("CHASE")
    for lineas in range(0, ANCHO_ALTO_JUEGO + 1, ANCHO_ALTO_CELDA):
        gamelib.draw_line(0, lineas, ANCHO_ALTO_JUEGO, lineas, fill="grey")
    for lineas in range(0, ANCHO_ALTO_JUEGO + 1, ANCHO_ALTO_CELDA):
        gamelib.draw_line(lineas, 0, lineas, ANCHO_ALTO_JUEGO, fill="grey")

    gamelib.draw_text(f'N I V E L : {nivel}', ANCHO_ALTO_JUEGO - 100, ANCHO_ALTO_JUEGO + ANCHO_ALTO_CELDA)
    gamelib.draw_text('"TAB" PARA TELETRANSPORTAR', 140, ANCHO_ALTO_JUEGO + ANCHO_ALTO_CELDA)


def dibujar_jugador(jugador):
    '''
    Dibuja la posición actual del jugador.
    '''
    y, x = jugador
    gamelib.draw_image('jugador.gif', (x * ANCHO_ALTO_CELDA),
                       (y * ANCHO_ALTO_CELDA))


def dibujar_bots(bots):
    '''
    Dibuja la posición actual de los bots.
    '''
    posiciones_bots, colisiones = bots

    for y, x in colisiones:
        gamelib.draw_image('colision.gif', x *
                           ANCHO_ALTO_CELDA, y * ANCHO_ALTO_CELDA)

    for fila, columna in posiciones_bots:
        gamelib.draw_image('bot.gif', columna *
                           ANCHO_ALTO_CELDA, fila * ANCHO_ALTO_CELDA)


def dibujar_pantalla_perdedor():
    '''
    Dibuja en la pantalla un texto y la imagen que informan al jugador que perdió.
    '''
    while gamelib.is_alive():
        gamelib.draw_begin()
        gamelib.draw_text('FUISTE CAPTURADO POR LOS ROBOTS',
                          345, 150, size='22')
        gamelib.draw_image('perdedor.gif', 170, 200)
        gamelib.draw_end()


def dibujar_pantalla_ganador():
    '''
    Dibuja en la pantalla un texto y la imagen que informan al jugador que ganó.
    '''
    while gamelib.is_alive():
        gamelib.draw_begin()
        gamelib.draw_text(
            'ESCAPASTE DE LOS ROBOTS, FELICITACIONES', 345, 150, size='22')
        gamelib.draw_image('ganador.gif', 170, 200)
        gamelib.draw_end()
