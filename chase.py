import gamelib
import random
import interfaz_chase
import movilidad

ANCHO_ALTO_JUEGO = 690
ANCHO_ALTO_CELDA = 30
CENTRO_GRILLA = 11


class Juego():
    def __init__(self, jugador, bots, x, y):
        '''
        Inicia el objeto juego con :
        >>> jugador(lista de posiciones [x, y]).
        >>> bots (lista de listas de posiciones [x, y], lista vacia de colisiones).
        >>> coordenadas x e y (en píxels).
        '''
        self.jugador = jugador
        self.bot = bots
        self.x = x
        self.y = y

    def avanzar_un_step_jugador(self):
        '''
        Actualiza las coordenadas donde esta el jugador.
        '''
        movimiento_jugador = movilidad.movimiento_personaje(self.jugador, self.x, self.y, self.bot)
        return movimiento_jugador

    def avanzar_un_step_bot(self, jugador):
        '''
        Actualiza las coordenadas de los bots y las colisiones.
        '''
        y, x = jugador
        movimiento_bots = movilidad.movimiento_bot(self.bot, x, y)
        return movimiento_bots

    def teleport(self):
        '''
        Teletransporta al jugador oprimiendo "Tab" a una posición aleatoria.
        '''
        x = random.randint(0, 22)
        y = random.randint(0, 22)
        return y, x

    def jugador_gana(self, nivel):
        '''
        Si el jugador concreta con exito el nivel 5 del juego devuelve True, en caso
        contrario devuelve False.
        '''
        if nivel == 6:
            return True
        return False

    def jugador_pierde(self):
        '''
        Si el jugador es alcanzado por un bot, devuleve True, en caso contrario devuelve False.
        '''
        bots, _ = self.bot
        if tuple(self.jugador) in bots:
            return True
        return False

    def nivel_terminado(self):
        '''
        Devuelve True si todos los bots fueron eliminados.
        '''
        bots, _ = self.bot
        return len(bots) == 0

def main():
    gamelib.resize(ANCHO_ALTO_JUEGO, ANCHO_ALTO_JUEGO + 60)

    x = ANCHO_ALTO_JUEGO // 2
    y = ANCHO_ALTO_JUEGO // 2

    nivel = 1

    jugador = [CENTRO_GRILLA, CENTRO_GRILLA]

    posiciones_bot = movilidad.posiciones_bots(nivel)
    colisiones = []

    bots = [posiciones_bot, colisiones]

    juego = Juego(jugador, bots, x, y)

    while gamelib.is_alive():

        gamelib.draw_begin()
        interfaz_chase.dibujar_grilla(nivel)
        interfaz_chase.dibujar_jugador(jugador)
        interfaz_chase.dibujar_bots(bots)

        if juego.jugador_pierde():
            interfaz_chase.dibujar_pantalla_perdedor()

        if juego.jugador_gana(nivel):
            interfaz_chase.dibujar_pantalla_ganador()
            
        gamelib.draw_end()

        ev = gamelib.wait()

        if not ev:
            break

        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            #El jugador oprimió la tecla Esc.
            break

        if ev.type == gamelib.EventType.ButtonPress:
            x, y = ev.x, ev.y
            #El jugador clickeó dentro de la grilla.
            if 0 < x < ANCHO_ALTO_JUEGO and 0 < y < ANCHO_ALTO_JUEGO:

                y = y // ANCHO_ALTO_CELDA
                x = x // ANCHO_ALTO_CELDA

                juego = Juego(jugador, bots, x, y)
                jugador, colisiones = juego.avanzar_un_step_jugador()
                bots = bots[0], colisiones
                bots = juego.avanzar_un_step_bot(jugador)
                juego = Juego(jugador, bots, x, y)

        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Tab':
            #El jugador oprimió la tecla Tab.
            jugador = juego.teleport()
            bots = juego.avanzar_un_step_bot(jugador)

            lista_bots, colisiones = bots
            if tuple(jugador) in colisiones:
                juego.jugador_pierde() == True
            juego = Juego(jugador, bots, jugador[0], jugador[1])

        if juego.nivel_terminado():
            nivel += 1
            jugador = [CENTRO_GRILLA, CENTRO_GRILLA]
            posiciones_bot = movilidad.posiciones_bots(nivel)
            colisiones = []
            bots = [posiciones_bot, colisiones]
            juego = Juego(jugador, bots, x, y)

gamelib.init(main)
