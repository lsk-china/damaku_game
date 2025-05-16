from sprites.base import Sprite, Enemy, Base
from util.action_queue import ActionQueue

class Game:
    def __init__(self):
        self.sprites = list[Sprite]
        self.enemies = list[Enemy]
        self.action_queue = ActionQueue[Base]()

    def initialize(self, file):
        # TODO
        pass

    def tick(self):
        current_action = self.action_queue.next()
        current_action.action(self)
        dead_indices = list[int]()
        entities = self.action_queue.get_actual_container()
        for

