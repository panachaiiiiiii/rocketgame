score = 0
ballY = 0
playerX = 0
ballX = 2
playerX = 2

def on_button_pressed_a():
    global playerX
    if playerX > 0:
        playerX += -1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global playerX
    if playerX < 4:
        playerX += 1
input.on_button_pressed(Button.B, on_button_pressed_b)



def on_forever():
    global ballY, ballX, score
    basic.clear_screen()
    ballY += 1
    if ballY == 5:
        ballY = 0
        ballX = Math.random_range(0, 4)
    led.plot(ballX, ballY)
    led.plot(playerX, 4)
    if ballY == 4 and ballX == playerX:
        score += 1
        basic.show_number(score)
    basic.pause(500)
basic.forever(on_forever)
