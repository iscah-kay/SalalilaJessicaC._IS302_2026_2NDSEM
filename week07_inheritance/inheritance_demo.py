class Animal_jcs:
    def __init__(self_jcs, name_jcs):
        self_jcs.name_jcs = name_jcs

    def speak(self_jcs):
        print(self_jcs.name_jcs, "makes a sound")

class Dog_jcs(Animal_jcs):
    def bark(self_jcs):
        print(self_jcs.name_jcs, "barks")

dog1_jcs = Dog_jcs("Buddy")
dog1_jcs.speak()
dog1_jcs.bark()