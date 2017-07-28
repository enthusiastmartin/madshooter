import pygame

from application.constants import BLACK, WHITE, WIDTH, HEIGHT

font_name = pygame.font.match_font('arial')


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def display_main_menu(screen):
    screen.fill(BLACK)

    while True:
        ev = pygame.event.poll()

        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_RETURN:
                break
            elif ev.key == pygame.K_q:
                pygame.quit()
                quit()
        else:
            draw_text(screen, "Press [ENTER] To Begin", 30, WIDTH / 2, HEIGHT / 2)
            draw_text(screen, "or [Q] To Quit", 30, WIDTH / 2, (HEIGHT / 2) + 40)
            pygame.display.update()
