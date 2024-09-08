import arcade
import time


class Sun(arcade.Sprite):
    def __init__(self, center_x, center_y):
        super().__init__("textures/plants/Sun/Sun_0.png", 0.12)
        for i in range(1, 22):
            self.append_texture(arcade.load_texture(f"textures/plants/Sun/Sun_{i}.png"))
        self.center_x = center_x
        self.center_y = center_y
        self.sun_time = time.time()

        self.scale = 0.5

    def update(self):
        self.angle += 1
        if time.time() - self.sun_time >= 10:
            self.kill()