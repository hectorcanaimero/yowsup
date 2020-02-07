import os
from yowsup.layers.interface import YowInterfaceLayer, ProtocolEntityCallback


class ReadEchoLayer(YowInterfaceLayer):
    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):
        if messageProtocolEntity.getType() == 'text':
            self.onTextMessage(messageProtocolEntity)
        elif messageProtocolEntity.getType() == 'media':
            self.onMediaMessage(messageProtocolEntity)

        self.toLower(messageProtocolEntity.ack())
        self.toLower(messageProtocolEntity.ack(True))

    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
        self.toLower(entity.ack())

    def onTextMessage(self,messageProtocolEntity):
        # just print info
        print("Llego el mensaje %s" % (messageProtocolEntity.getBody()))
        os.system("notify-send 'Mensaje de Whatsapp' '{mensje}'".format(mensje=messageProtocolEntity.getBody()))
        os.system("espeak -ves '%s'" % (messageProtocolEntity.getBody()))

    def onMediaMessage(self, messageProtocolEntity):
        # just print info
        if messageProtocolEntity.getMediaType() == "image":
            print("Echoing image %s to %s" % (messageProtocolEntity.url, messageProtocolEntity.getFrom(False)))
        elif messageProtocolEntity.getMediaType() == "location":
            print("Echoing location (%s, %s) to %s" % (messageProtocolEntity.getLatitude(),
                                                       messageProtocolEntity.getLongitude(),
                                                       messageProtocolEntity.getFrom(False)))
        elif messageProtocolEntity.getMediaType() == "vcard":
            print("Echoing vcard (%s, %s) to %s" % (messageProtocolEntity.getName(),
                                                    messageProtocolEntity.getCardData(),
                                                    messageProtocolEntity.getFrom(False)))
