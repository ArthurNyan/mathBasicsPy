import pygame
import numpy as np

class Drawer:
    def __init__(self, screen, window_size):
        self.screen = screen
        self.width, self.height = window_size
        self.color = (255, 255, 255)
    
    def draw_polygon(self, points, color, width=1):
        # Convert points to pixel coordinates
        pixel_points = [self._to_pixel(x, y) for x, y in zip(points[0], points[1])]
        # Draw the polygon
        pygame.draw.polygon(self.screen, color, pixel_points, width)
    
    def _to_pixel(self, x, y):
        # Convert coordinates to screen pixels
        return (self.width // 2 + int(x), self.height // 2 - int(y))