from game import Game
from skill.base import Skill

class Entity:
    """
        Entity
        Parent class for all game entities (sprites and mobs)
    """

    def __init__(self, hp: float, primary_skill: Skill, secondary_skills: list[Skill]):
        """
        Initialize attributes
        :param self: refers to this instance
        :param hp: Maximum hp for this entity
        :param primary_skill: primary skill, performed when actor is this entity
        :param secondary_skills: secondary skills, performed after each action, no matter if actor is this entity
        """
        self.hp = hp
        self.primary_skill = primary_skill
        self.secondary_skills = secondary_skills
        self.index = 0

    def get_hp(self) -> float:
        """
        Get HP information of this entity
        :param self: refers to this instance
        :return: HP information
        """
        return self.hp

    def action(self, game: Game) -> None:
        """
        Action logic of this entity.
        Performs the primary action.
        :param self: refers to this instance.
        :param game: Game instance to modify.
        """
        self.primary_skill.action(game)

    def set_index(self, index: int) -> None:
        """
        Set index of this entity, in the actual container of the ActionQueue.
        For convenience when this entity is dead and should be removed from the ActionQueue.
        :param index: The index
        """
        self.index = index

    def get_index(self) -> int:
        """
        Get index of this entity, in the actual container of the ActionQueue.
        :return: The index
        """
        return self.index

    def perform_secondary_action(self, game: Game) -> None:
        """
        Check and perform secondary skills for this entity. Will do nothing if this entity is dead.
        Called after each action.
        :param game: The game instance to modify.
        """
        # Do nothing if this entity is dead.
        if self.hp <= 0:
            return

        for secondary_skill in self.secondary_skills:
            secondary_skill.action(game)

class Sprite(Entity):
    def __init__(self, hp, primary_skill, secondary_skill):
        Entity.__init__(self, hp, primary_skill, secondary_skill)

class Enemy(Entity):
    def __init__(self, hp, primary_skill, secondary_skill):
        Entity.__init__(self, hp, primary_skill, secondary_skill)