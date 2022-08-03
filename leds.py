import time
import board
import neopixel

num_pixels = 510 #número de LEDs

pixels = neopixel.NeoPixel(
    board.D12,
    num_pixels,
    # brightness=0.2,
    auto_write=True,
    pixel_order=neopixel.GRB
)

while True:
    #RED
    pixels.fill((255, 0, 0))
    time.sleep(3)

    #GREEN
    pixels.fill((0, 255, 0))
    time.sleep(3)

    #BLUE
    pixels.fill((0, 0, 255))
    time.sleep(3)

    pixels.fill((0, 0, 0))

    for i in range(num_pixels):
        pixels[0] = (255, 255, 255)
        time.sleep(0.01)
        
    time.sleep(3)