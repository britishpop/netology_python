import requests
from pprint import pprint


class Animal:
    def __init__(self):
        self.obey_humans = True
        self.live_on_farm = True
        self.legs = None
        self.mouth = None
        self.production = None


class Even_toed(Animal):
    def __init__(self):
        self.fur = True
        self.mouth = "lips"
        self.legs = 4


class Bird(Animal):
    def __init__(self):
        self.feathers = True
        self.mouth = "beak"
        self.legs = 2
        self.wings = 2


class Cow(Even_toed):
    def __init__(self):
        self.production = ["milk", "meat"]


class Goat(Even_toed):
    def __init__(self):
        self.production = ["milk", "meat"]


class Sheep(Even_toed):
    def __init__(self):
        self.production = ["fur", "meat"]


class Pig(Even_toed):
    def __init__(self):
        self.production = ["meat"]


class Duck(Bird):
    def __init__(self):
        self.production = ["meat"]


class Chick(Bird):
    def __init__(self):
        self.production = ["eggs", "meat"]


class Goose(Bird):
    def __init__(self):
        self.production = ["meat"]


jeffrey = Goose()

big_cow = Cow()

small_cow = Cow()

big_cow.production.append("calves")

print("Big cow: ", big_cow.production)
print("Small cow: ", small_cow.production)
