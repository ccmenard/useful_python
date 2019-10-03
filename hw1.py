#!/bin/bash
#hw 1 completed spring 2019 
#Claire Menard

class Animal:
	def __init__(self,name,code):
		self.name = name
		self.code = code
class Oviparous(Animal):
        def LayEggs(self):
                print(self.name)

class Mammal(Animal):
        def Nurse(self):
                print(self.name)


Crocodile = Oviparous("Crocodile", 1)
Goose = Oviparous("Goose", 2)
Pelican = Oviparous("Pelican", 3)

Bat = Mammal("Bat", 4)
Whale = Mammal("Whale", 5)
SeaLion = Mammal("SeaLion", 6)

Crocodile.LayEggs()


