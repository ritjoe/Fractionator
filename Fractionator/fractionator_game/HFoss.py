#!/usr/bin/python
import pygame
from gi.repository import Gtk


class cards:
    def __init__(self):
        print("init card")


class button:
    def __init__(self, xLoc, yLoc, width, height):
        self.x = xLoc
        self.y = yLoc
        self.w = width
        self.h = height
        slef.color = (255, 0, 0)

    def isClicked(xLoc, yLoc):
        if (xLoc > self.x) and (xLoc < self.x + self.w) and (yLoc > self.y) and (yLoc < self.y + self.h):
            return true
        else:
            return false

    def drawButton(self):
        pygame.draw.rectangle(screen, self.color, (self.x, self.y), self.w, self.h)


class HFoss:
    def __init__(self):
        # Set up a clock for managing the frame rate.
        self.clock = pygame.time.Clock()

        # used for managing the gamestate
        self.gameState = 0

        self.x = -100
        self.y = 100

        self.vx = 10
        self.vy = 0

        self.paused = False
        self.direction = 1

        startButton = Button(10, 10, 100, 50)
        replayButton = Button(10, 30, 100, 50)

    def replay(self):
        # reset variables
        self.gameState = 0

    def set_paused(self, paused):
        self.paused = paused

    # Called to save the state of the game to the Journal.
    def write_file(self, file_path):
        pass

    # Called to load the state of the game from the Journal.
    def read_file(self, file_path):
        pass

    # The main game loop.
    def run(self):
        self.running = True

        screen = pygame.display.get_surface()

        while self.running:
            # Pump GTK messages.
            while Gtk.events_pending():
                Gtk.main_iteration()

            # Pump PyGame messages.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.VIDEORESIZE:
                    pygame.display.set_mode(event.size, pygame.RESIZABLE)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.direction = -1
                    elif event.key == pygame.K_RIGHT:
                        self.direction = 1

            # Play Game
            if not self.paused:
                # Start Screen
                if gameState == 0:
                    # Clear Display
                    screen.fill((255, 255, 255))  # 255 for white

                    # Draw the button
                    startButton.drawButton()

                    if startButton.isClicked():
                        gameState = 1

                # Game
                elif gameState == 1:
                    # Move Ball
                    self.x += self.vx * self.direction
                    if self.direction == 1 and self.x > screen.get_width() + 100:
                        self.x = -100
                    elif self.direction == -1 and self.x < -100:
                        self.x = screen.get_width() + 100

                    self.y += self.vy
                    
                    if self.y > screen.get_height() - 100:
                        self.y = screen.get_height() - 100
                        self.vy = -self.vy

                    self.vy += 5

                    # Clear Display
                    screen.fill((255, 255, 255))  # 255 for white
                    # Draw the ball
                    pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), 100)

                    # Flip Display
                    pygame.display.flip()

                    # Try to stay at 30 fps
                    self.clock.tick(30)

                    if self.x > screen.get_width() + 100:
                        gameState == 2

                    # Game Over
                elif gameState == 2:
                    # Clear Display
                    screen.fill((255, 255, 255))  # 255 for white
	
                    # Draw the button
                    replayButton.drawButton()
                    if replayButton.isClicked():
                        replay()


# This function is called when the game is run directly from the command line:
# ./TestGame.py
def main():
    pygame.init()
    pygame.display.set_mode((0, 0), pygame.RESIZABLE)
    game = hfoss()
    game.run()

if __name__ == '__main__':
    main()
