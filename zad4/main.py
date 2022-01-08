import random


class FunClass:
    PopularNames = ["Olivia", "Liam", "Emma", "Noah", "Amelia", "Oliver", "Ava", "Elijah", "Sophia", "Lucas"]
    Games = ["Call of Duty", "Minecraft", "Fortnite", "Overwatch", "Dota 2", "League of Legends", "Counter Strike",
             "Hearthstone", "Heroes of the Storm"]

    def is_your_name_popular(self, name) -> bool:
        if name in self.PopularNames:
            return True
        else:
            return False

    def what_is_my_tau_mark(self) -> float:
        return random.randint(2, 5)

    def get_random_popular_game(self) -> str:
        return random.choice(self.Games)


class NotFunClass:
    Pi = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"

    def get_pi_with_selected_length(self, length) -> str:
        return self.Pi[:length+1]

    def return_Fun_Class_or_None(self):
        if random.randint(0, 1) == 0:
            return None
        else:
            return FunClass()

    def get_random_number(self, a, b) -> int:
        return random.randint(a, b)
