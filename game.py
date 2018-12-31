from PyPong import pong_grafic
from PyPong import pong
from playerAI import Player
import pickle

player = pickle.load( open( "jugadores/jugador20", "rb" ) )

pong_grafic.run(player,0.185)
