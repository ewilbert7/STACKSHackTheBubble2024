import pygame
import sys
import json
import random
import cv2
from recognition import capture_emotion  # Assuming capture_emotion is in the recognition module
from fer import FER

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

# Initialize FER for emotion detection
emotion_detector = FER()

# Initialize the camera
cam = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Questions and options
questions = [
    "What is your preferred programming language?",
    "What is your preferred job title?",
    "What is your current salary range?",
    "What is your preferred company size?",
    "What is your preferred industry?"
]

def display_emotion(emotion):
    # Display the emotion captured by the camera
    emotion_text = text_font.render(f"Detected Emotion: {emotion}", True, WHITE)
    emotion_rect = emotion_text.get_rect(center=(screen_width // 2, screen_height // 1.5))
    screen.blit(emotion_text, emotion_rect)


# def question_slide(question):
#     question_text = text_font.render(question, True, WHITE)
#     question_rect = question_text.get_rect(center=(screen_width // 2, screen_height // 4))

#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()

#         # Drawing
#         screen.fill(DARK_BLUE)
#         screen.blit(question_text, question_rect)

#         # Get the emotion from the capture_emotion function
#         emotion = capture_emotion()

#         # Display the detected emotion
#         display_emotion(emotion)

#         # Update the screen
#         pygame.display.flip()

#         # Wait for user input or a timeout to proceed to the next question
#         for event in pygame.event.get():
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 return  # Proceed to next question when clicked

def question_slide(question, emotion_detector, cam):
    question_text = text_font.render(question, True, WHITE)
    question_rect = question_text.get_rect(center=(screen_width // 2, screen_height // 4))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Drawing
    screen.fill(DARK_BLUE)
    screen.blit(question_text, question_rect)
    
     # Display the question and capture emotion
    emotion = capture_emotion(cam, emotion_detector)  # Capture emotion continuously during the question
    print(f"Captured emotion: {emotion}")  

    # Display captured emotion (for debugging)
    emotion_text = text_font.render(f"Emotion: {emotion}", True, LIGHT_BLUE)
    emotion_rect = emotion_text.get_rect(center=(screen_width // 2, screen_height // 2 + 50))
    screen.blit(emotion_text, emotion_rect)

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

# def main_menu():
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 if button_rect.collidepoint(event.pos):
#                     print("Get Started button clicked!")
#                     for question in questions:
#                         question_slide(question)
#                     return

# Main menu or entry point
def main_menu():
    #load_policies()
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    print("Get Started button clicked!")
                    for question_data in questions:
                        question_slide(question_data, emotion_detector, cam)
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
        

# Start the main menu
main_menu()
pygame.quit()

# Run the main menu
main_menu()
pygame.quit