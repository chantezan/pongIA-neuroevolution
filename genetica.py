import random
import string
import matplotlib.pyplot as plt
import time
from playerAI import Player
from PyPong import pong
import pickle

class Genetico:
    def __init__(self, objetivo,label="6",number_children=10, iteraciones=1000,cantidad = [6],activacion=["sigmoid"],dim_input=4,dim_output=1):
        self.objetivo = objetivo
        self.number_children = number_children
        self.number_sampling = int(number_children * 3 / 4)
        self.iteraciones = iteraciones
        self.valores = []
        self.promedios = []
        self.encontrado = False
        self.best_player = None
        self.cantidad = cantidad
        self.activacion = activacion
        self.dim_input = dim_input
        self.dim_output = dim_output
        self.label = label

    def iniciar(self):
        lista = []
        suma = 0
        for i in range(self.number_children):
            jugador = Player(cantidad = self.cantidad,activacion=self.activacion,dim_input=self.dim_input,dim_output=self.dim_output)
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
        pong.run(hijo, 0.1)
        pong.run(hijo, 0.345)
        pong.run(hijo, 0.590)
        pong.run(hijo, 0.900)

    def torneo(self, generados_evaluados):
        best = None
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
        suma = 0
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
                if (fit.respuestas >= self.objetivo):
                    solucion = aleatorios[indice]
                    terminar = True
                    best_all = fit
                    file = open('jugadores/'+self.label+'/jugador' + str(iteracion), 'wb')
                    pickle.dump(best_all, file, pickle.HIGHEST_PROTOCOL)
                    file.close()
            if (terminar):
                self.encontrado = True
                print("solucion encontrada", solucion)
                break
            condicion = False
            if(len(self.promedios)> 50):
                condicion = True
                for i in range(2,15):
                    if(self.promedios[-1] + 0.5 < self.promedios[-i] or self.promedios[-1] - 0.5 > self.promedios[-i]):
                        condicion = False

            if(condicion):
                print("sin mejoras")
                break
            padre1 = self.torneo(aleatorios)
            padre2 = self.torneo(aleatorios)
            mejor_aux = self.comparar(padre1,padre2)
            if(best_all == None):
                best_all = mejor_aux
                file = open('jugadores/'+self.label+'/jugador' + str(iteracion), 'wb')
                pickle.dump(best_all, file, pickle.HIGHEST_PROTOCOL)
                file.close()
                #print("mejor", best_all.respuestas, best_all.distancia)
            elif(best_all != self.comparar(mejor_aux,best_all)):
                best_all = self.comparar(mejor_aux,best_all)
                file = open('jugadores/'+self.label+'/jugador' + str(iteracion), 'wb')
                pickle.dump(best_all, file, pickle.HIGHEST_PROTOCOL)
                file.close()
                #print("mejor", best_all.respuestas, best_all.distancia)
            aleatorios = self.generarHijos(padre1, padre2)
            if(j%25 == 0):
                print(j)
        self.iter = j
        self.duracion = int(time.time() * 100 - tiempo_inicial * 100) / 100
        self.best_player = best_all
        return self.best_player

    def save(self, rand):
        plt.figure()
        plt.title(str(rand) + ": " + str(self.objetivo) + " Pong - iteraciones: " + str(self.iter) + ", " + str(
            self.duracion) + "s, Resp" +str(self.best_player.respuestas))
        plt.plot(range(0, len(self.promedios)), self.promedios)
        plt.savefig("plot/"+self.label+"/R" + str(rand) + "B" + str(self.best_player.respuestas))