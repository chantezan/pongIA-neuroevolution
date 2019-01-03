from red import Red
import random
class Player:
    def __init__(self, red=None,cantidad = [6],activacion=["sigmoid"],dim_input=4,dim_output=1):
        self.cantidad = cantidad
        self.activacion = activacion
        self.dim_input = dim_input
        self.dim_output = dim_output
        if not(red):
            self.red = Red(cantidad=self.cantidad , activacion=self.activacion , dim_input=self.dim_input, dim_output=self.dim_output)
        else:
            self.red = red
        self.respuestas = 0
        self.distancia = 0
    def generarHijo(self,padre,mutacion):
        punto = random.randint(0, self.red.total_neuronas)
        red_aux = Red(cantidad=self.cantidad, activacion=self.activacion, dim_input=self.dim_input, dim_output=self.dim_output)
        index_capa = 0
        cantidad_recorrida = 0
        for neuronas_capa_i in red_aux.capas:
            index_neurona = 0
            for neurona_capa_i in neuronas_capa_i:
                if not(random.randint(1, 100) <= mutacion):
                    if(cantidad_recorrida < punto):
                        neurona_capa_i.peso = self.red.capas[index_capa][index_neurona].peso
                        neurona_capa_i.bias = self.red.capas[index_capa][index_neurona].bias
                    else:
                        neurona_capa_i.peso = padre.red.capas[index_capa][index_neurona].peso
                        neurona_capa_i.bias = padre.red.capas[index_capa][index_neurona].bias
                index_neurona += 1
                cantidad_recorrida += 1
            index_capa += 1
        return Player(red=red_aux,
                      cantidad=self.cantidad, activacion=self.activacion, dim_input=self.dim_input, dim_output=self.dim_output)

    def movimiento(self,datos):
        resp = self.red.forward(datos)
        if(resp[0] > 0.5):
            return 1
        else:
            return 0

    def agregarDistancia(self,d):
        self.distancia += d

    def agregarRespuesta(self):
        self.respuestas += 1