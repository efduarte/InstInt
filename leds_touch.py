import time
import board
import neopixel
from grove.gpio import GPIO

num_pixels = 510 #número de LEDs

pixels = neopixel.NeoPixel(
    board.D12,
    num_pixels,
    # brightness=0.2,
    auto_write=True,
    pixel_order=neopixel.GRB
)

touch1 = GPIO(10, GPIO.IN)
touch2 = GPIO( 9, GPIO.IN)
touch3 = GPIO(11, GPIO.IN)
touch4 = GPIO( 0, GPIO.IN)
touch5 = GPIO( 5, GPIO.IN)

touch1_last = 0
touch2_last = 0
touch3_last = 0
touch4_last = 0
touch5_last = 0

for i in range(60):
    pixels[i + 450] = (255, 255, 255)
    time.sleep(0.01) 

while True:
    touch1_current = touch1.read()
    touch2_current = touch2.read()
    touch3_current = touch3.read()
    touch4_current = touch4.read()
    touch5_current = touch5.read()

    if touch1_current == 1 and touch1_last == 0:        
        for i in range(90):
            pixels[i] = (255, 255, 255)
            time.sleep(0.01)
    elif touch1_current == 0 and touch1_last == 1:
        for i in range(90):
            pixels[i] = (0, 0, 0)
            time.sleep(0.01)
    touch1_last = touch1_current

    if touch2_current == 1 and touch2_last == 0:        
        for i in range(90):
            pixels[i + 90] = (255, 255, 255)
            time.sleep(0.01)
    elif touch2_current == 0 and touch2_last == 1:
        for i in range(90):
            pixels[i + 90] = (0, 0, 0)
            time.sleep(0.01)     
    touch2_last = touch2_current

    if touch3_current == 1 and touch3_last == 0:        
        for i in range(90):
            pixels[i + 180] = (255, 255, 255)
            time.sleep(0.01)
    elif touch3_current == 0 and touch3_last == 1:
        for i in range(90):
            pixels[i + 180] = (0, 0, 0)
            time.sleep(0.01)        
    touch3_last = touch3_current

    if touch4_current == 1 and touch4_last == 0:        
        for i in range(90):
            pixels[i + 270] = (255, 255, 255)
            time.sleep(0.01)
    elif touch4_current == 0 and touch4_last == 1:
        for i in range(90):
            pixels[i + 270] = (0, 0, 0)
            time.sleep(0.01)        
    touch4_last = touch4_current

    if touch5_current == 1 and touch5_last == 0:        
        for i in range(90):
            pixels[i + 360] = (255, 255, 255)
            time.sleep(0.01)
    elif touch5_current == 0 and touch5_last == 1:
        for i in range(90):
            pixels[i + 360] = (0, 0, 0)
            time.sleep(0.01)        
    touch5_last = touch5_current

    for i in range(num_pixels):
        pixels[i] = (255, 255, 255)
        time.sleep(0.01)