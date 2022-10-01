###############################################################################
#                                                                             #
# InstInt                                                                     #
#                                                                             #
###############################################################################

import time
import board
import neopixel
from gpiozero import Button, MotionSensor, Motor

###############################################################################
#                                                                             #
# SETUP                                                                       #
#                                                                             #
###############################################################################

# Neopixels
# pixels_count = 510
pixels_count = 10
pixels = neopixel.NeoPixel(
    board.D12,
    pixels_count,
    auto_write=True,
    pixel_order=neopixel.GRB
)
pixels.fill((0,0,0))

# Toque
toque_fita = [0] * 6
toque_fita[1] = Button(10, pull_up=False)
toque_fita[2] = Button(9, pull_up=False)
toque_fita[3] = Button(11, pull_up=False)
toque_fita[4] = Button(0, pull_up=False)
toque_fita[5] = Button(5, pull_up=False)

# Presença
presenca_ir_1 = MotionSensor(8)
presenca_ir_2 = MotionSensor(7)
presenca_ir_3 = MotionSensor(1)
presenca_microondas = MotionSensor(23)  # TO-DO: testar compatibilidade

# Movimento
motor_abre_fecha = Motor(21, 20)
motor_rotacao = Motor(16, 26)
fim_abertura = Button(24, pull_up=False)
fim_fechamento = Button(25, pull_up=False)

###############################################################################
#                                                                             #
# Comportamento Fitas                                                         #
#                                                                             #
###############################################################################

def fita_tocada_1():
    for i in range(2):
        pixels[i] = ((255,255,0))
    
def fita_tocada_2():
    for i in range(2):
        pixels[i + 2] = ((255,0,255))
    
def fita_tocada_3():
    for i in range(2):
        pixels[i + 4] = ((0,255,255))
    
def fita_tocada_4():
    for i in range(2):
        pixels[i + 6] = ((0,255,0))
    
def fita_tocada_5():
    for i in range(2):
        pixels[i + 8] = ((255,0,0))
        
toque_fita[1].when_pressed = fita_tocada_1
toque_fita[2].when_pressed = fita_tocada_2
toque_fita[3].when_pressed = fita_tocada_3
toque_fita[4].when_pressed = fita_tocada_4
toque_fita[5].when_pressed = fita_tocada_5
    
def fita_solta_1():
    for i in range(2):
        pixels[i] = ((0,0,0))
    
def fita_solta_2():
    for i in range(2):
        pixels[i + 2] = ((0,0,0))
    
def fita_solta_3():
    for i in range(2):
        pixels[i + 4] = ((0,0,0))
    
def fita_solta_4():
    for i in range(2):
        pixels[i + 6] = ((0,0,0))
    
def fita_solta_5():
    for i in range(2):
        pixels[i + 8] = ((0,0,0))

toque_fita[1].when_released = fita_solta_1
toque_fita[2].when_released = fita_solta_2
toque_fita[3].when_released = fita_solta_3
toque_fita[4].when_released = fita_solta_4
toque_fita[5].when_released = fita_solta_5

###############################################################################
#                                                                             #
# Comportamento Presença                                                      #
#                                                                             #
###############################################################################

def presenca_detectada_1():
    print("Presença IR 1")
    
def presenca_detectada_2():
    print("Presença IR 2")
    
def presenca_detectada_3():
    print("Presença IR 3")
    
def presenca_detectada_microondas():
    print("Presença Microondas")

presenca_ir_1.when_motion = presenca_detectada_1
presenca_ir_2.when_motion = presenca_detectada_2
presenca_ir_3.when_motion = presenca_detectada_3
presenca_microondas.when_motion = presenca_detectada_microondas

###############################################################################
#                                                                             #
# Comportamento Movimento                                                     #
#                                                                             #
###############################################################################

def abrir():
    if fim_abertura.is_pressed == False:
        motor_abre_fecha.forward(speed=1)

def fechar():
    if fim_fechamento.is_pressed == False:
        motor_abre_fecha.backward(speed=1)

def parar_abertura_fechamento():
    motor_abre_fecha.stop()

fim_abertura.when_pressed = parar_abertura_fechamento
fim_fechamento.when_pressed = parar_abertura_fechamento

###############################################################################
#                                                                             #
# Loop                                                                        #
#                                                                             #
###############################################################################

while True:
    abrir()
    motor_rotacao.forward(speed=0.5)
    time.sleep(5)
    fechar()
    motor_rotacao.backward(speed=0.5)
    time.sleep(5)