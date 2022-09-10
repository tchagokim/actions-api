import actions


class RootController:
    def __new__(self, request, payload):
        group, action = payload.action.split(".")
        if action.startswith("_"):
            return None
        data = payload.data
        module_group: str = getattr(actions, group)
        module_class = getattr(module_group, f"{group.capitalize()}Actions")
        method = getattr(module_class(request, data), action)
        return method()
