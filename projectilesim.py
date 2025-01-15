import pygame
import matplotlib.pyplot as plt
import math

def init_pygame():
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Projectile Motion Simulation")
    return screen

def calculate_trajectory(angle, velocity, air_resistance, wind_speed, dt = 0.1):
    angle_rad = math.radians(angle)
    vx = velocity*math.cos(angle_rad) + wind_speed
    vy = velocity*math.sin(angle_rad)
    g = 9.81
    x,y = 0,0
    trajectory = [(x,y)]

    while y>=0:
        ax = -air_resistance*vx
        ay = -g - air_resistance*vy
        vx += ax*dt
        vy += ay*dt
        x += vx*dt
        y += vy*dt
        if y>=0:
            trajectory.append((x,y))

    return trajectory


def plot_trajectory(trajectory):
    x_vals,y_vals = zip(*trajectory)
    plt.figure(figsize = (10,5))
    plt.plot(x_vals,y_vals,label = 'Projectile Path')
    plt.title('Projectile Motion with Air Resistance and Wind Effect')
    plt.xlabel('Distance(m)')
    plt.ylabel('Height(m)')
    plt.legend()
    plt.grid(True)
    plt.show()

def run_simulation():
    screen = init_pygame()
    clock = pygame.time.Clock()
    running = True

    angle = 45
    velocity = 50
    air_resistance = 0.01
    wind_speed = 0.0

    trajectory = calculate_trajectory(angle,velocity,air_resistance,wind_speed)
    plot_trajectory(trajectory)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255,255,255))
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    run_simulation()
