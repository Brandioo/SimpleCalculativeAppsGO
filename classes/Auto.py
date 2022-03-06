import time


class Auto:

    color = None
    model = None
    plate = None
    make = None
    is_switched_on = False
    max_speed = 0
    current_gear = 1
    current_speed = 0
    price = 0
    gear_type = "Manual"
    is_locked = True

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

car1 = Auto()

car1.make = "Ferrari"
car1.model = "Purosngue"
car1.color = "Red"
car1.max_speed = 300

print(car1.model)
print(car1.make)

car1.unlock()
car1.ignite()
car1.press_gas_pedal()
car1.select_gear(2)
car1.press_gas_pedal()

for x in range(2):
    car1.press_gas_pedal()
    print(car1.current_speed)
    time.sleep(1)
