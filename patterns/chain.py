class Handler:
    """Abstract Handler"""

    def __init__(self, successor):
        # Define who is the next handler
        self._successor = successor

    def handle(self, request):
        handled = self._handle(request)
        # Otherwise, keep going
        if not handled:
            self._successor.handle(request)

    def _handle(self, request):
        raise NotImplementedError("Must provide implementation")


class ConcreteHandler1(Handler):
    """Concrete handler 1"""

    def _handle(self, request):
        if 0 < request <= 10:
            print("Request {} handled by handler 1".format(request))
            return True


class ConcreteHandler2(Handler):
    """Concrete handler 2"""

    def _handle(self, request):
        if 10 < request <= 20:
            print("Request {} handled by handler 2".format(request))
            return True


class DefaultHandler(Handler):

    def _handle(self, request):
        print("End of chain, no handler for {}".format(request))
        return True


class Client:
    # Using Handlers
    def __init__(self):
        self.handler = ConcreteHandler1(ConcreteHandler2(DefaultHandler(None)))

    def delegate(self, inputs):
        for request in inputs:
            self.handler.handle(request)


if __name__ == "__main__":
    c = Client()
    requests = [2, 5, 20, 30]
    c.delegate(requests)
