import pygame, sys
from button import Button

pygame.init()
#Pantalla
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Quizi")

#Fondo Menu
BG = pygame.image.load("assets/fondo.png")
#Fuente
def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)
#Pantalla 2 Instrucciones
def instru():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill((0, 74, 173))

        PLAY_TEXT = get_font(60).render("INSTRUCCIONES ", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(200, 100))
        INTRU_TEXT = get_font(40).render("Bienvenido!\n Quizi es una aplicación que busca hacer el proceso de aprendisaje más entretenido\nPrimero, tendra que seleccionar la cantidad de preguntas que desea constestar\nEn el menu de pregunta seleccione la pregunta que usted concidere correcta, tendra 60 segundas para constestar cada una\nSuerte!", True, "White")
        INTRU_RECT = INTRU_TEXT.get_rect(center=(200,100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        SCREEN.blit(INTRU_TEXT, INTRU_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()
#Pantalla 3 (aun no incluida, debe de ser llamada por instru)
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()
#Pantalla 1 Menu
def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("QUIZI", True, "#FFFFFF")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        MENU_CREDIT = get_font(50).render("By. Alan, Jesus, Pablo, Emerson y Juan", True, "#FFFFFF")
        MENU_RECTDOS = MENU_CREDIT.get_rect(center=(640, 620))


        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 380), 
                            text_input="Empezar", font=get_font(90), base_color="White", hovering_color="Green")
        SCREEN.blit(MENU_CREDIT, MENU_RECTDOS)        
        SCREEN.blit(MENU_TEXT, MENU_RECT)
        

        for button in [PLAY_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    instru()

        pygame.display.update()

main_menu()