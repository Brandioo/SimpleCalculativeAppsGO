import time


class Auto:

    def __init__(self, color, model, make):
        self.color = color
        self.model = model
        self.plate = None
        self.make = make
        self.is_switched_on = False
        self.max_speed = 0
        self.current_gear = 1
        self.current_speed = 0
        self.price = 0
        self.gear_type = "Manual"
        self.is_locked = True

    # str - Convert To Text

    def __bool__(self):
        if self.color is not None:
            print("True")
        else:
            print("False")

    def __eq__(self, other):
        if self.color == other.color and self.model == other.model:
            return True
        else:
            return False

    def __repr__(self):
        print(f"""
        this is an auto Class
        make={self.make}
        model={self.model}
        color={self.color}""")

    def unlock(self):
        if self.is_locked == True:
            self.is_locked = False

    def lock(self):
        if self.is_locked == False:
            self.is_locked = True

    def ignite(self):
        if self.is_switched_on == False:
            self.is_switched_on = True

    def select_gear(self, gear=1):
        self.current_gear = gear

    def press_gas_pedal(self):
        self.current_speed += 10

    def press_brakes_pedals(self):
        self.current_speed -= 10

car1 = Auto(make="Ferrari",model="Enzo",color="Red")
car2 = Auto(make="Ferrari",model="Enzo",color="Red")

car1.max_speed = 300

# print(car1.model)
# print(car1.make)

car1.unlock()
car1.ignite()
car1.press_gas_pedal()
car1.select_gear(2)
car1.press_gas_pedal()

# for x in range(2):
#     car1.press_gas_pedal()
#     print(car1.current_speed)
#     time.sleep(1)
# print("Game-Over")

print(car1==car2)

# car1.__repr__()
