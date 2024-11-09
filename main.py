import pygame
import sys
import json
import random

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
OPTION_COLOR = (200, 200, 200)
OPTION_HOVER_COLOR = (150, 150, 150)

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

# Questions and options
questions = [
    {
        "question": "What is your area of expertise?",
        "options": ["Software Development", "Data Science", "Product Management", "Cybersecurity"]
    },
    {
        "question": "How many years of experience do you have?",
        "options": ["0-2 years", "3-5 years", "6-10 years", "10+ years"]
    },
]

def question_slide(question_data):
    question_text = text_font.render(question_data["question"], True, WHITE)
    question_rect = question_text.get_rect(center=(screen_width // 2, screen_height // 4))

    # Generate option surfaces and rectangles
    option_rects = []
    for i, option in enumerate(question_data["options"]):
        option_surface = text_font.render(option, True, DARK_BLUE)
        option_rect = option_surface.get_rect(center=(screen_width // 2, screen_height // 2 + i * 50))
        option_rects.append((option, option_surface, option_rect))  # Store the text, surface, and rect

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for option_text, option_surface, option_rect in option_rects:
                    if option_rect.collidepoint(event.pos):
                        print(f"Selected option: {option_text}")  # Use option_text directly
                        return  # Move to the next slide or end the quiz

        # Drawing
        screen.fill(DARK_BLUE)
        screen.blit(question_text, question_rect)

        # Draw each option
        mouse_pos = pygame.mouse.get_pos()
        for option_text, option_surface, option_rect in option_rects:
            color = OPTION_HOVER_COLOR if option_rect.collidepoint(mouse_pos) else OPTION_COLOR
            pygame.draw.rect(screen, color, option_rect.inflate(10, 10))  # Draw background rectangle for option
            screen.blit(option_surface, option_rect)

        pygame.display.flip()

def load_policies():
    kamalaPolicy = json.load(open("policies.json"))[0]["policies"][0]
    trumpPolicy = json.load(open("policies.json"))[1]["policies"][0]
    policies = []

    for policy in kamalaPolicy:
        for p in kamalaPolicy[policy]:
            policies.append(p)

    for policy in trumpPolicy:
        for p in trumpPolicy[policy]:
            policies.append(p)

    random.shuffle(policies)
    print(policies)
    

def main_menu():
    load_policies()
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    print("Get Started button clicked!")
                    for question_data in questions:
                        question_slide(question_data)
                    return

        # Drawing main menu
        screen.fill(DARK_BLUE)
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
