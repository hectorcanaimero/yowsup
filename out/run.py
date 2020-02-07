from yowsup.stacks import  YowStackBuilder
from layer import EchoLayer
from yowsup.layers import YowLayerEvent
from yowsup.layers.network import YowNetworkLayer
from yowsup.env import YowsupEnv

credentials = ("5541987752137",
               "2El/lk0c/qO34okBKJoSjBOIZGUlr1saNbshTtU2XERgEFXOgZIr2g+gKcYpI2hJhZpPKlh6IcHTrxS8gU58Jw==")

if __name__==  "__main__":
    stackBuilder = YowStackBuilder()

    stack = stackBuilder\
        .pushDefaultLayers()\
        .push(EchoLayer)\
        .build()

    stack.setCredentials(credentials)
    stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))   #sending the connect signal
    stack.loop() #this is the program mainloop