import numpy as np
from PIL import Image

WIDTH, HEIGHT = 800, 600
img = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)

def draw_pixel(x, y, color):
    if 0 <= x < WIDTH and 0 <= y < HEIGHT:
        img[y, x, :] = color  # Note the additional ':' to index the color channels

def draw_circle(h, k, r, color):
    x = 0
    y = r
    d = 1 - r

    while y > x:
        draw_pixel(h + x, k + y, color)
        draw_pixel(h + y, k + x, color)
        draw_pixel(h - x, k + y, color)
        draw_pixel(h - y, k + x, color)
        draw_pixel(h + x, k - y, color)
        draw_pixel(h + y, k - x, color)
        draw_pixel(h - x, k - y, color)
        draw_pixel(h - y, k - x, color)

        if d < 0:
            d += 2 * x + 3
        else:
            d += 2 * (x - y) + 5
            y -= 1
        x += 1

for center in [[0, 0], [0, 0.5], [-0.5, 0], [0, -0.5], [0.5, 0], [0.35, 0.35], [0.35, -0.35], [-0.35, -0.35], [-0.35, 0.35]]:
    h = int(center[0] * WIDTH / 2 + WIDTH / 2)
    k = int(center[1] * HEIGHT / 2 + HEIGHT / 2)
    r = int(0.5 * min(WIDTH, HEIGHT))
    color = (255, 255, 255)

    draw_circle(h, k, r, color)

# Display the image using Pillow
pil_img = Image.fromarray(img)
pil_img.show()


