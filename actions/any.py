class AnyActions:
    def __init__(self, data):
        self.data = data

    def something(self):
        return {"detail": "Something message"}

    def anything(self):
        return {"detail": "Anything message"}

    def _private(self):
        return {"detail": "PRIVATE METHOD"}
