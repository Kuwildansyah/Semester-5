import pygame
import sys
import random

# Game constants
WIDTH, HEIGHT = 800, 600
SPEED = 3
BULLET_SPEED = 5
ENEMY_SPEED = 1
SCORE = 0
ENEMY_COUNT = 1

# Initialize Pygame
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.Font(None, 36)

# Functional helpers
def create_player(x, y):
    return pygame.Rect(x, y, 50, 50)

def create_bullet(x, y):
    return pygame.Rect(x, y, 10, 20)

def create_enemy():
    return pygame.Rect(random.randrange(100, 700), 50, 50, 50)

def draw_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    win.blit(text_surface, (x, y))

def draw_rect(color, rect):
    pygame.draw.rect(win, color, rect)

def draw_window(player, bullets, enemies):
    win.fill((0, 0, 0))
    draw_text(f"Score: {SCORE}", (255, 255, 255), 10, 10)
    draw_rect((255, 255, 255), player)
    for enemy in enemies:
        draw_rect((255, 0, 0), enemy)
    for bullet in bullets:
        draw_rect((0, 255, 0), bullet)
    pygame.display.update()

def handle_bullets(bullets, enemies):
    global SCORE
    new_bullets = []
    for bullet in bullets:
        bullet.y -= BULLET_SPEED
        hit_enemy = next((enemy for enemy in enemies if bullet.colliderect(enemy)), None)
        if hit_enemy:
            SCORE += 10
            enemies.remove(hit_enemy)
        else:
            new_bullets.append(bullet)

    bullets_to_create = len(bullets) - len(new_bullets)
    new_bullets += [create_bullet(random.randrange(100, 700), 50) for _ in range(bullets_to_create)]

    # return new_bullets

    for _ in range(len(bullets) - len(new_bullets)):
        new_bullets.append(create_bullet(random.randrange(100, 700), 50))

    return new_bullets

def handle_enemies(enemies, player):
    for enemy in enemies:
        enemy.y += ENEMY_SPEED
    enemies = [enemy for enemy in enemies if enemy.y <= HEIGHT]
    if any(enemy.colliderect(player) for enemy in enemies):
        return False, []
    return True, enemies

def game_over():
    win.fill((0, 0, 0))
    draw_text("Game Over", (255, 255, 255), WIDTH // 2 - 70, HEIGHT // 2 - 18)
    draw_rect((0, 255, 0), play_again_button)
    draw_text("Play Again", (0, 0, 0), WIDTH // 2 - 70, HEIGHT // 2 + 25)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_again_button.collidepoint(event.pos):
                    return

def main():
    global SCORE, SPEED, ENEMY_SPEED, ENEMY_COUNT
    player = create_player(WIDTH // 2, HEIGHT - 50)
    bullets = []
    enemies = [create_enemy() for _ in range(ENEMY_COUNT)]
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullets.append(create_bullet(player.x + player.width // 2, player.y))

        keys = pygame.key.get_pressed()
        player = player.move((-SPEED if keys[pygame.K_LEFT] and player.x - SPEED > 0 else 0, 0))
        player = player.move((SPEED if keys[pygame.K_RIGHT] and player.x + SPEED < WIDTH - player.width else 0, 0))

        bullets = handle_bullets(bullets, enemies)
        run, enemies = handle_enemies(enemies, player)

        draw_window(player, bullets, enemies)

        if not run:
            game_over()
            SCORE, SPEED, ENEMY_SPEED, ENEMY_COUNT = 0, 3, 1, 1
            bullets = []
            enemies = [create_enemy() for _ in range(ENEMY_COUNT)]
            run = True

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
