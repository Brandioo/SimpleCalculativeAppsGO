class LiquidContainer:
    make = None
    content_type = ""
    color = None
    is_open = False
    volume_ml = 0
    current_volume_ml = 0

    def spray(self):
        if self.is_open == True:
            if self.current_volume_ml - 10 >= 0:
                self.current_volume_ml -= 10
            else:
                print("Can't Spray, no more content!")
        else:
            print("Can't Spray On Closed Container!")

    def open(self):
        if self.is_open == False:
            self.is_open = True

    def refill(self, ml):
        self.current_volume_ml = ml

d = LiquidContainer()
d.color = "white"
d.content_type = "Hand Sanitizier"
d.volume_ml = 500
d.current_volume_ml = 500

d.open()
d.spray()

print(d.current_volume_ml)