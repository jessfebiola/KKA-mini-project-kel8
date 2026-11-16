"""Efek kembang api untuk ending Level 3 (tanpa asset tambahan)."""
import math
import random
import pygame

_particles = []
_last_spawn = 0
_rng = random.Random()
_COLORS = [(255, 91, 109), (255, 210, 84), (100, 222, 255),
           (172, 120, 255), (135, 255, 170), (255, 151, 230)]


def reset():
    global _last_spawn
    _particles.clear()
    _last_spawn = 0


def _burst():
    x = _rng.randint(200, 1250)
    y = _rng.randint(100, 520)
    color = _rng.choice(_COLORS)
    for i in range(52):
        angle = 2 * math.pi * i / 52 + _rng.uniform(-0.09, 0.09)
        speed = _rng.uniform(1.7, 5.0)
        _particles.append([float(x), float(y), math.cos(angle)*speed,
                           math.sin(angle)*speed, _rng.randint(38, 75), color])


def draw(screen, now_ms):
    global _last_spawn
    if _last_spawn == 0 or now_ms - _last_spawn >= 600:
        _burst()
        _last_spawn = now_ms
    # Alpha surface membuat kembang api lebih lembut di atas gambar.
    layer = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    alive = []
    for p in _particles:
        x, y, vx, vy, life, color = p
        x += vx
        y += vy
        vy += 0.035
        vx *= 0.99
        life -= 1
        if life > 0:
            alpha = min(255, life * 5)
            pygame.draw.circle(layer, (*color, alpha), (int(x), int(y)), 3)
            alive.append([x, y, vx, vy, life, color])
    _particles[:] = alive
    screen.blit(layer, (0, 0))
