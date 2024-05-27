# fish.py

from datetime import datetime

class Fish:
    def __init__(self, species, number, date_added=None):
        self.species = species
        self.number = number
        self.date_added = date_added if date_added else datetime.now().strftime("%Y-%m-%d")

    def get_info(self):
        return f"Species: {self.species}, Number: {self.number}, Date Added: {self.date_added}"

    def update_number(self, number):
        self.number = number
