import pyglet
from pyglet import shapes
import pymunk

class lib:
    def __init__(self, width=800, height=600, title="Game Window"):
        """Ініціалізація основних компонентів (графіка, фізика, звук)"""
        self.batch = pyglet.graphics.Batch()
        self.shapes = {}
        self.world = pymunk.Space()
        self.world.gravity = (0, -9.8)  # Гравітація
        self.window = pyglet.window.Window(width, height, title)
        self.key_handlers = {}

        @self.window.event
        def on_key_press(symbol, modifiers):
            if symbol in self.key_handlers:
                self.key_handlers[symbol]()

        @self.window.event
        def on_draw():
            self.window.clear()
            self.batch.draw()

    def create_shape(self, shape_type, *args, **kwargs):
        """Створення графічних об'єктів (коло, прямокутник і т.д.)"""
        if shape_type == 'circle':
            self.shapes['circle'] = shapes.Circle(*args, **kwargs, batch=self.batch)
        elif shape_type == 'rectangle':
            self.shapes['rectangle'] = shapes.Rectangle(*args, **kwargs, batch=self.batch)
        return self.shapes

    def update_physics(self, dt):
        """Оновлення фізики"""
        self.world.step(dt)

    def add_physics_object(self, mass, size, position):
        """Створення фізичного об'єкта (тіла)"""
        mass = mass
        radius = size
        inertia = pymunk.moment_for_circle(mass, 0, radius, (0, 0))
        body = pymunk.Body(mass, inertia)
        body.position = position
        shape = pymunk.Circle(body, radius)
        shape.density = 1.0
        shape.friction = 0.7
        self.world.add(body, shape)
        return body, shape

    def draw(self):
        """Відображення графічних об'єктів"""
        self.batch.draw()

    def update(self, dt):
        """Основне оновлення гри"""
        self.update_physics(dt)

    def run(self):
        """Запуск гри"""
        pyglet.app.run()

    def register_key_handler(self, key, handler):
        """Реєстрація обробника натискання клавіші"""
        self.key_handlers[key] = handler
