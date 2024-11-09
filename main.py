import pygame
import sys

# Initialize pygame
pygame.init()

# Screen settings
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Candidate Connect")

# Colors
WHITE = (255, 255, 255)
DARK_BLUE = (18, 32, 47)
LIGHT_BLUE = (100, 149, 237)
BUTTON_COLOR = (70, 130, 180)
BUTTON_HOVER_COLOR = (100, 149, 237)

# Fonts
title_font = pygame.font.Font(None, 74)
text_font = pygame.font.Font(None, 36)
button_font = pygame.font.Font(None, 48)

# Texts
title_text = title_font.render("Welcome to Candidate Connect", True, LIGHT_BLUE)
title_rect = title_text.get_rect(center=(screen_width // 2, screen_height // 3))

desc_text = text_font.render("Find the best candidate match for you!", True, WHITE)
desc_rect = desc_text.get_rect(center=(screen_width // 2, screen_height // 2))

# Button settings
button_text = button_font.render("Get Started", True, WHITE)
button_width, button_height = 200, 60
button_rect = pygame.Rect((screen_width // 2 - button_width // 2, screen_height // 1.5), (button_width, button_height))

def main_menu():
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    print("Get Started button clicked!")
                    return  # Exit main menu when the button is clicked

        # Drawing
        screen.fill(DARK_BLUE)

        # Draw title and description
        screen.blit(title_text, title_rect)
        screen.blit(desc_text, desc_rect)

        # Draw button
        mouse_pos = pygame.mouse.get_pos()
        if button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, BUTTON_HOVER_COLOR, button_rect)
        else:
            pygame.draw.rect(screen, BUTTON_COLOR, button_rect)
        
        screen.blit(button_text, button_text.get_rect(center=button_rect.center))

        pygame.display.flip()

# Run the main menu
main_menu()
pygame.quit()
