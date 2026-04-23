class Car_jcs:
    def __init__(self_jcs, brand_jcs, model_jcs, year_jcs):
        self_jcs.brand_jcs = brand_jcs
        self_jcs.model_jcs = model_jcs
        self_jcs.year_jcs = year_jcs
    
    def display_car_jcs(self_jcs):
        print(self_jcs.brand_jcs, self_jcs.model_jcs, self_jcs.year_jcs)

car1_jcs = Car_jcs("Toyota", "Corolla", 2020)
car1_jcs.display_car_jcs()
