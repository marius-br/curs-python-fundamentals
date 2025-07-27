class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def info(self):
       vechime = 2025 - int(self.year)
       print(f"Brandul este {self.brand}, Modelul este {self.model} Anul este: {self.year}, Vechime este de {vechime} ani!")

    def get_brand(self):
        return self.brand

    def set_brand(self, new_brand):
        self.brand = new_brand

    def get_model(self):
        return self.model

    def set_model(self, new_model):
        self.model = new_model

    def get_year(self):
        return self.year

    def set_year(self, new_year):
        self.year = new_year

class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors=4):
        super().__init__(brand, model, year)
        self.num_doors = num_doors

    def get_num_doors(self):
        return self.num_doors

    def set_num_doors(self, new_num_doors):
        self.num_doors = new_num_doors

    def start_engine(self):
        print("Masina este pornita!")


car1 = Car("Toyota", "Corolla", '2013', 4)
car1.info()
print(car1.get_brand())
print(car1.get_num_doors())