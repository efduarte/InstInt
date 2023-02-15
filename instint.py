###############################################################################
#                                                                             #
# InstInt                                                                     #
#                                                                             #
###############################################################################

import os
import time
import board
import neopixel
from adafruit_led_animation.helper import PixelSubset
from gpiozero import Button, MotionSensor, Motor
import csv
from datetime import datetime
import signal
import sys
from pydub import AudioSegment
from pydub.utils import get_player_name
from threading import Thread
import argparse
import tempfile
import subprocess

###############################################################################
#                                                                             #
# SETUP                                                                       #
#                                                                             #
###############################################################################

# Argumentos do Script
parser = argparse.ArgumentParser(prog='InstInt')
parser.add_argument('-p', '--prototipo', action='store_true')
parser.add_argument('-l', '--logname', default='log_')
parser.add_argument('-s', '--som', default='instint')  # instint ou piano
args = parser.parse_args()

# Logs de Sistema e Argumentos
agora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_filename = args.logname + "_{}.csv".format(agora)


def log_data(event):
    print(event)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_filename, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([now, event])

log_data("Inicializando InstInt com --som " + args.som)

# Neopixels
if (args.prototipo):
    pixels_count = 10
    pixels_count_fita = 1
    pixels_count_matriz = 3
    pixels_count_caule = 2

else:
    pixels_count = 766
    pixels_count_fita = 90
    pixels_count_matriz = 256
    pixels_count_caule = 60

pixels = neopixel.NeoPixel(
    board.D10,
    pixels_count,
    brightness=1.0,
    auto_write=True,
    pixel_order=neopixel.GRB
)

inicio_matriz = 0
fim_matriz = pixels_count_matriz
matriz = PixelSubset(pixels, 0, pixels_count_matriz)

inicio_fita_1 = pixels_count_matriz
fim_fita_1 = inicio_fita_1 + pixels_count_fita
fita_1 = PixelSubset(pixels, inicio_fita_1, fim_fita_1)

inicio_fita_2 = fim_fita_1
fim_fita_2 = inicio_fita_2 + pixels_count_fita
fita_2 = PixelSubset(pixels, inicio_fita_2, fim_fita_2)

inicio_fita_3 = fim_fita_2
fim_fita_3 = inicio_fita_3 + pixels_count_fita
fita_3 = PixelSubset(pixels, inicio_fita_3, fim_fita_3)

inicio_fita_4 = fim_fita_3
fim_fita_4 = inicio_fita_4 + pixels_count_fita
fita_4 = PixelSubset(pixels, inicio_fita_4, fim_fita_4)

inicio_fita_5 = fim_fita_4
fim_fita_5 = inicio_fita_5 + pixels_count_fita
fita_5 = PixelSubset(pixels, inicio_fita_5, fim_fita_5)

inicio_caule = fim_fita_5
fim_caule = pixels_count
caule = PixelSubset(pixels, inicio_caule, fim_caule)

BRANCO = (160, 160, 160)  # brilho reduzido
SUPERBRANCO = (255, 255, 255)  # usar somente no 'caule'
PRETO = (0, 0, 0)  # desligado
VERMELHO = (255, 0, 0)
CARMESIM = (220, 20, 60)
PINK = (255, 192, 203)
PINKPROFUNDO = (255, 20, 147)
LARANJA = (255, 165, 0)
SALMAO = (255, 160, 122)
AMARELO = (255, 255, 0)
DOURADO = (255, 215, 0)
ROXO = (128, 0, 128)
MAGENTA = (255, 0, 255)
VERDE = (0, 255, 0)
CERCETA = (0, 128, 128)
AZUL = (0, 0, 255)
CIANO = (0, 255, 255)
MARROM = (165, 42, 42)
CHOCOLATE = (210, 105, 30)

# Toque
toque_fita_1 = Button(12, pull_up=False)
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
velocidade_vertical = 1
motor_rotacao = Motor(16, 26)
velocidade_rotacao_1 = 0.5
velocidade_rotacao_2 = 1.0
fim_abertura = Button(24, pull_up=False)
fim_fechamento = Button(25, pull_up=False)


# Desligar motores e luzes ao encerrar o sistema
def signal_handler(signal, frame):
    log_data("Encerrando a aplicação")
    pixels.fill(PRETO)
    motor_vertical.stop()
    motor_rotacao.stop()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Arquivos de Audio e Play com Threads
audio_file_0 = "audio/" + args.som + "/0.wav"
audio_file_1 = "audio/" + args.som + "/1.wav"
audio_file_2 = "audio/" + args.som + "/2.wav"
audio_file_3 = "audio/" + args.som + "/3.wav"
audio_file_4 = "audio/" + args.som + "/4.wav"
audio_file_5 = "audio/" + args.som + "/5.wav"

PLAYER = get_player_name()


def _play_with_ffplay_suppress(seg):
    with tempfile.NamedTemporaryFile("w+b", suffix=".wav") as f:
        seg.export(f.name, "wav")
        devnull = open(os.devnull, 'w')
        subprocess.call([PLAYER, "-nodisp", "-autoexit", "-hide_banner", f.name], stdout=devnull, stderr=devnull)


def play_threaded(filename, repeat=False, gain=0):
    def play_audio():
        while True:
            sound = AudioSegment.from_file(filename, format="wav")
            sound = sound.apply_gain(gain)
            _play_with_ffplay_suppress(sound)
            log_data("Tocando audio" + filename)
            if not repeat:
                break

    thread = Thread(target=play_audio)
    thread.start()

