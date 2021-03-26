
length = 2
direction = 0

snakeLocation = [
    0,
    0
]

def drawSnake(snakeLocation):
    for x in range(len(snakeLocation)/2):
        scrollbit.set_pixel(snakeLocation[x*2], snakeLocation[(x*2)+1])
    scrollbit.show()

drawSnake(snakeLocation)