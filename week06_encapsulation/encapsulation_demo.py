class Person_jcs:
    def __init__(self_jcs, name_jcs, age_jcs):
        self_jcs.__name = name_jcs
        self_jcs.__age = age_jcs

    def get_name_jcs(self_jcs):
        return self_jcs.__name

    def get_age_jcs(self_jcs):
        return self_jcs.__age

p1_jcs = Person_jcs("Maria", 20)
print("Name:", p1_jcs.get_name_jcs())
print("Age:", p1_jcs.get_age_jcs())