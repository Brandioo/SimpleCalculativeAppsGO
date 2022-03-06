from dataclasses import dataclass


@dataclass
class Bottle:
    make: str
    material: str
    content_type: str
    current_volume: int
    max_volume: int
    is_open: bool = False

    def open(self):
        if self.is_open == False:
            self.is_open = True


class drinkableBottle(Bottle):

    def drink(self):
        self.current_volume -= 50


qafshtama = drinkableBottle("Qafshtama", "Plastic", "water", 250, 500)

qafshtama.open()
qafshtama.drink()

print(qafshtama.current_volume)
print(qafshtama.content_type)
