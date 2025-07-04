from bird import Bird, Flyable, Moltable

class Eagle(Bird, Flyable, Moltable):

    def fly(self):
        self.set_current_location("in the air")

    def molt(self):
        self.set_number_of_feathers(self.number_of_feathers - 1)
