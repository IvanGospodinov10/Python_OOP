from project.id_mixin import IdMixin


class Customer(IdMixin):

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.id = self.get_next_id()
        self.increment_id()

        # self.id = Customer.id
        # Customer.id += 1

    # @classmethod
    # def get_next_id(cls) -> int:
    #     return cls.id

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"
