from item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Call to super function to have access to all attributes / methods
        # Run validations to the received arguments
        super().__init__(
            name, price, quantity
        )

        assert broken_phones >= 0, f"Broken phones {broken_phones} cannot be less than or equal to zero!"

        # Assign to self object
        self.broken_phones = broken_phones
