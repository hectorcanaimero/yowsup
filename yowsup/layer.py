from yowsup.layers.interface                            import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.auth                                 import YowAuthenticationProtocolLayer
from yowsup.layers.protocol_messages.protocolentities   import TextMessageProtocolEntity
from yowsup.layers.protocol_receipts.protocolentities   import OutgoingReceiptProtocolEntity
from yowsup.layers.protocol_acks.protocolentities       import OutgoingAckProtocolEntity
from yowsup.layers.protocol_messages                    import YowMessagesProtocolLayer
from yowsup.layers.protocol_receipts                    import YowReceiptProtocolLayer
from yowsup.layers.protocol_acks                        import YowAckProtocolLayer
from yowsup.layers.network                              import YowNetworkLayer
from yowsup.layers.coder                                import YowCoderLayer
from yowsup.stacks                                      import YowStack
from yowsup.common                                      import YowConstants
from yowsup.layers                                      import YowLayerEvent
from yowsup.stacks                                      import YowStack, YOWSUP_CORE_LAYERS

CREDENTIALS = ("5541987752137", "2El/lk0c/qO34okBKJoSjBOIZGUlr1saNbshTtU2XERgEFXOgZIr2g+gKcYpI2hJhZpPKlh6IcHTrxS8gU58Jw==")

class TestLayer(YowInterfaceLayer):

    def message_send(self, number, content):
        outgoingMessage = TextMessageProtocolEntity(content, to=self.normalizeJid(number))
        self.toLower(outgoingMessage)

    def normalizeJid(self, number):
        if '@' in number:
            return number
        return "%s@s.whatsapp.net" % number

if __name__==  "main":

    layers = (
        TestLayer,
        (YowAuthenticationProtocolLayer, YowMessagesProtocolLayer, YowReceiptProtocolLayer, YowAckProtocolLayer)
    ) + YOWSUP_CORE_LAYERS

    stack = YowStack(layers)
    stack.setProp(YowAuthenticationProtocolLayer.PROP_CREDENTIALS, CREDENTIALS)         #setting credentials
    stack.setProp(YowNetworkLayer.PROP_ENDPOINT, YowConstants.ENDPOINTS[0])    #whatsapp server address
    stack.setProp(YowCoderLayer.PROP_DOMAIN, YowConstants.DOMAIN)
    stack.setProp(YowCoderLayer.PROP_RESOURCE, YowConstants.RESOURCE)          #info about us as WhatsApp client

    stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))   #sending the connect signal

    #stack.loop()

    layer = stack.getLayer(5)
    layer.message_send("554198819501", "TestMessage")
