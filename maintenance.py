# maintenance.py

class MaintenanceAction:
    def __init__(self, action, date, time, quantity=None):
        self.action = action
        self.date = date
        self.time = time
        self.quantity = quantity

    def get_info(self):
        if self.action == "added fertilizer":
            return f"Action: {self.action}, Date: {self.date}, Time: {self.time}, Quantity: {self.quantity}ml"
        return f"Action: {self.action}, Date: {self.date}, Time: {self.time}"
