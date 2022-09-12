from faker import Faker

from schemas.customer_schema import CustomerSchema
from schemas.user_schema import UserSchema

fake = Faker()

users_data = [
    UserSchema(
        username=f"user{n}",
        password="123",
        name=fake.name(),
        phone=fake.phone_number(),
        premium_account = n % 2==0
    )
    for n in range(5)
]

customers_data = [
    CustomerSchema(
        name=fake.name(),
        address=fake.address(),
        phone=fake.phone_number(),
        job=fake.job(),
    )
    for c in range(5)
]
