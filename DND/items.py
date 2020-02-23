"""

Returns a randomly generated item that can be magical and/or cursed

Garrett Matthews

"""

import random as rdm


class Item:

    def __init__(self, magical = None, cursed = None):
        self.adjective = ''
        self.item_type = ''
        self.value = ''
        self.magical = magical
        self.cursed = cursed
        self.jewel = ''
        self.material = ''
        self.mgc = ''
        self.crs = ''

    def description(self):
        """Returns an adjective for an item"""
        colors = ["red", "green", "blue", "orange", "purple", "white", "black", "teal", "yellow", "gray"]
        shades = ["light", '', "dark", "metallic", "matte", "mottled"]
        jewels = ['diamond', 'ruby', 'sapphire', 'emerald', 'amethyst', 'opal', 'amber', 'topaz', 'lapis lazuli',
                  'garnet', 'turquoise', 'pearl', 'quartz', 'jade']
        materials = ['iron', 'steel', 'wood', 'gold', 'silver', 'brass', 'copper', 'platinum', 'glass']
        affixed = ['encrusted', 'inlaid']
        color = rdm.choice(colors)
        if color in ['white', 'black']:
            shades = ['', "metallic", "matte", "mottled"]
            shade = rdm.choice(shades)
        else:
            shade = rdm.choice(shades)
        gem = rdm.random()
        if gem >= 0.75:
            self.jewel = rdm.choice(jewels)
            self.jewel += ' ' + rdm.choice(affixed)
        self.material += rdm.choice(materials)
        self.adjective = shade + ' ' + color + ' ' + self.jewel

    def item(self):
        """Returns a randomly chosen item type"""
        types = ['staff', 'cup', 'chalice', 'plate', 'crown', 'wand', 'sword', 'shield', 'armor', 'knife', 'weapon',
                 'ring', 'amulet', 'bracer', 'bracelet', 'boots', 'mirror']
        self.item_type = rdm.choice(types)

    def item_value(self):
        """Returns a randomly generated value"""
        value = rdm.randrange(5, 2500, 5)
        if self.jewel == '':
            coin = rdm.choice(['cp', 'cp', 'cp', 'sp', 'sp', 'gp'])
        else:
            coin = rdm.choice(['sp', 'gp', 'gp', 'gp', 'pp'])
        if self.material == "platinum":
            coin = 'pp'
        elif self.material == "gold":
            coin = rdm.choice(['gp', 'pp'])
        elif self.material == "silver":
            coin = rdm.choice(['sp', 'gp'])
        elif self.material in ['copper', 'brass']:
            coin = rdm.choice(['cp', 'sp'])
        self.value = str(value) + ' ' + coin

    def magic(self):
        """Randomly chooses a mild magic affect"""
        pass

    def curse(self):
        """Randomly chooses a curse"""
        pass

    def main(self):
        """Runs the item program, and returns a string containing the item and description"""
        self.description()
        self.item()
        self.item_value()
        mgc = rdm.random()
        if mgc > .50:
            self.magic()
        if mgc > .85:
            self.curse()
        item = "a " + self.adjective + ' ' + self.item_type + ' made of ' + self.material + ' worth ' + self.value
        if self.mgc != '':
            item += self.mgc
        if self.crs != '':
            item += self.crs
        return item

    def __str__(self):
        item = self.main()
        prompt = "Item prompt: "
        prompt += item
        return prompt


def main():
    item = Item()
    print(item)


if __name__ == "__main__":
    main()
