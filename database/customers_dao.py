from database.dao import DAO
from database.data import customers_data
from schemas.customer_schema import CustomerSchema


class CustomersDAO(DAO):
    def __init__(self):
        super().__init__(customers_data)

    def new_customer(self, customer_dict: dict):
        return self.create(CustomerSchema(**customer_dict))

    def get_customer(self, id_):
        return self.read_id(id_)

    def get_customers(self):
        return [customer.dict() for customer in self.datalist]
