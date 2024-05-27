# aquarium.py

import pickle
from fish import Fish
from maintenance import MaintenanceAction

class Aquarium:
    def __init__(self):
        self.fish_list = []
        self.maintenance_log = []

    def add_fish(self, new_fish):
        self.fish_list.append(new_fish)

    def get_fish_list(self):
        return [fish.get_info() for fish in self.fish_list]

    def add_maintenance_action(self, action):
        self.maintenance_log.append(action)

    def get_maintenance_log(self):
        return [action.get_info() for action in self.maintenance_log]

    def save_data(self, filename="aquarium_data.pkl"):
        with open(filename, 'wb') as file:
            pickle.dump((self.fish_list, self.maintenance_log), file)

    def load_data(self, filename="aquarium_data.pkl"):
        try:
            with open(filename, 'rb') as file:
                self.fish_list, self.maintenance_log = pickle.load(file)
        except FileNotFoundError:
            self.fish_list = []
            self.maintenance_log = []
