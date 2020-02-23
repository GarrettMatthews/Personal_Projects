"""
This generates random quests for D&D - these can be used simply for building ideas, or as jobs attached to NPCs

Garrett Matthews

"""

import random as rdm
from items import Item
from setting import Setting
from villain import Villain
from prophecy import Prophecy


class Quest:

    def __init__(self, level):
        self.quest = ''
        self.item = ''
        self.location = ''
        self.enemy = ''
        self.reward = ''
        self.level = level
        self.prophecy = ''
        self.relation = ''

    def quest_type(self):
        """Randomly chooses a quest type"""
        quests = ["Fetch", "Rescue", "Steal", "Kill", "Avenge", "Escort", "Find", "Investigate", "Warning", "Prophecy",
                  "Deliver"]
        self.quest = rdm.choice(quests)

    def item_quest(self):
        """Receives a randomly generated item for an item quest"""
        item = Item()
        self.item = item.main()

    def quest_location(self):
        """Receives a randomly generated location for a quest"""
        setting = Setting()
        self.location = setting.main()

    def quest_reward(self):
        """Returns a randomly generated quest reward based on party level"""
        if self.level < 5:
            coin = "gp"
            amount = rdm.randrange(100, 1000, 5)
            self.reward = str(amount) + coin
        elif self.level < 10:
            coin = "gp"
            amount = rdm.randrange(500, 3000, 5)
            self.reward = str(amount) + coin
        else:
            coin = rdm.choice(["gp","pp"])
            amount = rdm.randrange(1000, 10000, 5)
            self.reward = str(amount) + coin

    def quest_enemy(self):
        """Returns an enemy for revenge/killing based quests"""
        villain = Villain()
        self.enemy = villain.main()

    def quest_prophecy(self):
        """Returns a prophecy for prophecy/warning based quests"""
        prophecy = Prophecy()
        self.prophecy = prophecy.main()

    def relationship(self):
        """Returns a relationship for a rescue/escort type mission"""
        lyst = ["father", "mother", "parent", "grandparent", "brother", "sister", "sibling", "friend", "uncle",
                "aunt", "niece", "nephew", "cousin", "friend", "neighbor", "family", "son", "daughter", "child"]
        self.relation = rdm.choice(lyst)

    def main(self):
        """Runs the quest program, choosing a quest and populating the needs"""
        self.quest_type()
        self.quest_reward()
        if self.quest in ["Fetch", "Steal", "Deliver", "Find"]:
            self.item_quest()
            self.quest_location()
            prompt = "You must " + self.quest.lower() + ". Accomplish this, and your reward will be "
            prompt += self.reward + '.'
            if self.quest == "Deliver":
                prompt += " they need you to deliver it to " + self.location + '.'
            elif self.quest == "Steal":
                prompt += " It can be found in/at/near the " + self.location + '.'
        elif self.quest in ["Rescue", "Avenge", "Escort"]:
            self.relationship()
            self.quest_location()
            if self.quest == "Escort":
                prompt = "they need you to escort their " + self.relation + " to/past/through the " + self.location
                prompt += ", you're reward will be " + self.reward
        if self.quest in ["Rescue", "Avenge", "Kill"]:
            self.quest_enemy()
            self.quest_location()
            if self.quest == "Rescue":
                prompt = "they need you to rescue their " + self.relation + " from " + self.enemy
                prompt += ". They can be found near/at/in " + self.location + '.'
                prompt += ", you're reward will be " + self.reward
            elif self.quest == "Avenge":
                prompt = "they need you to avenge their " + self.relation + ", they were killed by " + self.enemy
                prompt += ". They can be found near/in/at " + self.location + '.'
                prompt += ", you're reward will be " + self.reward
            elif self.quest == "Kill":
                prompt = "they need you to kill " + self.enemy + ". They can be found near/in/at " + self.location
                prompt += ", you're reward will be " + self.reward
        elif self.quest in ["Warning", "Prophecy"]:
            self.quest_prophecy()
            if self.quest == "Warning":
                prompt = "I have a warning for you, " + self.prophecy + '.'
            elif self.quest == "Prophecy":
                prompt = self.prophecy + '.'
        elif self.quest == "Investigate":
            investigate = rdm.choice(["mystery", "rumor", "monster"])
            self.quest_location()
            prompt = "they need you to investigate the " + investigate + " of " + self.location + '.'
            prompt += ", you're reward will be " + self.reward
        return self.quest, prompt

    def __str__(self):
        return self.main()


def main():
    """Tests/runs the quest program"""
    print(Quest(1))


if __name__ == '__main__':
    main()
