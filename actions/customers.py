from actions.base import BaseActions
from database.customers_dao import CustomersDAO
from decorators.auth.only_for import only_for

class CustomersActions(BaseActions):
    def __init__(self, request, data):
        super().__init__(request,data)
        self.dao = CustomersDAO()

    def new_customer(self):
        return {"detail": self.dao.new_customer(self.data)}

    def get(self):
        return self.dao.get_customers()

    @only_for("premium_account",True)
    def get_id(self):
        return self.dao.get_customer(self.data.get("id"))
