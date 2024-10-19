import pyglet
from lib import lib

# Ініціалізація допоміжних функцій
helper = lib()

# Створення вікна
window = helper.create_window(800, 600, "My Game")

# Створення графіки (коло)
shapes = helper.create_shape('circle', x=400, y=300, radius=50, color=(50, 255, 50))



# Функція оновлення гри
def update(dt):
    helper.update_physics(dt)



# Запуск гри
pyglet.app.run()
