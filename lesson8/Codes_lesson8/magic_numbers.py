# Магические числа (Magic numbers)
def draw_sprite(arg1, arg2, arg3):
    pass


# визуально непонятно что означает каждый из параметров
draw_sprite(53, 320, 240)

# самым простым решением будет сделать параметры константами
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_X_CENTER = SCREEN_WIDTH / 2
SCREEN_Y_CENTER = SCREEN_HEIGHT / 2
SPRITE_CROSSHAIR = 53

draw_sprite(SPRITE_CROSSHAIR, SCREEN_X_CENTER, SCREEN_Y_CENTER)
