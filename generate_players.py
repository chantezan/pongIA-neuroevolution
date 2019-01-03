import random
from genetica import Genetico
import time
import sys

seed_ini = sys.argv[1]
seed_range = sys.argv[2]
label = sys.argv[3]
t = time.time()
best_all = None
for i in range(int(seed_range)):
    seed = i + int(seed_ini)
    random.seed(seed)  # 17 objetivo 16
    objetivo = 16
    genetico = Genetico(objetivo, number_children=500, iteraciones=100,cantidad=[10,2]
                        ,activacion=["sigmoid","sigmoid"],dim_input=4,dim_output=1,label=label)
    print("seed-----------------------------------------------------------------", seed)

    best = genetico.run(seed)
    print("mejor", best.respuestas, best.distancia)
    if (best_all == None):
        best_all = best
    else:
        best_all = genetico.comparar(best_all, best)
    # print("cantidad encontrada",genetico.cantidad_cero)
    genetico.save(seed)
print("mejor de todos", best_all.respuestas, best_all.distancia)
print(time.time() - t)