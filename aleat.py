import webapp;

class aleat (webapp.webApp):
    def process(self, parsedRequest):
        """Process the relevant elements of the request.

        Returns the HTTP code for the reply, and an HTML page.
        """
        import random;
        return ("200 OK", "<html><body><p>Hola, <a href='" + str(random.randint(1,1000000)) + "'>Dame otra</a></p></body></html>")

if __name__ == "__main__":
    aleat = aleat('localhost', 1234)
