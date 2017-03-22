from gamelib import *

game = Game(800,600,"Game Project")

bk = Image("images\\desert.jpg",game)
bk.resizeTo(game.width,game.height)

ammo = 20

title = Image("images\\logo.png",game)
bk.draw()
title.draw()
game.drawText("Press [SPACE] to Begin",320, 400)
game.update(1)
game.wait(K_SPACE)

instructions = Image("images\\instructions.png",game)

'''
while not game.over:
    game.processInput()

    instructions.draw()
    game.wait(K_SPACE)

    game.update(1)
'''
roadrunner = Animation("images\\roadrunner.png",2,game,950,297,4)
roadrunner.resizeBy(-65)
roadrunner.setSpeed(4,30)

crosshair = Image("images\\crosshair.png", game)
crosshair.resizeBy(-80)

lizard = Image("images\\lizard.png",game)
lizard.resizeBy(-40)
lizard.setSpeed(4,30)
lizard.moveTo(200,200)

gun = Sound("sound\\Gun.wav",1)
gun2 = Sound("sound\\Sniper.wav",2)
beep = Sound("sound\\beepbeep.wav",3)

roadrunner2 = Animation("images\\roadrunner2.png",2,game,950,297,4)
roadrunner2.resizeBy(-65)
roadrunner2.moveTo(200,200)

lizard2 = Image("images\\lizard2.png",game)
lizard2.resizeBy(-40)
lizard2.moveTo(200,200)

while not game.over:
    game.processInput()

    roadrunner2.makeVisible(False)
    lizard2.makeVisible(False)
    
    if roadrunner.health < 5:
        gun2.play()
        roadrunner.makeVisible(False)
        roadrunner2.makeVisible(True)
        game.over = True

    if lizard.health < 5:
        lizard.makeVisible(False)
        lizard2.makeVisible(True)
        game.over = True
    
    bk.draw()
    roadrunner2.draw()
    lizard2.draw()
    roadrunner.move(True)
    lizard.move(True)
    crosshair.moveTo(mouse.x, mouse.y)
    
    if roadrunner.collidedWith(mouse) and mouse.LeftButton:
        beep.play()
        xCoordinate = randint(150,650)
        yCoordinate = randint(150,450)
        roadrunner.moveTo(xCoordinate, yCoordinate)
        roadrunner.speed += 0.5
        roadrunner.health -= 5
        game.score += 5
        ammo -= 1
        
    if roadrunner.collidedWith(lizard):
        xCoordinate = randint(100,700)
        yCoordinate = randint(100,500)
        lizard.moveTo(xCoordinate, yCoordinate)
        lizard.health -= 5

    if mouse.LeftButton:
        gun.play()

    game.drawText("Road Runner Health: " + str(roadrunner.health), 200, 5)
    game.drawText("Lizard Health: " + str(lizard.health),500,5)
    game.drawText("Ammo: " + str(ammo),700,5)
           
    game.displayScore() #displays the score
    game.update(60) #updates the game
over = Image("images\\gameover.png",game)
over.draw()
game.drawText("Press [ESC] to Exit",200,400)
game.update(1)
game.wait(K_ESCAPE)
game.quit()
