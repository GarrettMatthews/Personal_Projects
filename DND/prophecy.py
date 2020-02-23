"""

Program to generate a random prophecy

Garrett Matthews

"""

import random as rdm


class Prophecy:

    def __init__(self):
        self.event = ''
        self.sign = ''

    def warning(self):
        """Returns a warning/event of something to come"""
        lyst = ["a storm is coming", "a dark shadow rises", "a curse will soon befall that which you hold dear",
                "an evil is rising", "dark whispers will echo across the land", "a dark fire will burn",
                "a deep hatred will be revealed", "a flood of anger is coming", "the world will crack",
                "beware the half-covered eye", "watch for the crooked smile"]
        self.event = rdm.choice(lyst)

    def signal(self):
        """Returns a sign to look for the future event"""
        lyst = ["an angled, hooded figure", "a snow drenched canine", "a serpentine shadow", "the loose fang",
                "the broken dagger", "an empty footprint", "the broken crown", "the lost child", "the naked rose",
                "the frosted claw", "a kingdom in turmoil"]
        self.sign = rdm.choice(lyst)

    def main(self):
        """Runs the Prophecy program, returning a prophecy prompt"""
        self.warning()
        self.signal()
        prompt = "watch for " + self.sign + ', for when you see it know that ' + self.event
        return prompt

    def __str__(self):
        proph = self.main()
        prompt = "Prophecy prompt: "
        prompt += proph
        return prompt


def main():
    """Tests and runs the prophecy program"""
    print(Prophecy())


if __name__ == '__main__':
    main()
