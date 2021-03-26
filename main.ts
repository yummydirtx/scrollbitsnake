// cooper
let length = 1
let direction = 0
let snakeLocation = [0, 0]
function drawSnake(snakeLocation: number[]) {
    //  clear the screen before drawing
    scrollbit.clear()
    //  repeat this for every pair of coordinates
    for (let x = 0; x < snakeLocation.length / 2; x++) {
        //  if x is length divided by two it has to be multiplied again
        scrollbit.setPixel(snakeLocation[x * 2], snakeLocation[x * 2 + 1])
    }
    //  show the world
    scrollbit.show()
}

function moveSnake(snakeLocation: number[], direction: number, length: number): number[] {
    //  if going to the right
    if (direction == 0) {
        snakeLocation.push(snakeLocation[snakeLocation.length - 2] + 1)
        snakeLocation.push(snakeLocation[snakeLocation.length - 2])
    }
    
    while (snakeLocation.length / 2 > length) {
        //  remove extra snake
        snakeLocation = snakeLocation.slice(2)
    }
    return snakeLocation
}

while (true) {
    drawSnake(snakeLocation)
    snakeLocation = moveSnake(snakeLocation, direction, length)
    basic.pause(200)
}
