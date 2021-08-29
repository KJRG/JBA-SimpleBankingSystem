class Lightbulb:
    def __init__(self):
        self.state = "off"

    # create method change_state here
    def change_state(self):
        next_state = "on" if self.state == "off" else "off"
        self.state = next_state
        print("Turning the light {}".format(next_state))
