from bird import Bird, Moltable, Swimmable

class Penguin(Bird, Moltable, Swimmable):
    def molt(self):
        self.set_number_of_feathers(self.number_of_feathers - 1)

    def swim(self):
        self.set_current_location("in the water")
