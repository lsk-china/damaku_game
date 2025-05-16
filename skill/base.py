from game import Game

class Skill:
    def __init__(self, skill_id, skill_name):
        self.id = skill_id
        self.name = skill_name

    def action(self, game: Game):
        raise NotImplementedError