from lib import lib

# Ініціалізація гри з твоєю бібліотекою
game = lib(width=800, height=600, title="My Awesome Game")

game.create_shape('circle', x = 300, y = 300, radius = 10, color=(92, 95, 105))


# Запуск гри
game.run()
