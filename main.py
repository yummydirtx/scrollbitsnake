#cooper
length = 1
direction = 0

snakeLocation = [
    0,
    0
]

def drawSnake(snakeLocation):
    # clear the screen before drawing
    scrollbit.clear()
    # repeat this for every pair of coordinates
    for x in range(len(snakeLocation)/2):
        # if x is length divided by two it has to be multiplied again
        scrollbit.set_pixel(snakeLocation[x*2], snakeLocation[(x*2)+1])
    # show the world
    scrollbit.show()

def moveSnake(snakeLocation, direction, length):
    # if going to the right
    if direction == 0:
        snakeLocation.append(snakeLocation[len(snakeLocation)-2] + 1)
        snakeLocation.append(snakeLocation[len(snakeLocation)-2])
    while (len(snakeLocation) / 2) > length:
        # remove extra snake
        snakeLocation = snakeLocation[2:]
    return snakeLocation

while True:
    drawSnake(snakeLocation)
    snakeLocation = moveSnake(snakeLocation, direction, length)
    basic.pause(200)
