#cooper
length = 1
direction = 0

snakeLocation = [
    0,
    0
]

def drawSnake(snakeLocation):
    scrollbit.clear()
    for x in range(len(snakeLocation)/2):
        scrollbit.set_pixel(snakeLocation[x*2], snakeLocation[(x*2)+1])
    scrollbit.show()

def moveSnake(snakeLocation, direction, length):
    if direction == 0:
        snakeLocation.append(snakeLocation[len(snakeLocation)-2] + 1)
        snakeLocation.append(snakeLocation[len(snakeLocation)-2])
    while (len(snakeLocation) / 2) > length:
        snakeLocation = snakeLocation[2:]
    return snakeLocation

while True:
    drawSnake(snakeLocation)
    snakeLocation = moveSnake(snakeLocation, direction, length)
    basic.pause(200)
