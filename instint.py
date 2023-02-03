###############################################################################
#                                                                             #
# InstInt                                                                     #
#                                                                             #
###############################################################################

import time
import board
import neopixel
from gpiozero import Button, MotionSensor, Motor
import csv
from datetime import datetime
import signal
import sys

###############################################################################
#                                                                             #
# SETUP                                                                       #
#                                                                             #
###############################################################################

prototipo = True

# Neopixels
if prototipo is True:
    pixels_count = 10
    pixels_count_fita = 2
    pixels_count_matriz = 0

else:
    pixels_count = 766
    pixels_count_fita = 90
    pixels_count_matriz = 256

pixels = neopixel.NeoPixel(
    board.D12,
    pixels_count,
    auto_write=True,
    pixel_order=neopixel.GRB
)

pixels.fill((0, 0, 0))

# Toque
toque_fita_1 = Button(10, pull_up=False)
toque_fita_2 = Button(9, pull_up=False)
toque_fita_3 = Button(11, pull_up=False)
toque_fita_4 = Button(0, pull_up=False)
toque_fita_5 = Button(5, pull_up=False)

# Presença
presenca_ir_1 = MotionSensor(8)
presenca_ir_2 = MotionSensor(7)
presenca_ir_3 = MotionSensor(1)
presenca_microondas = MotionSensor(23)

# Movimento
motor_vertical = Motor(21, 20)
velocidade_vertical = 1  # confirmar
motor_rotacao = Motor(16, 26)
velocidade_rotacao = 0.5  # confirmar
fim_abertura = Button(24, pull_up=False)
fim_fechamento = Button(25, pull_up=False)

agora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_filename = "log_{}.csv".format(agora)


def log_data(event):
    print(event)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_filename, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([now, event])


def signal_handler(signal, frame):
    log_data("Encerrando a aplicação")
    pixels.fill((0, 0, 0))
    motor_vertical.stop()
    motor_rotacao.stop()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

###############################################################################
#                                                                             #
# Comportamento Fitas                                                         #
#                                                                             #
###############################################################################


def fita_tocada_1():
    log_data("Toque na Fita 1")
    for i in range(pixels_count_fita):
        pixels[pixels_count_matriz + i] = ((255, 255, 0))


def fita_tocada_2():
    log_data("Toque na Fita 2")
    for i in range(pixels_count_fita):
        pixels[pixels_count_matriz + i + pixels_count_fita] = ((255, 0, 255))


def fita_tocada_3():
    log_data("Toque na Fita 3")
    for i in range(pixels_count_fita):
        pixels[pixels_count_matriz + i + pixels_count_fita * 2] = ((0, 255, 255))


def fita_tocada_4():
    log_data("Toque na Fita 4")
    for i in range(pixels_count_fita):
        pixels[pixels_count_matriz + i + pixels_count_fita * 3] = ((0, 255, 0))


def fita_tocada_5():
    log_data("Toque na Fita 5")
    for i in range(pixels_count_fita):
        pixels[pixels_count_matriz + i + pixels_count_fita * 4] = ((255, 0, 0))


toque_fita_1.when_pressed = fita_tocada_1
toque_fita_2.when_pressed = fita_tocada_2
toque_fita_3.when_pressed = fita_tocada_3
toque_fita_4.when_pressed = fita_tocada_4
toque_fita_5.when_pressed = fita_tocada_5


def fita_solta_1():
    log_data("Fim do toque na Fita 1")
    for i in range(2):
        pixels[i] = ((0, 0, 0))


def fita_solta_2():
    log_data("Fim do toque na Fita 2")
    for i in range(2):
        pixels[i + 2] = ((0, 0, 0))


def fita_solta_3():
    log_data("Fim do toque na Fita 3")
    for i in range(2):
        pixels[i + 4] = ((0, 0, 0))


def fita_solta_4():
    log_data("Fim do toque na Fita 4")
    for i in range(2):
        pixels[i + 6] = ((0, 0, 0))


def fita_solta_5():
    log_data("Fim do toque na Fita 5")
    for i in range(2):
        pixels[i + 8] = ((0, 0, 0))


toque_fita_1.when_released = fita_solta_1
toque_fita_2.when_released = fita_solta_2
toque_fita_3.when_released = fita_solta_3
toque_fita_4.when_released = fita_solta_4
toque_fita_5.when_released = fita_solta_5

###############################################################################
#                                                                             #
# Comportamento Presença                                                      #
#                                                                             #
###############################################################################


def presenca_detectada_1():
    log_data("Presença no Sensor IR 1")


def presenca_detectada_2():
    log_data("Presença no Sensor IR 2")


def presenca_detectada_3():
    log_data("Presença no Sensor IR 3")


def presenca_detectada_microondas():
    log_data("Presença no Sensor Microondas")

presenca_ir_1.when_motion = presenca_detectada_1
presenca_ir_2.when_motion = presenca_detectada_2
presenca_ir_3.when_motion = presenca_detectada_3
presenca_microondas.when_motion = presenca_detectada_microondas

###############################################################################
#                                                                             #
# Comportamento Movimento                                                     #
#                                                                             #
###############################################################################


def abrir(velocidade=velocidade_vertical):
    if fim_abertura.is_pressed is False:
        log_data("Abrindo")
        motor_vertical.forward(speed=velocidade)


def fechar(velocidade=velocidade_vertical):
    if fim_fechamento.is_pressed is False:
        log_data("Fechando")
        motor_vertical.backward(speed=velocidade)


def parar_abertura():
    log_data("Parando abertura")
    motor_vertical.stop()


def parar_fechamento():
    log_data("Parando fechamento")
    motor_vertical.stop()

fim_abertura.when_pressed = parar_abertura
fim_fechamento.when_pressed = parar_fechamento


def girar_direita(velocidade=velocidade_rotacao):
    log_data("Girando no sentido horário")
    motor_rotacao.forward(speed=velocidade)


def girar_esquerda(velocidade=velocidade_rotacao):
    log_data("Girando no sentido anti-horário")
    motor_rotacao.backward(speed=velocidade)


def parar_giro():
    log_data("Parando giro")
    motor_rotacao.stop()

###############################################################################
#                                                                             #
# Loop                                                                        #
#                                                                             #
###############################################################################

while True:
    abrir()
    girar_direita()
    time.sleep(5)

    fechar()
    girar_esquerda()
    time.sleep(5)
