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

# Player
player = pygame.Rect(WIDTH // 2, HEIGHT - 50, 50, 50)

# Bullets
bullets = []

# Enemies
enemies = [pygame.Rect(random.randrange(100, 700), 50, 50, 50) for _ in range(ENEMY_COUNT)]

# Play Again button
play_again_button = pygame.Rect(WIDTH // 2 - 70, HEIGHT // 2, 140, 50)

# Higher-order function
def with_display_update(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        pygame.display.update()
    return wrapper

# Pure function
@with_display_update
def draw_window(win, score, player, enemies, bullets):
    win.fill((0, 0, 0))  # Fill the window with black
    score_text = font.render(f"Score: {score}", 1, (255, 255, 255))
    win.blit(score_text, (10, 10))
    pygame.draw.rect(win, (255, 255, 255), player)  # Draw the player
    for enemy in enemies:
        pygame.draw.rect(win, (255, 0, 0), enemy)  # Draw the enemies
    for bullet in bullets:
        pygame.draw.rect(win, (0, 255, 0), bullet)  # Draw the bullets

def handle_bullets():
    global SCORE
    for bullet in bullets:
        bullet.y -= BULLET_SPEED
        for enemy in enemies:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                SCORE += 10
                if SCORE % 50 == 0:
                    global ENEMY_SPEED
                    ENEMY_SPEED += 1
                    global SPEED
                    SPEED += 1
                    global ENEMY_COUNT
                    ENEMY_COUNT += 1
                enemies.append(pygame.Rect(random.randrange(100, 700), 50, 50, 50))
                break
        else:
            if bullet.y < 0:
                bullets.remove(bullet)

def handle_enemies():
    for enemy in enemies:
        enemy.y += ENEMY_SPEED
        if enemy.y > HEIGHT:
            enemies.remove(enemy)
            enemies.append(pygame.Rect(random.randrange(100, 700), 50, 50, 50))
        if enemy.colliderect(player):
            return False
    return True

def game_over():
    win.fill((0, 0, 0))  # Fill the window with black
    game_over_text = font.render("Game Over", 1, (255, 255, 255))
    win.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))
    pygame.draw.rect(win, (0, 255, 0), play_again_button)
    play_again_text = font.render("Play Again", 1, (0, 0, 0))
    win.blit(play_again_text, (WIDTH // 2 - play_again_text.get_width() // 2, HEIGHT // 2 + play_again_text.get_height() // 2))

@with_display_update
def main():
    global SCORE, SPEED, ENEMY_SPEED, ENEMY_COUNT, bullets, enemies
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(60)  # Cap the frame rate at 60 FPS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = pygame.Rect(player.x + player.width // 2, player.y, 10, 20)
                    bullets.append(bullet)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - SPEED > 0:
            player.x -= SPEED
        if keys[pygame.K_RIGHT] and player.x + SPEED < WIDTH - player.width:
            player.x += SPEED

        handle_bullets()
        run = handle_enemies()

        draw_window(win, SCORE, player, enemies, bullets)

        if not run:
            game_over()
            SCORE = 0
            SPEED = 3
            ENEMY_SPEED = 1
            ENEMY_COUNT = 1
            bullets = []
            enemies = [pygame.Rect(random.randrange(100, 700), 50, 50, 50) for _ in range(ENEMY_COUNT)]
            run = True

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
