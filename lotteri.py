import random

class Lotteri:

    def init(self):

        self.list_vinster = [
            "Oskar",
            "Alvin",
            "Birk",
            "OskarsbiRk",
            "Alexs gymnasiearbete",
            "Spotify Premium i två och en halv månad",
            "ChromebookMAc",
            "Fönsterbräda",
            "Förstärkare",
            "Audi TT",
            "Eriks kalsonger",
            "Axels stulna tvål",
            "Linneas bollar",
            "En använd servett",
            "Iphone 17S",
            "Imsdal",
            "Minecraft 2",
            "Pirelli f1 soft däck",
            "Snigel",
            "Lazersvärd",
            "Sköld"
        ]


    def get_vinst(self):
        slumptal = random.randint(0,19)
        return self.list_vinster(slumptal)
