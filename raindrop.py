import pygame
from pygame.sprite import Sprite


class Raindrop(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize the rain drop and set its starting position."""
        super(Raindrop, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the rain drop image and set its rect attribute.
        self.image = pygame.image.load('images/raindrop.bmp')
        self.rect = self.image.get_rect()

        # Start each new rain drop near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the rain drop's exact position.
        self.y = float(self.rect.y)

    def blitme(self):
        """Draw the rain drop at its current location."""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return True if rain drop is at bottom of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.top >= screen_rect.bottom:
            return True

    def update(self):
        """Move the rain drop down."""
        self.y += self.ai_settings.rain_speed_factor
        self.rect.y = self.y
