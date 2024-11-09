import pygame
import sys
import json
import random
import cv2
import time
from recognition import capture_emotion  # Assuming capture_emotion is in the recognition module
from fer import FER

# Initialize pygame
pygame.init()

# Screen settings
screen_width, screen_height = 1600, 1000
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

emotion_detector = FER()
cam = cv2.VideoCapture(0)

def question_slide(question_data, emotion_detector, cam):

    question_text = text_font.render(question_data[1], True, WHITE)
    question_rect = question_text.get_rect(center=(screen_width // 2, screen_height-100))

    # Drawing
    screen.fill(DARK_BLUE)
    screen.blit(question_text, question_rect)
    pygame.display.flip()

    # Capture emotion for 5 seconds
    emotion = capture_emotion(cam, emotion_detector)  
    print(f"Captured emotion: {emotion}")  

    # Display captured emotion (for debugging)
    emotion_text = text_font.render(f"Emotion: {emotion}", True, LIGHT_BLUE)
    emotion_rect = emotion_text.get_rect(center=(screen_width // 2, screen_height // 2 + 50))
    screen.blit(emotion_text, emotion_rect)
    pygame.display.flip()

    pygame.time.delay(2000)

    return emotion, question_data[0]

def load_policies():
    kamalaPolicy = json.load(open("policies.json"))[0]["policies"][0]
    trumpPolicy = json.load(open("policies.json"))[1]["policies"][0]
    policies = []

    for policy in kamalaPolicy:
        for p in kamalaPolicy[policy]:
            policies.append(("k", p))

    for policy in trumpPolicy:
        for p in trumpPolicy[policy]:
            policies.append(("t", p))

    random.shuffle(policies)
    return policies
    

def main_menu():
    policies = load_policies()

    while True:
        TrumpPoints = 0
        KamalaPoints = 0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    print("Get Started button clicked!")
                    for question_data in policies[:5]:
                        point = question_slide(question_data, emotion_detector, cam)
                        
                        if point[0] == "happy":

                            if point[1] == "t":
                                TrumpPoints += 1
                            else:
                                KamalaPoints += 1

                        elif point[0] == "sad":
                            if point[1] == "t":
                                TrumpPoints -= 1
                            else:
                                KamalaPoints -= 1

                        elif point[0] == "angry":
                            if point[1] == "t":
                                TrumpPoints -= 1
                            else:
                                KamalaPoints -= 1

                        elif point[0] == "surprise":
                            if point[1] == "t":
                                TrumpPoints -= 1
                            else:
                                KamalaPoints -= 1
                            
                    return (KamalaPoints, TrumpPoints)

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


def display_result(result):
    # Check who has the higher points
    if result[0] > result[1]:  # Kamala Harris has more points
        candidate_name = "Kamala Harris"
        candidate_image_path = "images/kamala-harris.jpeg"
    elif result[1] > result[0]:  # Trump has more points
        candidate_name = "Donald Trump"
        candidate_image_path = "images/donald-trump-mcdonalds.jpg"
    else:
        candidate_name = "Both candidates have equal points"
        candidate_image_path = "images/donald-trump-and-kamala.jpg"  # Placeholder image for equal points case

    # Load the appropriate image
    candidate_image = pygame.image.load(candidate_image_path)
    candidate_image = pygame.transform.scale(candidate_image, (300, 300))  # Adjust size as needed
    image_rect = candidate_image.get_rect(center=(screen_width // 2, screen_height // 2 - 50))

    # Display result text
    result_text = text_font.render(f"We match you to {candidate_name}", True, WHITE)
    result_rect = result_text.get_rect(center=(screen_width // 2, screen_height // 2 + 200))

    # Clear the screen and display the image and text
    screen.fill(DARK_BLUE)
    screen.blit(candidate_image, image_rect)
    screen.blit(result_text, result_rect)
    pygame.display.flip()

    # Delay before closing or moving to the next step
    pygame.time.delay(5000)

# Run the main menu
result = main_menu()
display_result(result)
pygame.quit()

