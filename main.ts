// cooper
let length = 1
let direction = 0
let snakeLocation = [0, 0]
function drawSnake(snakeLocation: number[]) {
    scrollbit.clear()
    for (let x = 0; x < snakeLocation.length / 2; x++) {
        scrollbit.setPixel(snakeLocation[x * 2], snakeLocation[x * 2 + 1])
    }
    scrollbit.show()
}

function moveSnake(snakeLocation: number[], direction: number, length: number): number[] {
    if (direction == 0) {
        snakeLocation.push(snakeLocation[snakeLocation.length - 2] + 1)
        snakeLocation.push(snakeLocation[snakeLocation.length - 2])
    }
    
    while (snakeLocation.length / 2 > length) {
        snakeLocation = snakeLocation.slice(2)
    }
    return snakeLocation
}

while (true) {
    drawSnake(snakeLocation)
    snakeLocation = moveSnake(snakeLocation, direction, length)
    basic.pause(200)
}
