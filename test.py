import time
import board
import neopixel
from gpiozero import Button

# Setup

num_pixels = 510

pixels = neopixel.NeoPixel(
    board.D12,
    num_pixels,
    auto_write=True,
    pixel_order=neopixel.GRB
)

touch1 = Button(10)
touch2 = Button(9)
touch3 = Button(11)
touch4 = Button(0)
touch5 = Button(5)

# Início dos Testes

#Vermelho
pixels.fill((255, 0, 0))
time.sleep(3)

#Verde
pixels.fill((0, 255, 0))
time.sleep(3)

#Azul
pixels.fill((0, 0, 255))
time.sleep(3)

#Apagados
pixels.fill((0, 0, 0))
time.sleep(3)

#Brancos um a um
for i in range(num_pixels):
    pixels[i] = (255, 255, 255)
    time.sleep(0.01)
time.sleep(3)
pixels.fill((0, 0, 0))

#Testar fita 1
touch1.wait_for_press()
pixels[0:89] = (255, 255, 255) * 90
touch1.wait_for_release()
pixels[0:89] = (0, 0, 0) * 90
touch1.wait_for_press()
pixels[0:89] = (255, 255, 255) * 90
touch1.wait_for_release()