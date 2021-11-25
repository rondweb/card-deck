class Card:
    def __init__(self, ref, suit, value):
        self.ref = ref
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.ref} {self.suit} {self.value}"

    def get_ref(self):
        return self.ref

    def get_value(self):
        return self.value

    def get_suit(self):
        return self.suit
