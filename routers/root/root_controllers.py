import actions


class RootController:
    def __new__(self, payload):
        self.group, self.action = payload.action.split(".")
        if self.action.startswith("_"):
            return None
        self.data = payload.data
        module_group: str = getattr(actions, self.group)
        module_class = getattr(module_group, f"{self.group.capitalize()}Actions")
        method = getattr(module_class(self.data), self.action)
        return method()
