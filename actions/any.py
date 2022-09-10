from actions.base import BaseActions

class AnyActions(BaseActions):
    def __init__(self, request, data):
        super().__init__(request,data)

    def who(self):
        return {"username": self.request.state.token.get("username")}

    def something(self):
        return {"detail": "Something message"}

    def anything(self):
        return {"detail": "Anything message"}

    def _private(self):
        return {"detail": "PRIVATE METHOD"}
