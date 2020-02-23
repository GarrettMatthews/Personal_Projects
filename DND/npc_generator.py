""""
This NPC generator will generate a name, a race, a sex, a personality, a job, an option to keep the NPC,
and will save each kept NPC to a text file named after the session number (possible personalized option in future)



Garrett Matthews
"""
import random as rdm
from quest import Quest


class NPC:

    def __init__(self, sex=None, race=None):
        self.sex = sex
        self.race = race
        self.race_lyst = ["Elf", "Half Elf", "Human", "Halfling", "Dwarf", "Gnome"]
        self.uncommon_races = ["Half-orc", "Water Genasi", "Earth Genasi", "Fire Genasi", "Air Genasi", "Tiefling",
                               "Dragonborn"]
        self.monstrous_races = ["Orc", "Goblin", "Hoggoblin", "Kobold", "Bug bear", "Yuan-ti", "Centaur", "Minotaur",
                                "Satyr", "Fairy", "Pixie"]
        self.job = ''
        self.hair = ''
        self.features = ''
        self.name = ''
        self.npc_lyst = []
        self.quest_type = ''

    def random_sex(self):
        """Returns a random sex for the NPC"""
        if self.sex is not None:
            pass
        else:
            lyst = ["male", "female", "non-binary", "trans"]
            self.sex = rdm.choice(lyst)

    def random_race(self):
        """Returns a random race for the NPC"""
        if self.race is not None:
            pass
        else:
            lyst = self.race_lyst + self.uncommon_races + self.monstrous_races
            self.race = rdm.choice(lyst)

    def common_race(self):
        """Returns a randomly chosen common race"""
        if self.race is not None:
            pass
        else:
            self.race = rdm.choice(self.race_lyst)

    def uncommon_race(self):
        """Returns a randomly chosen uncommon race"""
        if self.race is not None:
            pass
        else:
            self.race = rdm.choice(self.uncommon_races)

    def monstrous_race(self):
        """Returns a randomly chosen monstrous race"""
        if self.race is not None:
            pass
        else:
            self.race = rdm.choice(self.monstrous_races)

    def npc_need(self, level):
        """Returns a need/job from the NPC"""
        quest = Quest(level)
        self.quest_type, self.job = quest.main()

    def npc_hair(self):
        """Returns a hair type and description for the npc"""
        hair_cut = ["long", "short", "bald", "buzz cut", "medium", "mohawk", "undercut", "mullet", "dreadlocks",
                    "braids", "balding", "thinning"]
        hair_color = ["brown", "black", "white", "silver", "gray", "blond", "orange", "red", "green", "blue", "brown",
                      "purple", "pink"]
        hair_type = ["thin", "wispy", "thick", "curly", "straight", "frizzled", "poofy", "greasy"]
        facial_hair = ["mustache", "goatee", "mutton chops", "full beard", "soul patch", "sideburns", "van dyke",
                       "braided", "stubble beard", "scruffy beard", "patchy beard"]
        cut = rdm.choice(hair_cut)
        color = rdm.choice(hair_color)
        kind = rdm.choice(hair_type)
        beard = rdm.choice(facial_hair)
        if self.sex == "female":
            chance = rdm.random()
            self.hair = cut + " "
            if cut != "bald":
                self.hair += kind + " " + color + " haired "
            if chance <= 0.25:
                self.hair += " with a " + beard
        else:
            chance = rdm.random()
            self.hair = cut + " "
            if cut != "bald":
                self.hair += kind + " " + color + " haired "
            if chance <= 0.50:
                self.hair += " with a " + beard

    def npc_features(self):
        """Returns a unique feature of the npc"""
        lyst = ["crooked nose", "missing tooth", "cleft chin", "eye patch", "long scar on a cheek", "several piercings",
                "broken arm", "club foot", "crutch", "humpback", "limp"]
        chance = rdm.random()
        if chance >= 0.65:
            self.features = rdm.choice(lyst)

    def npc_name(self):
        """Returns a NPC name"""
        self.name = "Feature not available yet"

    def main(self):
        """Runs the main NPC generator program"""
        session = input("Please enter a session number: ")
        level = int(input("Please enter the average level of the party: "))
        cont = "yes"
        while cont in ["Yes", "yes", "y", "Y"]:
            self.random_sex()
            self.random_race()
            self.npc_features()
            self.npc_need(level)
            self.npc_hair()
            self.npc_name()
            prompt = "A " + self.sex + ' ' + self.race + ' with ' + self.hair + " named " + self.name + ". \n"
            if self.features != '':
                prompt += "They have a " + self.features + '. \n'
            prompt += "They need help with a " + self.quest_type + " quest. Specifically they need " + self.job + '.\n'
            print(prompt)
            keep = input("Would you like to keep this NPC? ")
            if keep in ["Yes", "yes", "y", "Y"]:
                self.npc_lyst.append(prompt)
            cont = input("Would you like to make another NPC?")
        file = "session_" + session + "_npcs" + ".txt"
        with open(file, 'w') as fn:
            for line in self.npc_lyst:
                fn.write(line)
                fn.write('\n')
                fn.write('\n')


def main():
    """Run and tests the NPC program"""
    npc = NPC()
    npc.main()


if __name__ == '__main__':
    main()