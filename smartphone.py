# smartphone.py

# Base class
class Device:
    def __init__(self, brand):
        self.brand = brand

    def power_on(self):
        print(f"{self.brand} device is now ON 🔋")


# Derived class (inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage):
        super().__init__(brand)  # call parent constructor
        self.model = model
        self.storage = storage
        self.__battery = 100  # encapsulated (private attribute)

    def install_app(self, app_name):
        print(f"{app_name} installed on {self.model} 📱")

    def use_battery(self, amount):
        if self.__battery - amount >= 0:
            self.__battery -= amount
            print(f"Battery now at {self.__battery}%")
        else:
            print("Battery too low! Please recharge 🔌")

    def get_battery(self):
        return self.__battery


# Example usage
phone1 = Smartphone("Samsung", "Galaxy S22", "128GB")
phone1.power_on()
phone1.install_app("Instagram")
phone1.use_battery(30)
print("Battery left:", phone1.get_battery(), "%")
