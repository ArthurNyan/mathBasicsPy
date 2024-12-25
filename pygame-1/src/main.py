import pygame
import sys
import numpy as np
from squares.graphics import Drawer
from squares.transform import create_translation_matrix, create_scaling_matrix, create_rotation_matrix

# Define constants
WINDOW_SIZE = (800, 600)
FPS = 30
NUM_ITERATIONS = 20
COLOR = (255, 255, 255)

def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Square Funnel")
    clock = pygame.time.Clock()
    
    drawer = Drawer(screen, WINDOW_SIZE)
    
    # Define initial square
    a = 100
    L = np.array([[a, -a, -a, a, a],
                  [a, a, -a, -a, a],
                  [1, 1, 1, 1, 1]])
    
    # Define transformation matrices
    xc, yc = 0, 0  # Center of the square in the coordinate system
    Tc = create_translation_matrix(-xc, -yc)
    S = create_scaling_matrix(0.9, 0.9)
    alpha = np.pi / 64
    R = create_rotation_matrix(alpha)
    Tdelta = create_translation_matrix(xc, yc)
    M = Tdelta @ R @ S @ Tc
    
    # Initialize list to store all squares
    squares = []
    current_L = L.copy()
    
    # Number of transformations performed
    transformation_step = 0
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        if transformation_step < NUM_ITERATIONS:
            # Apply transformation
            current_L = M @ current_L
            current_L[:2, :] /= current_L[2, :]
            # Append the 2D coordinates
            squares.append(current_L[:2, :].copy())
            transformation_step += 1
        
        # Clear the screen
        screen.fill((0, 0, 0))
        
        # Draw all squares
        for square in squares:
            drawer.draw_polygon(square, COLOR)
        
        # Update display
        pygame.display.update()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()