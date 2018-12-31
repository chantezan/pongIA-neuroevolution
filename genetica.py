import random
import string
import matplotlib.pyplot as plt
import time
from playerAI import Player
from PyPong import pong
import pickle

class Genetico:
    def __init__(self, generador, objetivo, number_children=10, iteraciones=1000):
        self.generador = generador
        self.objetivo = objetivo
        self.number_children = number_children
        self.number_sampling = int(number_children * 3 / 4)
        self.iteraciones = iteraciones
        self.valores = []
        self.promedios = []
        self.encontrado = False

    def iniciar(self):
        lista = []
        suma = 0
        self.cantidad_cero = 0
        for i in range(self.number_children):
            jugador = Player()
            self.fitness(jugador)
            suma += jugador.respuestas
            lista.append(jugador)
        self.promedios.append(suma * 1.0 / self.number_children)
        return lista

    #fitness es la cantidad de tiempo que juega
    def fitness(self, hijo):
        pong.run(hijo,0.625)
        pong.run(hijo,0.875)
        pong.run(hijo,0.125)
        pong.run(hijo,0.375)

    def torneo(self, generados_evaluados):
        best = None
        best_fit = -1
        for indice in range(self.number_sampling):
            aux = random.randint(0, self.number_children - 1)
            aux_object = generados_evaluados[aux]
            if (best == None):
                best = aux_object
            else:
                best = self.comparar(best,aux_object)
        return best

    def comparar(self,hijo1,hijo2):
        #or (hijo1.respuestas <= 2 and hijo2.respuestas <= 2)
        if(hijo1.respuestas == hijo2.respuestas ):
            if(hijo1.distancia < hijo2.distancia):
                return hijo1
            else:
                return hijo2
        if (hijo1.respuestas > hijo2.respuestas):
            return hijo1
        else:
            return hijo2

    def generarHijos(self, padre1, padre2):
        hijos = []
        probabilidad_mutation = 1
        self.valores = []
        suma = 0
        self.cantidad_cero = 0
        for indice in range(self.number_children):
            hijo = padre1.generarHijo(padre2,probabilidad_mutation)
            self.fitness(hijo)
            suma += hijo.respuestas
            hijos.append(hijo)
        self.promedios.append(suma * 1.0 / self.number_children)
        return hijos

    def run(self,iteracion):
        tiempo_inicial = time.time()
        aleatorios = self.iniciar()
        j = 0
        best_all = None
        iteracion_iguales = 0
        while (self.iteraciones > j):
            j += 1
            terminar = False
            solucion = None
            indice = 0

            for fit in aleatorios:
                if (fit.respuestas == self.objetivo):
                    solucion = aleatorios[indice]
                    terminar = True
                    file = open('jugadores/jugador' + str(iteracion), 'wb')
                    pickle.dump(best_all, file, pickle.HIGHEST_PROTOCOL)
                    file.close()
            if (terminar):
                self.encontrado = True
                print("solucion encontrada", solucion)
                break
            condicion = False
            if(len(self.promedios)> 30):
                condicion = True
                for i in range(2,15):
                    if(self.promedios[-1] + 0.5 < self.promedios[-i] or self.promedios[-1] - 0.5 > self.promedios[-i]):
                        condicion = False

            if(condicion):
                print("sin mejoras")
                break
            if(self.cantidad_cero > self.number_children / 2):
                print("encontradas soluciones")
                break
            padre1 = self.torneo(aleatorios)
            padre2 = self.torneo(aleatorios)
            mejor_aux = self.comparar(padre1,padre2)
            if(best_all == None):
                best_all = mejor_aux
                file = open('jugadores/jugador' + str(iteracion), 'wb')
                pickle.dump(best_all, file, pickle.HIGHEST_PROTOCOL)
                file.close()
                print("mejor", best_all.respuestas, best_all.distancia)
            elif(best_all != self.comparar(mejor_aux,best_all)):
                best_all = self.comparar(mejor_aux,best_all)
                file = open('jugadores/jugador' + str(iteracion), 'wb')
                pickle.dump(best_all, file, pickle.HIGHEST_PROTOCOL)
                file.close()
                print("mejor", best_all.respuestas, best_all.distancia)
            aleatorios = self.generarHijos(padre1, padre2)
        self.iter = j
        self.duracion = int(time.time() * 100 - tiempo_inicial * 100) / 100
        print(self.promedios)

    def save(self, rand):
        if (self.encontrado):
            enc = "Encontrado"
            n = 1
        else:
            enc = "No Encontrado"
            n = 0
        plt.figure()
        plt.title(str(rand) + ": " + str(self.objetivo) + " Reinas - iteraciones: " + str(self.iter) + ", " + str(
            self.duracion) + "s, " + enc)
        plt.plot(range(0, len(self.promedios)), self.promedios)
        plt.savefig("Q" + str(self.objetivo) + "R" + str(rand) + "F" + str(n))
        file = open("datos2.txt", "a")
        file.write(
            "Reinas:" + str(self.objetivo) + "\t" "Solucion:" + enc + "\t" + "tiempo:" + str(self.duracion) + "\n")
        file.close()


def generator_string_number():
    return random.choice(string.ascii_lowercase + ' ' + string.digits)


def generator_string():
    return random.choice(string.ascii_lowercase + ' ')


def generator_byte():
    return random.randint(0, 1)


def generador_queen(n):
    return random.randint(0, n - 1)


for i in range(40):
    seed = i + 46
    random.seed(seed)  # 17 objetivo 16
    objetivo = 30
    genetico = Genetico(generador_queen, objetivo, number_children=50, iteraciones=500)
    print("seed-----------------------------------------------------------------", seed)
    # print genetico.fitness("2031")
    # print genetico.fitness("2013")
    # print genetico.fitness("3102")
    genetico.run(seed)
    #print("cantidad encontrada",genetico.cantidad_cero)
    #genetico.save(i)
