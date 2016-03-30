import aiml
class Responder():
        query = ""

        def __init__(self, query):
                self.query = query
                self.kernel = aiml.Kernel()
                self.kernel.learn("torz/startup.xml")
                self.kernel.respond("LOAD AIML TORZ")

        def respond(self):
                return self.kernel.respond(self.query)

