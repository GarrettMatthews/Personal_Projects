"""
Generates a random location/setting

Garrett Matthews

"""

import random as rdm


class Setting:

    def __init__(self):
        self.setting = ''
        self.description = ''
        self.direction = ''
        self.travel = ''

    def dscptn(self):
        """Returns a random descriptor for a setting"""
        lyst = ["dark", "haunted", "blessed", "cursed", "heavenly", "ancient", "abandoned", "overgrown", "derelict",
                "empty", "overrun", "populated", "sparse", "dense", "angry", "barren", "windswept", "broken", "dusty"]
        chance = rdm.random()
        if chance > 0.25:
            self.description = rdm.choice(lyst)

    def location(self):
        """Returns a randomly generated location"""
        lyst = ["forest", "plains", "cliff", "seaside", "hills", "castle", "town", "village", "desert", "mountains",
                "caves", "tundra", "swamp", "bog", "fens", "graveyard", "mansion", "camp", "hideout", "ocean", "river",
                "quarry", "mines", "ravine", "jungle", "oasis", "garden"]
        self.setting = rdm.choice(lyst)

    def drtn(self):
        """Returns a random direction"""
        attach = ["north-", "south-"]
        dctn = rdm.choice(["north", "west", "south", "east"])
        chance = rdm.random()
        if chance > 0.80:
            attach = rdm.choice(attach)
            dctn = rdm.choice(['west', 'east'])
            self.direction = attach + dctn
        else:
            self.direction = dctn

    def distance(self):
        dist = rdm.randint(1,20)
        unit = rdm.choice(["miles", "days", "weeks", "months", "hours"])
        if unit == "miles":
            dist *= rdm.randint(1,20)
        self.travel = str(dist) + ' ' + unit

    def main(self):
        """Runs Setting program"""
        self.dscptn()
        self.location()
        self.drtn()
        self.distance()
        location = self.description + ' ' + self.setting + " located " + self.travel + " to the " + \
                   self.direction
        return location

    def __str__(self):
        local = self.main()
        prompt = "Location prompt: A "
        prompt += local
        return prompt


def main():
    print(Setting())


if __name__ == "__main__":
    main()
