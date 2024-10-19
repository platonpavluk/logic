import pyglet
from pyglet import shapes
import pymunk
import soundfile as sf
import pyaudio

class lib:
    def __init__(self):
        # Ініціалізація основних компонентів (графіка, фізика, звук)
        self.batch = pyglet.graphics.Batch()
        self.shapes = {}
        self.world = pymunk.Space()
        self.world.gravity = (0, -9.8)  # Гравітація
        self.audio_data = None
        self.sample_rate = None
        self.window = None

    def create_window(self, width, height, title="Game Window"):
        """Створення вікна гри"""
        if self.window is None:
            self.window = pyglet.window.Window(width, height, title)
        return self.window

    def create_shape(self, shape_type, *args, **kwargs):
        """Створення графічних об'єктів (кола, прямокутник і т.д.)"""
        if shape_type == 'circle':
            self.shapes['circle'] = shapes.Circle(*args, **kwargs, batch=self.batch)
        elif shape_type == 'rectangle':
            self.shapes['rectangle'] = shapes.Rectangle(*args, **kwargs, batch=self.batch)
        return self.shapes

    def load_sound(self, file_path):
        """Завантаження аудіофайлу"""
        self.audio_data, self.sample_rate = sf.read(file_path)
        return self.audio_data, self.sample_rate

    def play_sound(self):
        """Відтворення звуку"""
        if self.audio_data is not None:
            stream = pyaudio.PyAudio().open(format=pyaudio.paInt16, channels=1, rate=self.sample_rate, output=True)
            stream.write(self.audio_data.tobytes())

    def handle_keys(self, window, on_key_press=None, on_key_release=None):
        """Обробка натискання та відпускання клавіші"""
        window.push_handlers(on_key_press=on_key_press, on_key_release=on_key_release)

    def update_physics(self, dt):
        """Оновлення фізики"""
        self.world.step(dt)  # Оновлення фізики

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
        self.draw()

# Основний файл для гри
if __name__ == "__main__":
    game = GameHelper()


