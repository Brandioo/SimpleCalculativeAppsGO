
class Bottle:
    def __init__(self, make , material, content_type, current_volume, max_volume):
        self.make = make
        self.material = material
        self.content_type = content_type
        self.current_volume = current_volume
        self.max_volume = max_volume
        self.is_open = False

    def open(self):
        if self.is_open == False:
            self.is_open = True

class drinkableBottle(Bottle):

    def __init__(self, make , material, content_type, current_volume, max_volume):
        super().__init__(make , material, content_type, current_volume, max_volume)

    def drink(self):
        self.current_volume -= 50

qafshtama = drinkableBottle("Qafshtama", "Plastic","water", 250, 500)

qafshtama.open()
qafshtama.drink()

print(qafshtama.current_volume)