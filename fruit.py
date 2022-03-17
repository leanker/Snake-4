from pygame.math import Vector2

class FRUIT:
    def __init__(self):
        self.x = 5
        self.y = 4
        self.pos = Vector2(self.x,self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x, self.pos.y ,)