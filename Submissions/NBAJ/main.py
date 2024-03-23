import numpy as np
import pygame
import math

G = 100
AU = 1.4960e11 #meters

class Particle:
    def __init__(self,x,y,mass,ini_vx, ini_vy) -> None:
        self.x = x
        self.y = y
        self.mass = mass
        self.vx = ini_vx
        self.vy = ini_vy

    def get_r(self,b_x,b_y):
        self.r = math.sqrt(((b_x - self.x)**2) + ((b_y - self.y)**2))

    def get_fgrav(self,b_m):
        self.fgrav = (G * b_m * self.mass)/(self.r**2)

    def get_theta(self,b_x,b_y):
        self.theta = math.atan2((b_y-self.y), (b_x-self.x))

    def get_fx(self):
        self.fx = self.fgrav*math.cos(self.theta)

    def get_fy(self):
        self.fy = -self.fgrav*math.sin(self.theta)

    def get_dv_x(self,dt):
        return (self.fx/self.mass)*dt

    def get_dv_y(self, dt):
        return (self.fy/self.mass)*dt

def main():
    SCREEN_X, SCREEN_Y = 800,500
    screen = pygame.display.set_mode([SCREEN_X, SCREEN_Y])
    x = 100
    y = 100
    prev_x = 100
    prev_y = 100
    dv_x = 0
    dv_y = 0
    # Run until the user asks to quit
    dt = 0.05
    mass = 3
    b_mass = 1000
    running = True
    particle = Particle(x,y,mass,3,3)
    positive = True
    while running:

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the background with white
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (0, 0, 0), (SCREEN_X//2, SCREEN_Y//2), 50)
        # Update velocities
        particle.get_r(SCREEN_X//2,SCREEN_Y//2)
        particle.get_fgrav(b_mass)
        particle.get_theta(SCREEN_X//2,SCREEN_Y//2)
        particle.get_fx()
        particle.get_fy()
        dv_x = particle.get_dv_x(dt)
        dv_y = particle.get_dv_y(dt)

        particle.vx += dv_x * dt
        particle.vy += dv_y * dt

        # Update location
        x += particle.vx * dt
        y += particle.vy * dt
        pygame.draw.circle(screen, (255, 0, 0), (x,y), 5)
        pygame.draw.lines(screen,color=0,points=[(prev_x,prev_y),(x,y)],width=2,closed=True)
        # Flip the display
        pygame.display.flip()
        if positive:
            positive = False
        else:
            positive = True
        
        prev_x,prev_y = x,y

    # Done! Time to quit.
    pygame.quit()

main()
