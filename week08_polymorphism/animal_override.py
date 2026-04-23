class Animal_jcs:
    def speak_jcs(self_jcs):
        print("Animal makes a sound")

class Dog_jcs(Animal_jcs):
    def speak_jcs(self_jcs):
        print("Dog barks")

class Cat_jcs(Animal_jcs):
    def speak_jcs(self_jcs):
        print("Cat meows")

animals_jcs = [Dog_jcs(), Cat_jcs()]
for animal_jcs in animals_jcs:
    animal_jcs.speak_jcs()