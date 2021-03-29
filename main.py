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
rand1=0
rand2=0
def drawSnake(snakeLocation: List[number]):
    global rand1, rand2
    # clear the screen before drawing
    scrollbit.clear()
    # repeat this for every pair of coordinates
    for x in range(len(snakeLocation) / 2):
        # if x is length divided by two it has to be multiplied again
        scrollbit.set_pixel(snakeLocation[x * 2], snakeLocation[x * 2 + 1],50)
    scrollbit.set_pixel(snakeLocation[len(snakeLocation)-2], snakeLocation[len(snakeLocation)-1] )
    scrollbit.set_pixel(rand2, rand1)
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
    global rand1
    global rand2
    scrollbit.set_pixel(rand2, rand1,100)
    scrollbit.show()
    if snakeLocation[lengthfunc - 2] == rand2 and snakeLocation[lengthfunc - 1] == rand1:
        length= length + .5
    return length
drawSnake(snakeLocation)
def checkDeath(snakeLocation, lengthfunc):
    death = False
    if snakeLocation[lengthfunc-1] > 6 or snakeLocation[lengthfunc-2] > 16:
        death = True
    if snakeLocation[lengthfunc-1] < 0 or snakeLocation[lengthfunc-2] < 0:
        death = True
    return death

while True:
    food()
    lengthfunc = len(snakeLocation)
    snakeLocation = moveSnake(snakeLocation, direction, length)
    if checkDeath(snakeLocation, lengthfunc):
        direction = 0
        # cooper
        length = 1
        snakeLocation = [0, 0]
    drawSnake(snakeLocation)
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
    if checkDeath(snakeLocation, lengthfunc):
        direction = 0
        # cooper
        length = 1
        snakeLocation = [0, 0]