import random
import sys

import pygame


# ----------------------------
# Dino Runner (Chrome-style)
# ----------------------------
# Controls:
#   Space / Up / W : Jump
#   R               : Restart after game over
#   Esc             : Quit


SCREEN_W, SCREEN_H = 900, 300
FPS = 60
GROUND_Y = 240

DINO_W, DINO_H = 44, 44
CACTUS_W_RANGE = (20, 40)

# Colors
WHITE = (245, 245, 245)
BLACK = (15, 15, 15)
BG_COLOR = (255, 255, 255)
GROUND_COLOR = (40, 40, 40)
DINO_COLOR = (40, 160, 70)
CACTUS_COLOR = (30, 120, 30)
CLOUD_COLOR = (235, 235, 235)


def clamp(n, lo, hi):
    return max(lo, min(hi, n))


def draw_text(surface, text, size, x, y, color=BLACK, center=False):
    font = pygame.font.SysFont(None, size)
    img = font.render(text, True, color)
    rect = img.get_rect()
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    surface.blit(img, rect)


class Dino:
    def __init__(self):
        self.reset()

    def reset(self):
        self.x = 120
        self.y = GROUND_Y - DINO_H
        self.vy = 0
        self.on_ground = True
        self.jump_sfx_timer = 0

    def jump(self):
        if self.on_ground:
            # A simple physics setup
            self.vy = -12.5
            self.on_ground = False

    def update(self, dt):
        # dt is in seconds. Scale gravity/jump accordingly.
        gravity = 35.0  # px/s^2
        self.vy += gravity * dt
        self.y += self.vy * dt

        if self.y >= GROUND_Y - DINO_H:
            self.y = GROUND_Y - DINO_H
            self.vy = 0
            self.on_ground = True

    def rect(self):
        # Slightly shrink for more forgiving collision
        return pygame.Rect(self.x + 6, int(self.y) + 6, DINO_W - 12, DINO_H - 10)

    def draw(self, surface):
        pygame.draw.rect(surface, DINO_COLOR, pygame.Rect(self.x, int(self.y), DINO_W, DINO_H), border_radius=8)


class Cactus:
    def __init__(self, speed, level):
        self.w = random.randint(*CACTUS_W_RANGE)
        self.h = random.randint(40, 90)
        self.x = SCREEN_W + random.randint(30, 200)
        self.y = GROUND_Y - self.h
        self.speed = speed
        self.level = level

    def update(self, dt):
        self.x -= self.speed * dt

    def is_offscreen(self):
        return self.x + self.w < 0

    def rect(self):
        return pygame.Rect(int(self.x), int(self.y), self.w, self.h)

    def draw(self, surface):
        # Draw a simple cactus: body + small top arms
        body = pygame.Rect(int(self.x), int(self.y), self.w, self.h)
        pygame.draw.rect(surface, CACTUS_COLOR, body, border_radius=6)

        # Arms (deterministic-ish based on size)
        arm_count = 1 if self.w < 30 else 2
        for i in range(arm_count):
            arm_w = max(6, self.w // 5)
            arm_h = self.h // 4
            px = int(self.x) + (self.w // (arm_count + 1)) * (i + 1) - arm_w // 2
            py = int(self.y) + self.h - arm_h - 8
            arm = pygame.Rect(px, py, arm_w, arm_h)
            pygame.draw.rect(surface, CACTUS_COLOR, arm, border_radius=4)


class Cloud:
    def __init__(self):
        self.reset(initial=True)

    def reset(self, initial=False):
        self.x = random.randint(0, SCREEN_W) if initial else SCREEN_W + random.randint(0, 300)
        self.y = random.randint(20, 90)
        self.w = random.randint(60, 120)
        self.h = self.w // 3
        self.speed = random.uniform(10.0, 22.0)

    def update(self, dt):
        self.x -= self.speed * dt
        if self.x + self.w < 0:
            self.reset(initial=False)

    def draw(self, surface):
        x = int(self.x)
        y = int(self.y)
        pygame.draw.ellipse(surface, CLOUD_COLOR, pygame.Rect(x, y, self.w, self.h))
        pygame.draw.ellipse(surface, CLOUD_COLOR, pygame.Rect(x + 18, y - self.h // 2, self.w // 2, self.h))
        pygame.draw.ellipse(surface, CLOUD_COLOR, pygame.Rect(x + 38, y, self.w // 2, self.h))


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption("Dino Runner")
    clock = pygame.time.Clock()

    dino = Dino()
    clouds = [Cloud(), Cloud(), Cloud()]
    cactuses = []

    # Difficulty / speed settings
    base_speed = 260.0  # px/s
    spawn_interval = 1.15  # seconds
    time_since_spawn = 0.0

    score = 0
    best = 0
    game_over = False

    def restart():
        nonlocal cactuses, score, game_over, time_since_spawn
        dino.reset()
        cactuses = []
        score = 0
        time_since_spawn = 0.0
        game_over = False

    restart()

    while True:
        dt = clock.tick(FPS) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if game_over and event.key == pygame.K_r:
                    restart()

                if not game_over and event.key in (pygame.K_SPACE, pygame.K_UP, pygame.K_w):
                    dino.jump()

                if game_over and event.key in (pygame.K_SPACE, pygame.K_UP):
                    # allow jump key to restart too
                    restart()

        keys = pygame.key.get_pressed()
        if not game_over:
            if keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]:
                # avoid continuous jump: Dino.jump already checks on_ground
                dino.jump()

        # --- Update ---
        for cloud in clouds:
            cloud.update(dt)

        if not game_over:
            # Increase difficulty with score
            level = score // 250  # step difficulty
            speed = base_speed + level * 30

            time_since_spawn += dt
            current_interval = max(0.55, spawn_interval - level * 0.07)

            if time_since_spawn >= current_interval:
                # spawn cactus
                cactuses.append(Cactus(speed=speed, level=level))
                time_since_spawn = 0.0

            dino.update(dt)

            for c in list(cactuses):
                c.speed = speed
                c.update(dt)
                if c.is_offscreen():
                    cactuses.remove(c)

            # Score by time survived
            score += int(120 * dt)
            best = max(best, score)

            # Collision
            dino_r = dino.rect()
            for c in cactuses:
                if dino_r.colliderect(c.rect()):
                    game_over = True
                    break

        # --- Draw ---
        screen.fill(BG_COLOR)

        # Ground
        pygame.draw.rect(screen, GROUND_COLOR, pygame.Rect(0, GROUND_Y, SCREEN_W, SCREEN_H - GROUND_Y))
        pygame.draw.line(screen, (90, 90, 90), (0, GROUND_Y), (SCREEN_W, GROUND_Y), 2)

        for cloud in clouds:
            cloud.draw(screen)

        # Cactuses
        for c in cactuses:
            c.draw(screen)

        # Dino
        dino.draw(screen)

        # HUD
        draw_text(screen, f"Score: {score}", 28, 20, 10)
        draw_text(screen, f"Best: {best}", 24, 20, 40)

        if game_over:
            draw_text(screen, "GAME OVER", 72, SCREEN_W // 2, SCREEN_H // 2 - 40, color=BLACK, center=True)
            draw_text(screen, "Press R to Restart", 34, SCREEN_W // 2, SCREEN_H // 2 + 10, color=BLACK, center=True)

        pygame.display.flip()


if __name__ == "__main__":
    main()

