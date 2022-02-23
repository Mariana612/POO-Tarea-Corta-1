from Ficha import *

class Tablero:
    '''
    La idea es tener un juego sencillo que podamosprogramar en un ciclo lanzando dados
    para cada jugador hasta quealguno llegue a la casilla final. La clase ficha representará a un juga-dor en el
    tablero, por lo que debe tener algún atributo identificador.Además debe recordar"su propia posición en el tablero.
    La clase Ta-blero es un conjunto de posiciones o casillas y debe tener atributosque indiquen por ejemplo
    cuántas casillas son en total, cuántos juga-dores son y el orden.
'''
    fichas = []
    cantidad_casillas = 20

    def __init__(self):
        jugador1 = Ficha("rojo")
        jugador2 = Ficha("azul")

        self.fichas = [jugador1,jugador2]
        self.moverFicha()

    def moverFicha(self):
        count = 0
        while self.fichas[0].posicion <= self.cantidad_casillas and self.fichas[1].posicion <= self.cantidad_casillas:
            count += 1
            print("ronda" + " " + str(count))
            for i in self.fichas:
                i.avanzar()
                if i.posicion >= 20:
                    print("genial cano el jugador" + " " + i.color)
                    break




