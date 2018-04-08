class Animal:
	obey_humans = True
	live_on_farm = True
	legs = None
	mouth = None
	production = None

class Even_toed(Animal):
	fur = True
	mouth = "lips"
	legs = 4

class Bird(Animal):
	feathers = True
	mouth = "beak"
	legs = 2
	wings = 2

class Cow(Even_toed):
	production = ["milk", "meat"]

class Goat(Even_toed):
	production = ["milk", "meat"]

class Sheep(Even_toed):
	production = ["fur", "meat"]

class Pig(Even_toed):
	production = ["meat"]

class Duck(Bird):
	production = ["meat"]

class Chick(Bird):
	production = ["eggs", "meat"]

class Goose(Bird):
	production = ["meat"]

jeffrey = Goose()
print(jeffrey.feathers)