class Person_jcs:
    def __init__(self_jcs, name_jcs, age_jcs):
        self_jcs.name_jcs = name_jcs
        self_jcs.age_jcs = age_jcs
    
    def display_info_jcs(self_jcs):
        print("Name:", self_jcs.name_jcs)
        print("Age:", self_jcs.age_jcs)

p1_jcs = Person_jcs("Juan", 20)
p1_jcs.display_info_jcs()
