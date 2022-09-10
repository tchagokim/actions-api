from database.customers_dao import CustomersDAO


class CustomersActions:
    def __init__(self, data):
        self.data = data
        self.dao = CustomersDAO()

    def new_customer(self):
        return {"detail": self.dao.new_customer(self.data)}

    def get(self):
        return self.dao.get_customers()

    def get_id(self):
        return self.dao.get_customer(self.data.get("id"))
