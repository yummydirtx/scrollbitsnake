def on_button_pressed_a():
    global direction
    if direction == 0:
        direction = 3
    elif direction == 1:
        direction = 0
    elif direction == 2:
        direction = 1
    elif direction == 3:
        direction = 2
def on_button_pressed_b():
    global direction
    if direction == 0:
        direction = 1
    elif direction == 1:
        direction = 2
    elif direction == 2:
        direction = 3
    elif direction == 3:
        direction = 0
ppFlag = False
direction = 0
# cooper
length = 1
snakeLocation = [0, 0]
def drawSnake(snakeLocation: List[number]):
    # clear the screen before drawing
    scrollbit.clear()
    # repeat this for every pair of coordinates
    for x in range(len(snakeLocation) / 2):
        # if x is length divided by two it has to be multiplied again
        scrollbit.set_pixel(snakeLocation[x * 2], snakeLocation[x * 2 + 1])
    # show the world
    scrollbit.show()
def moveSnake(snakeLocation: List[number], direction: number, length: number):
    # if going to the right
    if direction == 0:
        snakeLocation.append(snakeLocation[len(snakeLocation) - 2] + 1)
        snakeLocation.append(snakeLocation[len(snakeLocation) - 2])
    elif direction == 1:
        snakeLocation.append(snakeLocation[len(snakeLocation) - 2])
        snakeLocation.append(snakeLocation[len(snakeLocation) - 2] + 1)
    elif direction == 2:
        snakeLocation.append(snakeLocation[len(snakeLocation) - 2] - 1)
        snakeLocation.append(snakeLocation[len(snakeLocation) - 2])
    elif direction == 3:
        snakeLocation.append(snakeLocation[len(snakeLocation) - 2])
        snakeLocation.append(snakeLocation[len(snakeLocation) - 2] - 1)
    while len(snakeLocation) / 2 > length:
        # remove extra snake
        snakeLocation = snakeLocation.slice(2)
    return snakeLocation
def food():
    global length
    if snakeLocation[lengthfunc - 2] == 1 and snakeLocation[lengthfunc - 1] == 1:
        length= length +.5
    return length
def deathCheck(snakeLocation):
    if 

drawSnake(snakeLocation)
while True:
    lengthfunc = len(snakeLocation)
    snakeLocation = moveSnake(snakeLocation, direction, length)
    drawSnake(snakeLocation)
    food()
    for x2 in range(200):
        if ppFlag == False:
            if input.button_is_pressed(Button.A):
                on_button_pressed_a()
                ppFlag = True
            if input.button_is_pressed(Button.B):
                on_button_pressed_b()
                ppFlag = True
        basic.pause(1)
    ppFlag = False