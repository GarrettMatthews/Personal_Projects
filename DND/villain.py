"""

A random villain generator

Garrett Matthews

"""

import random as rdm

class Villain:

    def __init__(self):
        self.description = ''
        self.kind = ''
        self.minion = ''
        self.crime = ''

    def describe(self):
        """Returns a description/adjective to describe the villain"""
        lyst = ["shadowy", "cloaked", "angry", "barbaric", "blood thirsty", "crippled", "old", "mysterious",
                "backstabbing", "murderous", "trickster", "careful", "violent", "psychotic", "tired", "wizened",
                "young", "strong", "smart", "crafty", "careful"]
        self.description = rdm.choice(lyst)

    def villain_type(self):
        """Returns a type/class for a villain"""
        lyst = ["crime boss", "knight", "priest", "cult leader", "noble", "tax collector", "highway man", "lich",
                "brigand leader", "thief", "cutthroat", "general", "wizard", "monster", "traitor", "gangster",
                "assassin", "ambassador", "spy", "dark paladin", "vampire", "figure"]
        self.kind = rdm.choice(lyst)

    def minions(self):
        """Gives a 50% chance of a villain having minions, and randomly chooses some"""
        chance = rdm.random()
        lyst_1 = ["goblins", "kobolds", "cultists", "brigands", "thieves", "men at arms", "wolves", "dogs", "bats",
                  "rats", "zombies", "skeletons"]
        lyst_2 = ["knights", "guards", "soldiers", "ghosts", "wraiths", "pirates", "hobgoblins"]
        lyst_3 = ["mages", "clerics", "paladins", "mercenaries", "bears", "bug bears"]
        lyst = lyst_1 + lyst_2 + lyst_3
        if chance >= 0.50:
            choice = rdm.choice(lyst)
            if choice in lyst_1:
                amount = rdm.randint(4, 15)
            elif choice in lyst_2:
                amount = rdm.randint(2, 10)
            else:
                amount = rdm.randint(1, 5)
            self.minion = str(amount) + " " + choice

    def crime_type(self):
        """Returns a potential crime they committed"""
        lyst = ["murder", "robbery", "necromancy", "being a conman", "blasphemy", "summoning a demon",
                "bargain with  a devil", "betrayal", "poisoning", "planning coup", "assassination",
                "organized crime", "serial killing", "running a pyramid scheme"]
        self.crime = rdm.choice(lyst)

    def main(self):
        """Assembles a villain prompt"""
        self.describe()
        self.villain_type()
        self.minions()
        self.crime_type()
        adj = rdm.choice([1, 2, 3])
        if adj == 2:
            dsc_1 = self.description
            self.describe()
            while dsc_1 == self.description:
                self.describe()
            prompt = "a " + dsc_1 + ", " + self.description + ' ' + self.kind + " who's crime is "
            prompt += self.crime + '.'
            if self.minion != '':
                prompt += " They have " + self.minion + " as minions"
        if adj == 3:
            dsc_1 = self.description
            self.describe()
            while dsc_1 == self.description:
                self.describe()
            dsc_2 = self.description
            self.describe()
            while dsc_1 == self.description or dsc_2 == self.description:
                self.describe()
            prompt = "a " + dsc_1 + ", " + dsc_2 + ", " + self.description + ' ' + self.kind
            prompt += " who's crime is " + self.crime + '.'
            if self.minion != '':
                prompt += " They have " + self.minion + " as minions"
        else:
            prompt = "a " + self.description + ' ' + self.kind + " who's crime is "
            prompt += self.crime + '.'
            if self.minion != '':
                prompt += " They have " + self.minion + " as minions"
        return prompt

    def __str__(self):
        vill = self.main()
        prompt = "Villain prompt: "
        prompt += vill
        return prompt


def main():
    """Runs/Tests the villain program"""
    print(Villain())


if __name__ == "__main__":
    main()
