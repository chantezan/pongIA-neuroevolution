from PyPong import pong_grafic
from PyPong import pong
from playerAI import Player
import pickle

player = pickle.load( open( "jugadores/8y2/jugador21", "rb" ) )

pong_grafic.run(player,0.625)
pong_grafic.run(player,0.875)
pong_grafic.run(player,0.125)
pong_grafic.run(player,0.375)
pong_grafic.run(player,0.1)
pong_grafic.run(player,0.345)
pong_grafic.run(player,0.900)
pong_grafic.run(player,0.590)