###############################################################################
#                                                                             #
# Comportamento Fitas                                                         #
#                                                                             #
###############################################################################


def fita_tocada_1():
    log_data("Toque na Fita 1")
    fita_1.fill(VERMELHO)
    estimulo("toque")
    play_threaded(audio_file_1)


def fita_tocada_2():
    log_data("Toque na Fita 2")
    fita_2.fill(AMARELO)
    estimulo("toque")
    play_threaded(audio_file_2)


def fita_tocada_3():
    log_data("Toque na Fita 3")
    fita_3.fill(PINK)
    estimulo("toque")
    play_threaded(audio_file_3)


def fita_tocada_4():
    log_data("Toque na Fita 4")
    fita_4.fill(CIANO)
    estimulo("toque")
    play_threaded(audio_file_4)


def fita_tocada_5():
    log_data("Toque na Fita 5")
    fita_5.fill(VERDE)
    estimulo("toque")
    play_threaded(audio_file_5)


toque_fita_1.when_pressed = fita_tocada_1
toque_fita_2.when_pressed = fita_tocada_2
toque_fita_3.when_pressed = fita_tocada_3
toque_fita_4.when_pressed = fita_tocada_4
toque_fita_5.when_pressed = fita_tocada_5


def fita_solta_1():
    log_data("Fim do toque na Fita 1")
    fita_1.fill(BRANCO)


def fita_solta_2():
    log_data("Fim do toque na Fita 2")
    fita_2.fill(BRANCO)


def fita_solta_3():
    log_data("Fim do toque na Fita 3")
    fita_3.fill(BRANCO)


def fita_solta_4():
    log_data("Fim do toque na Fita 4")
    fita_4.fill(BRANCO)


def fita_solta_5():
    log_data("Fim do toque na Fita 5")
    fita_5.fill(BRANCO)


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
    presenca_detectada()


def presenca_detectada_2():
    log_data("Presença no Sensor IR 2")
    presenca_detectada()


def presenca_detectada_3():
    log_data("Presença no Sensor IR 3")
    presenca_detectada()


def presenca_detectada_microondas():
    log_data("Presença no Sensor Microondas")
    presenca_detectada()


def presenca_detectada():
    estimulo("presenca")

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


def girar_direita(velocidade=velocidade_rotacao_1):
    log_data("Girando no sentido horário")
    motor_rotacao.forward(speed=velocidade)
    matriz.fill(AZUL)


def girar_esquerda(velocidade=velocidade_rotacao_1):
    log_data("Girando no sentido anti-horário")
    motor_rotacao.backward(speed=velocidade)
    matriz.fill(VERMELHO)


def parar_giro():
    log_data("Parando giro")
    motor_rotacao.stop()
    matriz.fill(BRANCO)

###############################################################################
#                                                                             #
# Estados                                                                     #
#                                                                             #
###############################################################################

estado = 'parado'


def estimulo(tipo):
    global ultimo_estimulo
    global estado

    if tipo == "presenca" and estado != "parado":
        return

    ultimo_estimulo = 0

    if estado == "parado":
        log_data("Mudança de estado: de 'parado' para 'direita_1'")
        abrir()
        girar_direita(velocidade_rotacao_1)
        estado = 'direita_1'
        return

    elif estado == "direita_1":
        log_data("Mudança de estado: de 'direita_1' para 'direita_2'")
        girar_direita(velocidade_rotacao_2)
        estado = 'direita_2'
        return

    elif estado == "direita_2":
        log_data("Estado mantido em 'direita_2'")
        return

    elif estado == "esquerda_1":
        log_data("Mudança de estado: de 'esquerda_1' para 'esquerda_2'")
        girar_esquerda(velocidade_rotacao_2)
        estado = 'esquerda_2'
        return

    elif estado == "esquerda_2":
        log_data("Estado mantido em 'esquerda_2'")
        return

    else:
        log_data("Mudança de estado: de #ERRO para 'parado'")
        estado = 'parado'
        parar_giro()
        fechar()
        return


def falta_de_estimulo():
    global estado
    if estado == "parado":
        log_data("Estado mantido em 'parado'")
        return

    elif estado == "direita_1":
        log_data("Mudança de estado: de 'direita_1' para 'parado'")
        estado = 'parado'
        parar_giro()
        fechar()
        return

    elif estado == "direita_2":
        log_data("Mudança de estado: de 'direita_2' para 'esquerda_1'")
        girar_esquerda(velocidade_rotacao_1)
        estado = 'esquerda_1'
        return

    elif estado == "esquerda_1":
        log_data("Mudança de estado: de 'esquerda_1' para 'parado'")
        estado = 'parado'
        parar_giro()
        fechar()
        return

    elif estado == "esquerda_2":
        log_data("Mudança de estado: de 'esquerda_2' para 'direita_1'")
        girar_direita(velocidade_rotacao_1)
        estado = 'direita_1'
        return

    else:
        log_data("Mudança de estado: de #ERRO para 'parado'")
        estado = 'parado'
        parar_giro()
        fechar()
        return


###############################################################################
#                                                                             #
# Loop                                                                        #
#                                                                             #
###############################################################################

fechar()
pixels.fill(BRANCO)
caule.fill(SUPERBRANCO)
ultimo_estimulo = 0
play_threaded(audio_file_0, repeat=True, gain='-10')

while True:
    ultimo_estimulo += 1
    time.sleep(1)
    if ultimo_estimulo >= 15:
        falta_de_estimulo()
        ultimo_estimulo = 0
